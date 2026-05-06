import subprocess
import os

print("=== Generating Trips for Pessac ===")

cmd = [
    "python",
    os.path.join(os.getenv("SUMO_HOME"), "tools", "randomTrips.py"),
    "-n", "pessac.net.xml",
    "-o", "pessac.trips.xml",
    "--period", "6",           # har 6 second mein 1 gaadi
    "-e", "3600",              # simulation end time (sahi argument)
    "--fringe-factor", "3",
    "--min-distance", "200",
    "--max-distance", "2000",
    "--seed", "42"
]

try:
    subprocess.run(cmd, check=True, cwd=".")
    print("✅ Trips file successfully generated: pessac.trips.xml")
except Exception as e:
    print("❌ Error:", e)