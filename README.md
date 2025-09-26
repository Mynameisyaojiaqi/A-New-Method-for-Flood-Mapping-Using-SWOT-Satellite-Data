🌊 A New Method for Flood Mapping Using SWOT Flood Volume Estimation (SWOT-FVE)
Introduction
This repository provides code, sample data, and visualization materials for two case studies of flood monitoring and modeling using SWOT (Surface Water and Ocean Topography) satellite water surface elevation (WSE) observations.

Key Features

SWOT Data Preprocessing: Read and filter L2_HR_Raster (WSE) and quality grids.

Noise Removal: Apply Fourier transform–based denoising for striping artifacts.

Flood Volume Estimation: Estimate monthly flood volume using probability distribution functions (PDF/CDF).

Flood Modeling: Integrate SWOT-derived WSE into hydrological models to improve simulation accuracy.

Visualization: Generate GeoTIFF maps, time series plots, and flood risk assessment figures.

Case Studies
1.Gangnan Reservoir (Hebei, China)
Based on the published paper:
Yao et al. (2025), "3-D Flood Mapping from SWOT Observations during Extreme Rainfall: A Case Study of Gangnan Reservoir," International Journal of Digital Earth.
DOI: 10.1080/17538947.2025.2544916

<img width="554" height="468" alt="image" src="https://github.com/user-attachments/assets/2fe67ba3-07f9-4468-9292-845af734ced3" />

Fig. 1. Overview of the Gangnan Reservoir area. (a) SWOT satellite mapping model. (b) Research area location. (c) Research area rainfall and average water level change. (d) Research area land use type change before and after disaster.

<img width="475" height="463" alt="image" src="https://github.com/user-attachments/assets/0777ee4f-cdb0-4b96-a460-54fa0b93c46e" />

Fig. 2. Water level height measurement accuracy verification results. ( a1 ) ICESat-2 verification data of Gangnan Reservoir area. ( a2–3 ) 100 m/250 m spatial resolution WSE within the range of Gangnan Reservoir. (b1–2) The error statistical results of the 100 m spatial resolution data. ( c1–2)  The 250 m spatial resolution data error statistics.

<img width="554" height="250" alt="image" src="https://github.com/user-attachments/assets/7923ea04-2d64-499a-a2ff-904e77fe9f4b" />

Fig. 3. Spatiotemporal variation of monthly flood and empty disasters in Gangnan Reservoir based on SWOT satellite products. (a) WSE distribution of Gangnan Reservoir before the flood events. (b) WSE distribution of Gangnan Reservoir after the flood events. (c) Cumulative flood distribution of Gangnan Reservoir in the flood events. (d) the distribution of the maximum flood peak arrival time node of Gangnan Reservoir in d flood event. (e) time series changes of flood water level height and submerged area in typical disaster-stricken areas.(f) Images of Sentinel-2 near area A before the torrential rain,(g) Represents a Sentinel-2 image during a rainstorm event,(h) Image of the reservoir during the flood discharge 

2.Miyun Reservoir (Beijing, China)
Based on the submitted paper:
"SWOT-Based Water Surface Elevation Observations Improve Flood Modeling of the 25·7 Miyun Reservoir Basin Extreme Rainfall Event," submitted to Geophysical Research Letters (GRL).（under review）

<img width="463" height="411" alt="image" src="https://github.com/user-attachments/assets/5e2dc5cd-9be1-416a-afb3-cd7019bc5251" />

Figure 4. SWOT-derived flood volume and peak timing in three representative regions. a. SWOT and mathematical model used to fit the conceptual schematic diagram of flood volume. b1-b3. Flood Volume for Baihe River, Miyun Reservoir, and Chaobai River. c1-c3. Peak Arrival Time for Baihe River, Miyun Reservoir, and Chaobai River(Days since June 27).

<img width="554" height="478" alt="image" src="https://github.com/user-attachments/assets/a8bf01ff-e419-4cfb-b5d0-6b343e678f13" />

Figure 5 Water surface elevation map before and after the rainstorm. a1-a3, the water surface elevation of Baihe River, Miyun Reservoir, and the Chaobai River before the heavy rainstorm. b1-b3, the water surface elevation of the same locations after the heavy rainstorm. c1-c3, water surface elevation Changes caused by the heavy rainstorm.











