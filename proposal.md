# 🧪 Tech Spike: User Emulation Approach for Close-Ranged Platform

## 🎯 Objective
As part of the red/green team effort, we aim to **emulate realistic user behavior and generate background traffic** on workstations.
This helps mask MSEL procedures and makes them less detectable during monitoring or forensic analysis.

## 🛠 Recommended Approach Overview
| Layer | Tool | Language | Purpose |
|--|--|--|--|
| Web user emulation | Playwright | Node.js | Simulate browsing, clicking, scrolling, search inputs |
| Desktop app emulation | pyautogui | Python | Open apps (e.g., Notepad, PowerPoint), type text, save files |
| Orchestration | Python script | Python | Schedule & randomize script execution, manage logs |
| Monitoring | Zabbix Agent + custom UserParameter | – | Monitor process, log content, generate alerts & graphs |
