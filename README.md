# 🌊 A New Method for Flood Mapping Using SWOT Flood Volume Estimation (SWOT-FVE)

<p align="center">
  <img src="https://github.com/user-attachments/assets/2fe67ba3-07f9-4468-9292-845af734ced3" alt="SWOT-FVE Cover" width="600"/>
  <br>
  <em>A conceptual cover image: SWOT satellite observing flood events from space</em>
</p>

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









