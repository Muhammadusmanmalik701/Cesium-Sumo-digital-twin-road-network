import subprocess

print("=== Pessac Digital Twin - Running Simulation ===")

cmd = [
    "sumo",
    "-c", "pessac.sumocfg",
    "--no-step-log",
    "--duration-log.statistics",
    "--xml-validation", "never"
]

try:
    print("Simulation chal rahi hai... (thoda time lagega)")
    subprocess.run(cmd, check=True)
    print("\n✅ Simulation successfully complete ho gayi!")
    print("Output files: pessac_fcd.xml (vehicle positions)")
except Exception as e:
    print("Error:", e)