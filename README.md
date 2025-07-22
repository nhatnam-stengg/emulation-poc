# 🧪 emulation-poc

Proof of concept: user emulation to generate realistic traffic and process data for cyber range.

## 📦 Project structure
```
emulation-poc/
├── desktop/pyautogui_demo.py
├── web/emulate.js
├── orchestrator.py
├── logs/
├── README.md
└── proposal.md
```

## 🌐 Web emulation (Node.js + Playwright)
```bash
cd web
npm install
node emulate.js
```

## 🖥 Desktop emulation (Python + pyautogui)
```bash
pip install -r requirements.txt
python desktop/pyautogui_demo.py
```

## 🔄 Orchestrator
```bash
python orchestrator.py
```

## 📊 Logs
- logs/web_emulation.log
- logs/desktop_emulation.log
