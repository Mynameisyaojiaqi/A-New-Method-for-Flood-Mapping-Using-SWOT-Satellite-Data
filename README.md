📘 Case Studies
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
from src.preprocess import preprocess_wse
from src.flood_volume import estimate_volume

# Preprocess SWOT WSE data
wse_data = preprocess_wse("data/Gangnan_WSE.nc")

# Estimate flood volume
flood_volume = estimate_volume(wse_data, method="PDF")

🔹 Visualization
<p align="center"> <img src="figures/gangnan_overview.png" width="500"/> <br> <em>Fig.1. Overview of the Gangnan Reservoir study area</em> </p>
Case 2: Miyun Reservoir (Beijing, China)

📄 Based on (under review):
"SWOT-Based Water Surface Elevation Observations Improve Flood Modeling of the 25·7 Miyun Reservoir Basin Extreme Rainfall Event," submitted to GRL

🔹 Input

SWOT WSE observations

Hydrological model inputs (precipitation, DEM, flow data)

🔹 Output

SWOT-derived flood volume estimation

Peak arrival time detection across rivers and reservoir

Water surface elevation maps before/after rainstorm

🔹 Example Code
from src.model_integration import integrate_wse

# Integrate SWOT WSE into hydrological model
results = integrate_wse("data/Miyun_WSE.nc", model="GR4J")

🔹 Visualization
<p align="center"> <img src="figures/miyun_results.png" width="500"/> <br> <em>Fig.2. SWOT-derived flood volume & peak arrival time</em> </p>
⚙️ Requirements

Python 3.9+

Required libraries:

pip install -r requirements.txt

🚀 Quick Start
# Clone repository
git clone https://github.com/yourname/SWOT-FVE.git
cd SWOT-FVE

# Run Gangnan case study
python src/run_gangnan.py

# Run Miyun case study
python src/run_miyun.py

📖 Citation

If you use this repository, please cite:

@article{yao2025flood,
  title={3-D Flood Mapping from SWOT Observations during Extreme Rainfall: A Case Study of Gangnan Reservoir},
  author={Yao, X. and others},
  journal={International Journal of Digital Earth},
  year={2025},
  doi={10.1080/17538947.2025.2544916}
}

🎨 Additional Notes

📌 Figures are centered and widths unified (500 px)

🖼️ Cover images can be added (AI-generated conceptual figures of “satellite-based flood mapping”)

🧩 Case studies structured as Input → Output → Code → Visualization







