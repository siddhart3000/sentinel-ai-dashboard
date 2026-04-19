<div align="center">

<!-- ANIMATED BANNER -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:060a10,50:00d4ff,100:a855f7&height=200&section=header&text=SENTINEL%20AI&fontSize=70&fontFamily=Orbitron&fontAlignY=38&desc=Intelligence%20Fusion%20Platform&descAlignY=58&descSize=20&fontColor=ffffff&animation=fadeIn" />

<!-- LIVE BADGES ROW -->
<p align="center">
  <img src="https://img.shields.io/badge/STATUS-DEPLOY%20READY-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=060a10" />
  <img src="https://img.shields.io/badge/VERSION-3.1.0-00d4ff?style=for-the-badge&logo=semver&logoColor=white&labelColor=060a10" />
  <img src="https://img.shields.io/badge/PYTHON-3.10%2B-a855f7?style=for-the-badge&logo=python&logoColor=white&labelColor=060a10" />
  <img src="https://img.shields.io/badge/STREAMLIT-1.35%2B-ef4444?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=060a10" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ASSIGNMENT-CYBERJOAR%20AI-00d4ff?style=flat-square&labelColor=0b1220" />
  <img src="https://img.shields.io/badge/REF-OC.41335.2026.59218-a855f7?style=flat-square&labelColor=0b1220" />
  <img src="https://img.shields.io/badge/DEADLINE-20%20APR%2017%3A00%20IST-ef4444?style=flat-square&labelColor=0b1220" />
</p>

<br/>

<!-- TYPING ANIMATION -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=3000&pause=800&color=00D4FF&center=true&vCenter=true&multiline=true&width=700&height=80&lines=LoRa+Telemetry+Reconstruction+%E2%80%A2+Gap+Fill+%E2%86%92+0ms+Downtime;Predictive+Traffic+Congestion+%E2%80%A2+15-Step+Forecasting;Velocity-Based+Prediction+%E2%80%A2+%CE%B1%3D0.72+Smoothing" alt="Typing SVG" />
</a>

<br/><br/>

</div>

---

## ⚡ What is SENTINEL AI?

**SENTINEL AI** is a real-time **Intelligence Fusion Platform** built for the CyberJoar AI assignment. It solves two critical operational problems through a unified, production-grade Streamlit dashboard:

> *When data is broken, incomplete, or delayed — SENTINEL reconstructs reality.*

<br/>

<table>
<tr>
<td width="50%">

### 📡 Module 01 — LoRa Telemetry Reconstruction
> **Problem 2 from the assignment**

When LoRa nodes transmit fragmented or lost packets across low-bandwidth tactical networks, traditional systems stutter or go blind. SENTINEL's reconstruction layer maintains **continuous situational awareness** — no manual intervention required.

**Core Algorithm:**
- Detects `NaN` gaps in incoming GPS stream
- Velocity-based dead-reckoning: `t̂ = t₋₁ + α(t₋₁ − t₋₂)`
- Exponential smoother `α = 0.72` for jitter suppression
- Visual distinction: `◆ Yellow` estimated vs `● Green` verified

</td>
<td width="50%">

### 🚦 Module 02 — Predictive Traffic Congestion
> **Problem 4 from the assignment**

Fuses a 6-point trailing moving average with global linear trend (polyfit deg=1) to project **15 steps ahead** with a ±1.65σ confidence band — classifying risk before congestion materialises.

**Core Algorithm:**
- Hybrid MA + polyfit forecasting engine
- ±1.65σ confidence band from recent residuals
- Congestion classification: `HIGH >70` · `MEDIUM 40–70` · `LOW <40`
- Anomaly spike injection for incident simulation

</td>
</tr>
</table>

---

## 🎯 Live Demo Metrics

<div align="center">

| Metric | Module 01 — LoRa | Module 02 — Traffic |
|--------|-----------------|---------------------|
| **Reconstruction Method** | Velocity prediction + α-smoothing | MA-anchor + polyfit trend |
| **Packet Loss Handled** | Up to 55% | — |
| **Forecast Horizon** | — | 15 steps |
| **Confidence Band** | — | ±1.65σ (~90% CI) |
| **Visual Continuity** | ✅ Estimated dots distinct | ✅ Uncertainty shading |
| **Real-time Playback** | ✅ 0.25× to 4× speed | ✅ Live zone alerts |
| **Avg Position Error** | ~70–80m at 40% loss | — |
| **Risk Classification** | — | HIGH / MEDIUM / LOW |

</div>

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

<br/>

```
SENTINEL AI STACK
├── streamlit          → UI framework + session state management
├── plotly             → Interactive charts with custom dark theme
├── numpy              → Signal processing, polyfit, NaN handling
├── pandas             → Dataframe rendering for packet/forecast logs
└── python random/time → Simulation engine + playback timing
```

---

## 🚀 Quick Start

### Prerequisites

```bash
python --version   # 3.10 or higher required
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/siddhart3000/sentinel-ai.git
cd sentinel-ai

# 2. Install dependencies
pip install streamlit plotly numpy pandas

# 3. Launch the dashboard
streamlit run app.py
```

### That's it. Open `http://localhost:8501` in your browser. 🎯

---

## 📁 Project Structure

```
sentinel-ai/
│
├── app.py                    ← Main application (single-file architecture)
│   │
│   ├── PLOT_BASE             ← Shared Plotly dark theme defaults
│   │
│   ├── Module 01: LoRa
│   │   ├── generate_gps_path()      ← Lissajous-style synthetic GPS near Delhi
│   │   ├── apply_packet_loss()      ← Random NaN injection (anchored endpoints)
│   │   ├── reconstruct()            ← O(n) velocity prediction + α-smoothing
│   │   ├── run_telemetry()          ← Orchestrates full simulation run
│   │   ├── build_telemetry_fig()    ← Static overview chart
│   │   └── build_playback_fig()     ← Per-frame animated playback chart
│   │
│   └── Module 02: Traffic
│       ├── generate_traffic()       ← Random walk + rush-hour harmonics
│       ├── forecast_traffic()       ← Hybrid MA + polyfit forecaster
│       ├── congestion_info()        ← Risk classifier (HIGH/MEDIUM/LOW)
│       ├── run_traffic()            ← Orchestrates full simulation run
│       └── build_traffic_fig()      ← Forecast chart with confidence band
│
└── README.md
```

---

## 🧠 Algorithm Deep Dive

<details>
<summary><b>📡 LoRa Reconstruction — How It Works</b></summary>

<br/>

**Step 1: Gap Detection**
```python
# NaN values in the stream = lost packets
lat_obs, lon_obs = apply_packet_loss(true_lat, true_lon, loss_rate, rng)
```

**Step 2: Velocity-Based Prediction**
```python
# Single O(n) forward pass — no nested loops
for i in range(2, len(lat_obs)):
    if np.isnan(lat_p[i]):
        vx = lat_p[i-1] - lat_p[i-2]   # velocity estimate
        vy = lon_p[i-1] - lon_p[i-2]
        lat_p[i] = lat_p[i-1] + alpha * vx   # alpha = 0.72
        lon_p[i] = lon_p[i-1] + alpha * vy
```

**Step 3: Visual Continuity**
```
◆ YELLOW DIAMONDS → Estimated (reconstructed) positions
● GREEN DOTS      → Verified (received) packets
··· GREY LINE     → Ground truth trajectory
```

**Error metric:** Average position error in metres = `mean(|lat_pred − lat_true|) × 111,320`

</details>

<details>
<summary><b>🚦 Traffic Forecasting — How It Works</b></summary>

<br/>

**Step 1: Series Generation**
```python
noise  = rng.normal(0, 2.8 * intensity, n).cumsum()
rush   = 12 * intensity * (np.sin(t * 3) + 0.5 * np.sin(t * 7))
series = np.clip(42 + intensity * 0.75 * noise + rush, 5, 98)
```

**Step 2: Hybrid Forecasting**
```python
slope, intercept = np.polyfit(t, series, 1)          # global trend
ma         = np.mean(series[-6:])                     # 6-point MA anchor
offset     = ma - np.polyval((slope, intercept), t[-1])  # bias correction
base       = np.polyval((slope, intercept), ft) + offset  # bias-corrected forecast
```

**Step 3: Confidence Band**
```python
resid_std = np.std(series[-6:] - np.polyval((slope, intercept), t[-6:]))
upper = base + 1.65 * resid_std   # ~90% CI upper
lower = base - 1.65 * resid_std   # ~90% CI lower
```

**Risk thresholds:**
| Value | Classification | Action |
|-------|---------------|--------|
| ≥ 70  | 🔴 HIGH       | ⚠ IMMEDIATE ACTION REQUIRED |
| 40–70 | 🟡 MEDIUM     | ◉ MONITOR CLOSELY |
| < 40  | 🟢 LOW        | ✓ NOMINAL FLOW |

</details>

---

## 🎨 UI Design Philosophy

SENTINEL AI uses a custom **cyber-intelligence dark theme** with:

- **Font stack:** `Orbitron` (brand/headings) + `JetBrains Mono` (data/labels) + `Inter` (body)
- **Primary accent:** `#00d4ff` — cyan for verified/live data
- **Secondary accent:** `#a855f7` — purple for system/version elements  
- **Alert color:** `#ef4444` — red for high congestion / errors
- **Background:** `#060a10` (deep space) → `#0b1220` (card surfaces)
- **Animations:** CSS shimmer on logo, pulse on live badge, gradient progress bars

---

## 👤 Candidate

<div align="center">

| | |
|---|---|
| **Name** | Siddharth Singh |
| **Degree** | B.Tech Computer Science Engineering |
| **University** | Lovely Professional University (LPU), Punjab |
| **Email** | [singhsiddharthgagha@gmail.com](mailto:singhsiddharthgagha@gmail.com) |
| **Phone** | +91 8948950988 |
| **GitHub** | [@siddhart3000](https://github.com/siddhart3000) |
| **LinkedIn** | [siddharth-singh-rajput](https://linkedin.com/in/siddharth-singh-rajput) |

</div>

---

## 📋 Assignment Reference

<div align="center">

| Field | Detail |
|-------|--------|
| **Organisation** | CyberJoar AI |
| **Reference Code** | `OC.41335.2026.59218` |
| **Submit To** | [sashrik@cyberjoar.com](mailto:sashrik@cyberjoar.com) |
| **Deadline** | 20 April 2026 · 17:00 IST |
| **Problems Solved** | Problem 2 (LoRa) + Problem 4 (Traffic) |

</div>

---

<div align="center">

<!-- FOOTER WAVE -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:a855f7,50:00d4ff,100:060a10&height=120&section=footer&animation=fadeIn" />

<br/>

**SENTINEL AI &nbsp;·&nbsp; SIDDHARTH SINGH &nbsp;·&nbsp; CYBERJOAR AI &nbsp;·&nbsp; OC.41335.2026.59218**

*Built with precision. Deployed with confidence.*

<br/>

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=siddhart3000.sentinel-ai&left_color=060a10&right_color=00d4ff&left_text=VISITORS)

</div>
