import subprocess, random, time

scripts = [
    ("node web/emulate.js", "Web emulation"),
    ("python desktop/pyautogui_demo.py", "Desktop emulation")
]

print("=== User emulation orchestrator started ===")

while True:
    script, desc = random.choice(scripts)
    print(f"\n[+] Running: {desc}")
    subprocess.call(script, shell=True)
    wait = random.randint(300, 900)  # 5–15 minutes
    print(f"[-] Sleeping for {wait} seconds...\n")
    time.sleep(wait)
