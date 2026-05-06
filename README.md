<img width="1363" height="688" alt="image" src="https://github.com/user-attachments/assets/20b638a6-682c-407e-a2fc-750c84652181" /># 🚗 Cesium + SUMO Digital Twin Road Network

A **Real-Time 3D Traffic Digital Twin** built using **Cesium.js** and **SUMO (Simulation of Urban Mobility)** to simulate and visualize urban traffic on real-world road networks.


### 🔗 Live Demo
[→ Open Live Demo](https://muhammadusmanmalik701.github.io/Cesium-Sumo-digital-twin-road-network/)

---

## 🎯 Project Overview

This project creates a **3D Digital Twin** of an urban area (Bordeaux, France) where real geographic data is combined with realistic traffic simulation. It allows users to visualize how vehicles move through the city in a 3D interactive environment.

### Key Integrations:
- **Cesium.js** → High-performance 3D globe and visualization
- **SUMO** → Realistic traffic simulation engine
- **OpenStreetMap** → Real-world road network data
- **CZML** → Dynamic vehicle animation

---

## ✨ Key Features

- 🌍 Interactive 3D Globe with real terrain and 3D buildings
- 🛣️ Dynamic road network rendering (Overpass API)
- 🚗 Realistic vehicle movement using SUMO simulation
- 🎛️ Road layer filtering (Major, Primary, Secondary, Local, Tram, Rail)
- 📊 Live Dashboard (Traffic count, Speed, Flow, Weather)
- 🔴 Congestion visualization through road coloring
- 📍 Click on vehicles for details

---

## 🛠 Technology Stack

| Technology       | Purpose                          |
|------------------|----------------------------------|
| Cesium.js        | 3D Visualization & Globe         |
| SUMO             | Traffic Simulation               |
| Python           | FCD to CZML conversion           |
| OpenStreetMap    | Real map data                    |
| Overpass API     | Dynamic road extraction          |
| Chart.js         | Analytics Dashboard              |
| GitHub Pages     | Hosting                          |

---

## 📂 Project Structure

Cesium-Sumo-digital-twin-road-network/
├── index.html
├── README.md
├── .gitignore
└── sumo_files/
    ├── map.net.xml
    ├── map.osm
    ├── routes.rou.xml
    ├── sim.sumocfg
    ├── trips.trips.xml
    ├── vehicles.czml
    └── fcd_to_czml.py

🚀 How to Run Locally

Clone the repository
Go to project folder
Run local server:

python -m http.server 8000

Open browser and go to: http://localhost:8000
Select an area → Click "Load SUMO Vehicles"


🔮 Future Enhancements

Real-time traffic light simulation
AI-based traffic optimization
WebSocket-based live updates
Lane-level behavior modeling
Multi-city support
Emission and environmental analysis


👨‍💻 Author
Muhammad Usman Malik

⭐ Support & Contribution

If you find this project useful:

⭐ Star the repository
🔁 Share with others
🤝 Contribute improvements
