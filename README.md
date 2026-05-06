# Cesium + SUMO Digital Twin Road Network

**A Real-time 3D Road Network Digital Twin** using **Cesium.js** and **SUMO (Simulation of Urban MObility)**.

[![Project Preview](https://muhammadusmanmalik701.github.io/Cesium-Sumo-digital-twin-road-network/)]

---

## 🚦 Project Overview

Yeh project ek **complete 3D Digital Twin** hai jisme real-world road network ko 3D mein visualize kiya jata hai aur SUMO simulation ke through **live moving traffic** dekha ja sakta hai.

**Goal**: Real city traffic ko simulate karke predict karna aur control karna (future mein AI-based traffic management).

---

## ✨ Features

- **3D Interactive Visualization** using Cesium.js
- **Real Terrain + 3D Buildings** (OSM data)
- **Real SUMO Road Network** (Pessac, France - expandable)
- **Moving Vehicles Animation** (CZML format)
- **SUMO Integration** for realistic traffic simulation
- **Python Scripts** for data conversion (SUMO → Cesium)
- **GitHub Pages Ready** (Live Demo)

---

## 🛠 Tech Stack

| Technology       | Purpose                          |
|------------------|----------------------------------|
| **Cesium.js**    | 3D Globe & Visualization        |
| **SUMO**         | Traffic Simulation Engine       |
| **Python**       | Data Processing & CZML Generation |
| **OpenStreetMap**| Base Map & Building Data        |
| **GitHub Pages** | Live Hosting                    |

---

## 📁 Project Structure

```bash
Cesium-Sumo-digital-twin-road-network/
├── public/
│   ├── index.html          # Main 3D Viewer
│   └── vehicles.czml       # Moving vehicles data
├── data/
│   └── sumo_data/
│       ├── pessac.osm
│       ├── pessac.net.xml
│       ├── pessac.sumocfg
│       └── *.py            # SUMO scripts
├── scripts/
│   ├── fcd_to_czml.py      # Convert SUMO output to Cesium
│   ├── generate_trips.py
│   └── run_simulation.py
├── README.md
└── .gitignore
