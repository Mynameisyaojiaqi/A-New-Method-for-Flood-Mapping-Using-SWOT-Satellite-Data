
import os
import numpy as np
import rasterio
from rasterio.warp import reproject, Resampling
from scipy.optimize import curve_fit
from scipy.integrate import quad
from tqdm import tqdm


# Define Gaussian function
def gaussian(x, amp, mu, sigma):
    return amp * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


# Automatically find the best initial parameters
def find_best_initial_params(x_data, y_data):
    amp_guess = np.max(y_data)  # Amplitude guess: maximum value of data
    mu_guess = np.sum(x_data * y_data) / np.sum(y_data)  # Mean guess: weighted average
    sigma_guess = np.std(x_data)  # Standard deviation guess: standard deviation of data

    # If the guess parameters are unreasonable, use default values as fallback
    if np.isnan(mu_guess) or np.isnan(sigma_guess) or sigma_guess == 0:
        mu_guess = np.median(x_data)
        sigma_guess = (np.max(x_data) - np.min(x_data)) / 4
    return [amp_guess, mu_guess, sigma_guess]


# File path and order
tif_dir = r"H:\20250831密云水库\rrrr"  # Replace with your raster file folder path

tif_files = sorted(os.listdir(tif_dir))  # Sort files by name (ensure they represent a time series)

# Extract the time series for x-axis (from file names)
x_data = np.array([int(os.path.splitext(f)[0]) for f in tif_files])

# Get target shape (based on the first TIFF file)
with rasterio.open(os.path.join(tif_dir, tif_files[0])) as src:
    target_shape = src.shape
    target_transform = src.transform
    target_crs = src.crs

# Register and resample all TIFF files
tif_stack = []
for tif_file in tif_files:
    with rasterio.open(os.path.join(tif_dir, tif_file)) as src:
        data = src.read(1).astype(np.float32)  # Read the first band and convert to float
        data_resampled = np.full(target_shape, np.nan, dtype=np.float32)  # Fill the target shape with NaN
        reproject(
            source=data,
            destination=data_resampled,
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=target_transform,
            dst_crs=target_crs,
            resampling=Resampling.bilinear
        )
        tif_stack.append(data_resampled)

tif_stack = np.array(tif_stack)  # Convert to numpy array with shape (z, rows, cols)

# Initialize result arrays
rows, cols = tif_stack.shape[1], tif_stack.shape[2]
area_result = np.full((rows, cols), np.nan)  # For storing area results
peak_x_result = np.full((rows, cols), np.nan)  # For storing Gaussian peak positions

# Iterate over each pixel for Gaussian fitting and area calculation
print("Processing data...")

# Get fixed integration range (based on file names)
integration_min = x_data.min()  # Minimum value in file names
integration_max = x_data.max()  # Maximum value in file names

for i in tqdm(range(rows), desc="Row processing progress", unit="row"):
    for j in range(cols):
        y_data = tif_stack[:, i, j]  # Value sequence for the current pixel

        # Count the number of invalid values
        nan_count = np.isnan(y_data).sum()

        # Skip the pixel if invalid values exceed half of the time series
        if nan_count > len(y_data) / 2:
            continue

        # Filter out invalid values, keeping only valid data
        valid_mask = ~np.isnan(y_data)
        x_data_valid = x_data[valid_mask]
        y_data_valid = y_data[valid_mask]

        # Skip the pixel if there are fewer than 3 valid points
        if len(y_data_valid) < 3:
            continue

        # Gaussian fitting
        try:
            # Automatically find initial parameters
            p0 = find_best_initial_params(x_data_valid, y_data_valid)

            # Call curve_fit with maxfev parameter
            popt, _ = curve_fit(
                gaussian,
                x_data_valid,
                y_data_valid,
                p0=p0,
                maxfev=1000000000
            )

            amp_fit, mu_fit, sigma_fit = popt

            # Check if the peak position is within a valid range [0, 365]
            if mu_fit < 0 or mu_fit > 1000:
                area_result[i, j] = np.nan
                peak_x_result[i, j] = np.nan
                continue

            # Save the Gaussian peak position (mu)
            peak_x_result[i, j] = mu_fit

            # Use the original minimum value as the baseline
            original_min = np.min(y_data_valid)  # Original minimum value

            # Define the integration function
            def area_func(x):
                return gaussian(x, amp_fit, mu_fit, sigma_fit) - original_min

            # Calculate the area (integral), range from the minimum to maximum x of the time series
            area, _ = quad(area_func, integration_min, integration_max)

            # Check if the integral area exceeds 10000
            if area > 10000:
                area_result[i, j] = np.nan  # Set the area as invalid for this pixel
                peak_x_result[i, j] = np.nan  # Set the corresponding peak time as invalid
                continue
            area_result[i, j] = area if area > 0 else np.nan  # Ensure non-negative area

        except RuntimeError as e:
            print(f"Pixel ({i}, {j}) fitting failed: {e}")
            continue

# Save the area results as GeoTIFF
with rasterio.open(
        os.path.join(tif_dir, tif_files[0])
) as src_template:  # Use the first TIFF file as the template
    profile = src_template.profile
    profile.update(dtype=rasterio.float32, count=1)

    with rasterio.open(r"H:\20250831密云水库\rrrr\Cumulative_flood _volume.tif", "w", **profile) as dst:
        dst.write(area_result.astype(np.float32), 1)

# Save the peak position results as GeoTIFF
with rasterio.open(
        os.path.join(tif_dir, tif_files[0])
) as src_template:  # Use the first TIFF file as the template
    profile = src_template.profile
    profile.update(dtype=rasterio.float32, count=1)

    with rasterio.open(r"H:\20250831密云水库\rrrr\Peak_flood_time.tif", "w", **profile) as dst:
        dst.write(peak_x_result.astype(np.float32), 1)

print("Processing completed!")
