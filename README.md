# AI-Powered Microclimate Farming System (Sustainable Agriculture)
Organized **backend + frontend** you can host from the command line.

## 🧱 Tech
- **Backend:** FastAPI, SQLite (no external DB), simple hybrid AI (rules + lightweight regression)
- **Frontend:** Plain HTML/CSS/JS (fetches backend), no build tools, served by FastAPI as static files

## 🚀 Quick Start (Windows CMD / macOS / Linux)
### 1) Create venv & install deps
```bash
cd server
python -m venv .venv
# Windows CMD
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run the server (serves API + frontend)
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
Open: http://localhost:8000  (frontend)
API root: http://localhost:8000/docs

### 3) (Optional) Point your ESP32 nodes
Set `SERVER_BASE` in firmware to `http://<your-ip>:8000` and post to `/ingest`.

## 📂 Structure
```
agri_microclimate/
├─ server/
│  ├─ app.py            # FastAPI + static hosting
│  ├─ model.py          # Hybrid controller (rules + regression)
│  ├─ requirements.txt  # deps
│  ├─ config.yaml       # thresholds, crop profile, quiet hours
│  ├─ .env.example      # env defaults
│  └─ static/           # Frontend (no build step)
│     ├─ index.html
│     ├─ styles.css
│     └─ app.js
├─ README.md
└─ LICENSE
```

## 🔌 Useful API Endpoints
- `POST /ingest` — ingest sensor batch
- `GET  /control-state` — latest control decision
- `GET  /dashboard-data?limit=300` — recent series for charts/table
- `POST /override` — manual override (irrigation/mist/light)
- `GET  /config` and `POST /config` — read/update config on the fly

## 🧪 Simulating Data (no hardware)
Use the browser "Simulate" button on the frontend, or POST JSON to `/ingest`:
```bash
curl -X POST http://localhost:8000/ingest -H "Content-Type: application/json" -d '{"readings":[{"soil_raw":640,"soil_pct":38.0,"temp_c":33.2,"humidity":48.0,"light_lux":18000}]}'
```

## 🔐 Notes
- CORS is open for dev. Tighten for production in `.env` or code.
- SQLite DB auto-creates at runtime in the server folder.
- This is a clean starter; extend with MQTT, auth, multi-node support, charts, etc.
