# Tech Spike: User Emulation Approach for Cyber-Ranged Platform

## Objective

As part of the red/green team effort, we aim to **emulate realistic user behavior and generate background traffic** on workstations. This helps mask MSEL procedures and makes them less detectable during monitoring or forensic analysis.

### Requirements

The solution must:

- **Easy to maintain** by our dev team (Node.js & Python background)
- **Fit into our current stack**: React frontend, Node/Express backend, MongoDB, Python3 for orchestration/infra
- **Integrate with Zabbix** for monitoring and reporting

---

## Available Tools & Options

### Web-based User Emulation
*Browser automation & web traffic generation*

| Tool | Description | Pros | Cons | Best For |
|------|-------------|------|------|----------|
| **Selenium** | Control real browsers (Chrome, Firefox, Edge, etc.) | • Realistic user behavior<br>• Real browsers<br>• Multi-language support | • Complex setup<br>• Slower execution | Teams familiar with Python, Java, C# |
| **Puppeteer** | Headless Chrome/Chromium automation | • Fast execution<br>• Modern API<br>• Node.js native | • Chrome only<br>• Limited browser support | Node.js teams |
| **Playwright** | Multi-browser automation (Chromium, Firefox, WebKit) | • Very powerful<br>• Multi-browser support<br>• Multi-tab capability | • New API to learn<br>• Larger footprint | Node.js & Python teams |
| **Cypress** | E2E testing framework | • Integrated test runner<br>• Time-travel debugging<br>• Snapshots | • Testing-focused<br>• Hard to run random scripts | Web testing scenarios |
| **PhantomJS** *(deprecated)* | Headless browser | • Lightweight | • No longer maintained<br>• Outdated | Legacy projects only |
| **Locust / k6** | Load testing tools | • Generate high traffic volumes<br>• Performance focused | • No real GUI interaction<br>• Limited user behavior | Traffic simulation without GUI |

### Desktop App User Emulation
*GUI automation for native applications*

| Tool | Description | Pros | Cons |
|------|-------------|------|------|
| **SikuliX** | Find and click based on image templates | • Very realistic behavior<br>• Works on any application | • Sensitive to resolution changes<br>• Requires image maintenance |
| **pyautogui** | Move mouse, type text, keyboard shortcuts | • Lightweight<br>• Python native<br>• Simple API | • Cannot "see" UI controls<br>• Basic functionality |
| **AutoHotKey** | Windows script automation | • Powerful scripting<br>• Lightweight<br>• Fast execution | • Windows only<br>• Custom syntax |
| **AutoIt** | Similar to AutoHotKey | • Deep Windows integration<br>• GUI spy tools | • Windows only<br>• Learning curve |
| **WinAppDriver / Winium** | Automate native Windows apps | • Can access UI controls<br>• Professional grade | • More complex setup<br>• Windows specific |

### Mobile User Emulation
*Mobile device automation*

| Tool | Description | Use Case |
|------|-------------|----------|
| **Appium** | Automate real devices or emulators | Cross-platform mobile automation |
| **UIAutomator (Android)** | Native Android automation | Android-specific automation |
| **Bluestacks + macros** | GUI-based macro scripting | Quick Android emulation setup |
| **Genymotion + adb** | Control Android emulators via adb | Professional Android testing |

---

## 🌐 Web Automation: Playwright vs Selenium

|                    | Playwright                                             | Selenium                                             |
| ------------------ | ----------------------------------------------------- | --------------------------------------------------- |
| Language           | Node.js, Python, C#                                   | Python, Java, C#, Node.js, etc.                     |
| Browsers           | Chromium, Firefox, WebKit                             | Chrome, Firefox, Edge, Safari                        |
| Speed & API        | Faster, modern async API                              | Slower, legacy API                                   |
| Multi-tab / context| Built-in                                              | More complex                                         |
| Fit with team      | Great for Node.js / JavaScript developers            | Better if team uses Java/other                       |

**Why Playwright?**  
- Native Node.js fits backend/frontend stack
- Supports multiple browsers → more realistic traffic
- Modern, concise API

---

## ▶ Example: Search "cyber security" on Wikipedia

### Playwright (Node.js)
```javascript
// web/emulate.js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://www.wikipedia.org');
  await page.fill('input[name=search]', 'cyber security');
  await page.press('input[name=search]', 'Enter');
  await browser.close();
})();
```

### Selenium (Python)
```python
# web/emulate_selenium.py
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
search = driver.find_element("name", "search")
search.send_keys("cyber security")
search.submit()
driver.quit()
```

---

## 🖥 Desktop Automation: pyautogui vs SikuliX

|             | pyautogui                                      | SikuliX                                       |
| ----------- | ---------------------------------------------- | --------------------------------------------- |
| How         | Type & move mouse via code                     | Find & click UI elements by image             |
| Language    | Native Python → team‑friendly                  | Python‑like (Jython) → needs Java runtime     |
| Pros        | Simple, lightweight, quick scripting           | Works if UI moves, doesn't rely on coordinates|
| Cons        | Needs stable UI, fixed positions/shortcuts     | Sensitive to screen res; needs image assets   |

---

## ▶ Example: Open Notepad, type, save as note.txt

### pyautogui (Python)
```python
# desktop/pyautogui_demo.py
import pyautogui, os, time

os.system("start notepad")
time.sleep(1)
pyautogui.typewrite("Hello cyber range!\n")
pyautogui.hotkey('ctrl', 's')
time.sleep(0.5)
pyautogui.typewrite("note.txt")
pyautogui.press('enter')
pyautogui.hotkey('alt', 'f4')
```

### SikuliX (Jython‑style Python)
```python
# notepad_sikulix.sikuli/script.py
openApp("notepad.exe")
wait(1)
type("Hello cyber range!\n")
type("s", Key.CTRL)
wait(0.5)
type("note.txt")
type(Key.ENTER)
type("f4", Key.ALT)
```

---

## Recommended Tech Stack

> **Optimized for Node.js & Python teams**

| Layer | Tool | Language | Purpose |
|-------|------|----------|---------|
| **Web Emulation** | Playwright | Node.js | Simulate browsing, clicking, scrolling, search inputs |
| **Desktop Emulation** | pyautogui | Python | Open apps (Notepad, PowerPoint), type text, save files |
| **Orchestration** | Custom Python Script | Python | Schedule & randomize script execution, manage logs |
| **Monitoring** | Zabbix Agent + UserParameter | Shell/Python | Monitor processes, log content, generate alerts & graphs |

### Why These Tools?

| Tool | Reasoning |
|------|-----------|
| **Playwright** | • Native JavaScript/Node.js → fits team skillset<br>• Multi-browser support → more natural traffic<br>• Can run headless or visible<br>• Modern, well-maintained API |
| **pyautogui** | • Simple Python API → quick to extend<br>• Generates realistic process & filesystem activity<br>• Lightweight and reliable |
| **Python Orchestrator** | • Team expertise in Python<br>• Easy to write scheduling logic<br>• Great for randomization and logging<br>• Already in infrastructure |
| **Zabbix Integration** | • Custom metrics via UserParameter<br>• Excellent monitoring capabilities |

---

## Implementation Approach

### 1. Web User Emulation

**Technology:** Playwright (Node.js)

**Capabilities:**
- Automate real browsers (Chromium, Firefox, WebKit)
- Simulate human-like behavior with randomization
- Navigate to random websites
- Perform random searches
- Random wait times, scrolling, and link clicks
- Log all actions to `logs/web_emulation.log`

**Benefits:**
- Native JavaScript/Node.js integration
- Multi-browser support for realistic traffic patterns
- Can run headless or with visible browser windows
- Modern, performant API

### 2. Desktop App Emulation

**Technology:** pyautogui (Python)

**Capabilities:**
- Open applications (Notepad, PowerPoint, Calculator, etc.)
- Type realistic content with random phrases
- Save files to disk with meaningful names
- Simulate typical user workflows
- Log execution to `logs/desktop_emulation.log`

**Benefits:**
- Simple Python API that team can easily extend
- Generates realistic process data and filesystem changes
- Lightweight and reliable for basic automation needs

### 3. Orchestration & Scheduling

**Technology:** Python Orchestrator Script

**Features:**
- Randomly selects which emulation script to run
- Randomizes intervals between executions (5-15 minutes)
- Aggregates logs from all emulation scripts
- Continuous operation with error handling

**Example Logic:**
```python
import subprocess, random, time, logging
[test](https://github.com/nhatnam-stengg/emulation-poc)
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

scripts = [
    ("node web/emulate.js", "Web emulation"),
    ("python3 desktop/pyautogui_demo.py", "Desktop emulation")
]

def run_orchestrator():
    while True:
        try:
            # Randomly select a script
            script, description = random.choice(scripts)
            logging.info(f"Running: {description}")
            
            # Execute the script
            result = subprocess.run(script, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                logging.info(f"{description} completed successfully")
            else:
                logging.error(f"{description} failed: {result.stderr}")
            
            # Random wait between 5-15 minutes
            wait_time = random.randint(300, 900)
            logging.info(f"Sleeping for {wait_time} seconds")
            time.sleep(wait_time)
            
        except Exception as e:
            logging.error(f"Orchestrator error: {e}")
            time.sleep(60)  # Wait 1 minute before retrying

if __name__ == "__main__":
    run_orchestrator()
```

### 4. Monitoring Integration

**Zabbix Configuration:**

1. **Custom UserParameter** in `zabbix_agentd.conf`:
   ```bash
   UserParameter=emulation.web.status,grep -c "Web emulation" /var/log/emulation/web_emulation.log
   UserParameter=emulation.desktop.status,grep -c "Desktop emulation" /var/log/emulation/desktop_emulation.log
   UserParameter=emulation.last.run,stat -c %Y /var/log/emulation/orchestrator.log
   ```

2. **Monitor Key Metrics:**
   - Script execution frequency
   - Success/failure rates
   - Last execution timestamp
   - Log file sizes
   - Process resource usage

---

## Project Structure

```
user-emulation/
├── web/
│   ├── emulate.js          # Playwright web automation
│   ├── package.json        # Node.js dependencies
│   └── config.json         # Web emulation settings
├── desktop/
│   ├── pyautogui_demo.py   # Desktop automation script
│   └── requirements.txt    # Python dependencies
├── orchestration/
│   ├── orchestrator.py     # Main scheduling script
│   └── config.yaml         # Orchestration settings
├── logs/
│   ├── web_emulation.log
│   ├── desktop_emulation.log
│   └── orchestrator.log
├── monitoring/
│   ├── zabbix_template.xml # Zabbix monitoring template
│   └── custom_checks.sh    # Additional monitoring scripts
└── README.md               # Setup and usage instructions
```

---

## Next Steps

1. **Setup Development Environment**
   - Install Node.js and Python dependencies
   - Configure Playwright browsers
   - Test basic automation scripts

2. **Develop Core Scripts**
   - Create Playwright web emulation script
   - Develop pyautogui desktop automation
   - Build Python orchestrator

3. **Implement Monitoring**
   - Configure Zabbix UserParameters
   - Create monitoring dashboards
   - Set up alerting rules

4. **Testing & Validation**
   - Test in controlled environment
   - Validate traffic patterns
   - Ensure MSEL procedure masking

5. **Production Deployment**
   - Deploy to target workstations
   - Monitor execution and adjust parameters
   - Document operational procedures
