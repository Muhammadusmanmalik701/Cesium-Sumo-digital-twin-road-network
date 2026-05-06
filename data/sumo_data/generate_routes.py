import subprocess

print("=== Generating Proper Routes ===")

cmd = [
    "duarouter",
    "-n", "pessac.net.xml",
    "-t", "pessac.trips.xml",
    "-o", "pessac.rou.xml",
    "--ignore-errors", "true",
    "--repair", "true",
    "--max-alternatives", "3"
]

try:
    subprocess.run(cmd, check=True)
    print("✅ Routes file successfully created: pessac.rou.xml")
except Exception as e:
    print("❌ Error in duarouter:", e)