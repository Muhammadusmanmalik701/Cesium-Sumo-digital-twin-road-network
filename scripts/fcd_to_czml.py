import xml.etree.ElementTree as ET
import json
from datetime import datetime

print("=== SUMO FCD to Cesium CZML Converter ===")

fcd_file = "../sumo_data/pessac_fcd.xml"
czml_file = "../cesium_app/vehicles.czml"

try:
    tree = ET.parse(fcd_file)
    root = tree.getroot()

    czml = [
        {
            "id": "document",
            "name": "Pessac Traffic Digital Twin",
            "version": "1.0"
        }
    ]

    vehicle_data = {}

    for timestep in root.findall('timestep'):
        t = float(timestep.get('time'))
        for vehicle in timestep.findall('vehicle'):
            vid = vehicle.get('id')
            x = float(vehicle.get('x'))
            y = float(vehicle.get('y'))
            speed = float(vehicle.get('speed', 0))

            if vid not in vehicle_data:
                vehicle_data[vid] = []
            
            # Convert SUMO (x,y) to Longitude, Latitude (rough approx for Pessac)
            lon = -0.615 + (x / 100000)
            lat = 44.806 + (y / 100000)
            
            vehicle_data[vid].append({
                "time": t,
                "lon": lon,
                "lat": lat,
                "speed": speed
            })

    # Create CZML for each vehicle
    for vid, positions in vehicle_data.items():
        packet = {
            "id": f"vehicle_{vid}",
            "name": f"Vehicle {vid}",
            "availability": "2025-05-04T00:00:00Z/2025-05-04T01:00:00Z",
            "model": {
                "gltf": "https://assets.cesium.com/1/vehicle.glb",  # simple car model
                "scale": 8,
                "minimumPixelSize": 32
            },
            "path": {
                "material": {
                    "polylineGlow": {
                        "color": {"rgba": [255, 0, 0, 255]},
                        "glowPower": 0.1
                    }
                },
                "width": 2
            },
            "position": {
                "cartographicDegrees": []
            }
        }

        for pos in positions:
            packet["position"]["cartographicDegrees"].extend([
                pos["time"], pos["lon"], pos["lat"], 5
            ])

        czml.append(packet)

    with open(czml_file, "w") as f:
        json.dump(czml, f, indent=2)

    print(f"✅ CZML file created successfully! ({len(vehicle_data)} vehicles)")
    print("File saved at: cesium_app/vehicles.czml")

except Exception as e:
    print("Error:", e)