import osmnx as ox
import subprocess
import os

print("=== Making SUMO Network File ===")

# Pessac map download
place = "Pessac, France"
G = ox.graph_from_place(place, network_type="drive", simplify=False)

ox.save_graph_xml(G, filepath="pessac.osm")
print("✅ OSM file saved")

# Netconvert command
cmd = [
    "netconvert",
    "--osm-files", "pessac.osm",
    "--output-file", "pessac.net.xml",
    "--roundabouts.guess", "true",
    "--ramps.guess", "true",
    "--junctions.corner-detail", "5",
    "--tls.guess-signals", "true",
    "--geometry.remove", "true"
]

try:
    subprocess.run(cmd, check=True)
    print("✅ pessac.net.xml successfully created!")
except Exception as e:
    print("Error:", e)