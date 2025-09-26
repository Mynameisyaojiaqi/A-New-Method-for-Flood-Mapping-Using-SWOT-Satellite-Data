# 🌊 A New Method for Flood Mapping Using SWOT Flood Volume Estimation (SWOT-FVE)

## ✨ Overview
This repository provides codes, sample data, and visualization materials for two case studies of **flood monitoring and modeling** using **SWOT (Surface Water and Ocean Topography)** satellite **Water Surface Elevation (WSE)** observations.

## 🔑 Key Features
- **SWOT Data Preprocessing** → Read & filter `L2_HR_Raster (WSE)` and quality grids  
- **Noise Removal** → Fourier transform–based denoising for striping artifacts  
- **Flood Volume Estimation** → Estimate monthly flood volume using PDF/CDF methods  
- **Flood Modeling** → Integrate SWOT-derived WSE into hydrological models  
- **Visualization** → Generate GeoTIFF maps, time series plots, and flood risk figures  

---

## 📂 Repository Structure
```bash
SWOT-FVE/
│── data/                # Sample SWOT WSE data
│── src/                 # Preprocessing, modeling & visualization scripts
│── results/             # Case study outputs (GeoTIFFs, plots, stats)
│── figures/             # All figures used in README + papers
│── README.md            # Project documentation
```
## 📘 Case Studies
Case 1: Gangnan Reservoir (Hebei, China)
📄 Based on:
Yao et al. (2025), “3-D Flood Mapping from SWOT Observations during Extreme Rainfall”, International Journal of Digital Earth.
DOI: 10.1080/17538947.2025.2544916
🔹 Input

SWOT L2_HR_Raster WSE products

Sentinel-2 optical imagery

Land use change datasets

🔹 Output

WSE accuracy validation (compared with ICESat-2)

Spatiotemporal flood distribution maps

Flood volume estimation curves

🔹 Example Code
```bash
from src.preprocess import preprocess_wse
from src.flood_volume import estimate_volume

# Preprocess SWOT WSE data
wse_data = preprocess_wse("data/Gangnan_WSE.nc")

# Estimate flood volume
flood_volume = estimate_volume(wse_data, method="PDF")
```

🔹 Visualization
<p align="center"> <img src="figures/gangnan_overview.png" width="500"/> <br> <em>Fig.1. Overview of the Gangnan Reservoir study area</em> </p>

Case 2: Miyun Reservoir (Beijing, China)

📄 Based on (under review):
"SWOT-Based Water Surface Elevation Observations Improve Flood Modeling of the 25·7 Miyun Reservoir Basin Extreme Rainfall Event," submitted to Geophysical Research Letters (GRL)

🔹 Input

SWOT WSE observations

Hydrological model inputs (precipitation, DEM, flow data)

🔹 Output

SWOT-derived flood volume estimation

Peak arrival time detection across rivers and reservoir

Water surface elevation maps before/after rainstorm

🔹 Example Code
```bash
from src.model_integration import integrate_wse

# Integrate SWOT WSE into hydrological model
results = integrate_wse("data/Miyun_WSE.nc", model="GR4J")
```
🔹 Visualization
<p align="center"> <img src="figures/miyun_results.png" width="500"/> <br> <em>Fig.2. SWOT-derived flood volume & peak arrival time</em> </p>

⚙️ Requirements

Python 3.9+

Required libraries:
```bash
pip install -r requirements.txt
```
🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/yourname/SWOT-FVE.git
cd SWOT-FVE

# Run Gangnan case study
python src/run_gangnan.py

# Run Miyun case study
python src/run_miyun.py
```
📖 Citation

If you use this repository, please cite:
```bash
@article{yao2025flood,
  title={3-D Flood Mapping from SWOT Observations during Extreme Rainfall: A Case Study of Gangnan Reservoir},
  author={Yao, X. and others},
  journal={International Journal of Digital Earth},
  year={2025},
  doi={10.1080/17538947.2025.2544916}
}

```
🎨 Additional Notes
📌 Figures are centered and widths unified (500 px)

🖼️ Cover images can be added (AI-generated conceptual figures of “satellite-based flood mapping”)

🧩 Case studies structured as Input → Output → Code → Visualization
