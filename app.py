"""
SENTINEL AI — Intelligence Fusion Platform  v3.1
CyberJoar Assignment · Problem 2: LoRa Telemetry · Problem 4: Traffic Prediction
"""

from __future__ import annotations

import random
import time
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ── Version ────────────────────────────────────────────────────────────────────
__version__ = "3.1.0"

# ══════════════════════════════════════════════
# PAGE CONFIG  (must be first Streamlit call)
# ══════════════════════════════════════════════
st.set_page_config(
    page_title="SENTINEL AI — Intelligence Fusion",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ══════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════
def inject_css() -> None:
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, .stApp { background:#060a10 !important; color:#c9d6e3; font-family:'Inter',sans-serif; }
    [data-testid="stSidebar"] { background:linear-gradient(180deg,#060a10 0%,#0b1220 100%) !important; border-right:1px solid rgba(0,212,255,0.18); }
    [data-testid="stSidebar"] * { color:#c9d6e3 !important; }
    [data-testid="stHeader"]  { background:rgba(6,10,16,0.95) !important; }

    /* ── Brand ── */
    .sentinel-logo {
        font-family:'Orbitron',monospace; font-size:2.8rem; font-weight:900;
        letter-spacing:0.14em; text-transform:uppercase; margin:0; line-height:1.1;
        background:linear-gradient(135deg,#00d4ff 0%,#a855f7 50%,#00d4ff 100%);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
        background-size:200%; animation:shimmer 5s linear infinite;
    }
    @keyframes shimmer { 0%{background-position:0% center} 100%{background-position:200% center} }
    .sentinel-sub {
        font-family:'JetBrains Mono',monospace; font-size:0.68rem;
        letter-spacing:0.22em; color:#00d4ff; opacity:0.55; margin-top:6px;
        text-transform:uppercase;
    }
    .sentinel-tagline {
        font-size:0.88rem; color:#5a7a9a; margin-top:6px;
        font-weight:300; letter-spacing:0.02em;
    }

    /* ── Live badge ── */
    .badge-live {
        display:inline-flex; align-items:center; gap:7px;
        background:rgba(0,212,255,0.07); border:1px solid rgba(0,212,255,0.28);
        border-radius:20px; padding:5px 15px;
        font-family:'JetBrains Mono',monospace; font-size:0.7rem; color:#00d4ff; letter-spacing:0.12em;
    }
    .badge-dot {
        width:7px; height:7px; background:#00d4ff; border-radius:50%;
        display:inline-block; animation:pulse 1.6s ease-in-out infinite;
    }
    @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.3;transform:scale(0.85)} }

    /* ── Version pill ── */
    .version-pill {
        display:inline-flex; align-items:center;
        background:rgba(168,85,247,0.08); border:1px solid rgba(168,85,247,0.28);
        border-radius:12px; padding:3px 11px;
        font-family:'JetBrains Mono',monospace; font-size:0.62rem;
        color:#a855f7; letter-spacing:0.1em;
    }

    /* ── Metric cards ── */
    div[data-testid="stMetric"] { background:#0b1220 !important; border:1px solid rgba(0,212,255,0.16) !important; border-radius:10px !important; padding:14px 18px !important; }
    div[data-testid="stMetric"] label { color:#5a7a9a !important; font-size:0.78rem !important; letter-spacing:0.04em !important; }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] { color:#00d4ff !important; font-family:'Orbitron',monospace !important; font-size:1.5rem !important; }

    /* ── Info card ── */
    .info-card {
        background:#0b1220; border:1px solid rgba(0,212,255,0.13);
        border-left:3px solid #00d4ff; border-radius:0 8px 8px 0;
        padding:13px 18px; margin-bottom:18px; font-size:0.87rem; line-height:1.75; color:#7a96b0;
    }
    .info-card b    { color:#00d4ff; font-weight:600; }
    .info-card code {
        background:rgba(168,85,247,0.15); color:#c084fc; padding:2px 7px;
        border-radius:4px; font-family:'JetBrains Mono',monospace; font-size:0.8rem;
    }

    /* ── Labels / dividers ── */
    .section-label {
        font-family:'JetBrains Mono',monospace; font-size:0.68rem;
        letter-spacing:0.24em; color:#00d4ff; opacity:0.55;
        text-transform:uppercase; margin-bottom:8px;
    }
    .cyber-divider {
        height:1px;
        background:linear-gradient(90deg,transparent,rgba(0,212,255,0.35),transparent);
        margin:22px 0;
    }

    /* ── Buttons ── */
    .stButton > button {
        background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(168,85,247,0.1)) !important;
        border:1px solid rgba(0,212,255,0.45) !important; color:#00d4ff !important;
        font-family:'Orbitron',monospace !important; font-size:0.75rem !important;
        letter-spacing:0.12em !important; border-radius:6px !important;
        padding:10px 26px !important; transition:all 0.2s ease !important; width:100%;
    }
    .stButton > button:hover {
        background:linear-gradient(135deg,rgba(0,212,255,0.2),rgba(168,85,247,0.2)) !important;
        box-shadow:0 0 22px rgba(0,212,255,0.22) !important; border-color:#00d4ff !important;
    }

    /* ── Empty state ── */
    .empty-state {
        text-align:center; padding:64px 20px; color:#2a4060;
        border:1px dashed rgba(0,212,255,0.12); border-radius:10px; margin-top:18px;
        font-family:'JetBrains Mono',monospace; font-size:0.82rem; letter-spacing:0.1em;
    }

    /* ── Error card ── */
    .error-card {
        background:rgba(239,68,68,0.07); border:1px solid rgba(239,68,68,0.35);
        border-left:3px solid #ef4444; border-radius:0 8px 8px 0;
        padding:14px 18px; margin:12px 0;
        font-family:'JetBrains Mono',monospace; font-size:0.82rem; color:#fca5a5;
        line-height:1.8;
    }

    /* ── Footer ── */
    .footer {
        text-align:center; padding:22px 0 6px; margin-top:28px;
        border-top:1px solid rgba(0,212,255,0.09);
        font-size:0.7rem; color:#2a4060;
        font-family:'JetBrains Mono',monospace; letter-spacing:0.1em;
    }

    /* ── Misc ── */
    ::-webkit-scrollbar       { width:4px; }
    ::-webkit-scrollbar-track { background:#060a10; }
    ::-webkit-scrollbar-thumb { background:rgba(0,212,255,0.25); border-radius:2px; }
    .stSlider > div           { color:#5a7a9a; }
    div[data-testid="stToggle"] label { color:#8aa4be !important; }
    </style>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════
def init_state() -> None:
    defaults = {
        "tel_result":    None,
        "traf_result":   None,
        "stop_playback": False,   # flag to interrupt playback gracefully
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def _seed() -> int:
    """Unbiased random seed — simpler than uuid modulo approach."""
    return random.randint(0, 2**31 - 1)


# ══════════════════════════════════════════════
# PLOTLY LAYOUT DEFAULTS
# ══════════════════════════════════════════════
PLOT_BASE = dict(
    paper_bgcolor="#060a10",
    plot_bgcolor="#0b1220",
    font=dict(color="#8aa4be", family="JetBrains Mono", size=10),
    margin=dict(l=58, r=28, t=52, b=48),
    hovermode="closest",
)
XAXIS_BASE = dict(gridcolor="rgba(0,212,255,0.07)", zeroline=False, tickfont=dict(size=9))
YAXIS_BASE = dict(gridcolor="rgba(124,58,237,0.07)", zeroline=False, tickfont=dict(size=9))


# ══════════════════════════════════════════════
# HEADER — FIX: cleaner subtitle, version + DEMO READY badge
# ══════════════════════════════════════════════
def render_header() -> None:
    col_logo, col_right = st.columns([5, 2])
    with col_logo:
        st.markdown("""
        <p class="sentinel-logo">SENTINEL AI</p>
        <p class="sentinel-sub">Intelligence Fusion Platform</p>
        <p class="sentinel-tagline">
            LoRa telemetry reconstruction &amp; predictive traffic congestion modeling
        </p>
        """, unsafe_allow_html=True)
    with col_right:
        st.markdown(f"""
        <div style="display:flex;flex-direction:column;align-items:flex-end;
             gap:10px;padding-top:14px;">
            <span class="badge-live"><span class="badge-dot"></span>LIVE SIM</span>
            <span class="version-pill">v{__version__} &nbsp;·&nbsp; DEMO READY</span>
        </div>""", unsafe_allow_html=True)
    st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# SIDEBAR — FIX: all contact links clickable; DEPLOY READY badge added
# ══════════════════════════════════════════════
def render_sidebar() -> str:
    with st.sidebar:
        # Platform logo + version + deploy-ready pill
        st.markdown(f"""
        <div style="padding:6px 0 16px;">
            <p style="font-family:'Orbitron',monospace;font-size:1.05rem;font-weight:700;
               color:#00d4ff!important;letter-spacing:0.18em;margin:0 0 2px;">SENTINEL</p>
            <p style="font-family:'JetBrains Mono',monospace;font-size:0.6rem;
               color:#2a4060!important;letter-spacing:0.22em;margin:0 0 8px;">
               AI PLATFORM v{__version__}</p>
            <span style="display:inline-block;background:rgba(34,197,94,0.1);
               border:1px solid rgba(34,197,94,0.35);border-radius:10px;
               padding:2px 10px;font-family:'JetBrains Mono',monospace;
               font-size:0.6rem;color:#22c55e;letter-spacing:0.1em;">✓ DEPLOY READY</span>
        </div>""", unsafe_allow_html=True)

        # ── Candidate card — all links are real anchors ──
        st.markdown("""
        <div style="background:#0b1220;border:1px solid rgba(0,212,255,0.18);
             border-radius:10px;padding:14px 16px;margin-bottom:16px;">
            <p style="font-family:'Orbitron',monospace;font-size:0.85rem;font-weight:700;
               color:#00d4ff!important;letter-spacing:0.1em;margin:0 0 2px;">SIDDHARTH SINGH</p>
            <p style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;
               color:#a855f7!important;letter-spacing:0.08em;margin:0 0 10px;">
               B.Tech CSE · LPU Punjab</p>
            <div style="border-top:1px solid rgba(0,212,255,0.08);padding-top:10px;
                 font-family:'JetBrains Mono',monospace;font-size:0.62rem;
                 color:#5a7a9a!important;line-height:2.2;">
                📧 <a href="mailto:singhsiddharthgagha@gmail.com"
                   style="color:#5a7a9a;text-decoration:none;">
                   singhsiddharthgagha@gmail.com</a><br>
                📱 +91 8948950988<br>
                🐙 <a href="https://github.com/siddhart3000" target="_blank"
                   style="color:#00d4ff;text-decoration:none;">
                   github.com/siddhart3000</a><br>
                🔗 <a href="https://linkedin.com/in/siddharth-singh-rajput" target="_blank"
                   style="color:#00d4ff;text-decoration:none;">
                   linkedin.com/in/siddharth-singh-rajput</a>
            </div>
        </div>""", unsafe_allow_html=True)

        # Navigation
        st.markdown('<p class="section-label">Mission Modules</p>', unsafe_allow_html=True)
        page = st.radio("", [
            "📡  LoRa Telemetry Reconstruction",
            "🚦  Traffic Congestion Modeling",
        ], label_visibility="collapsed")

        st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

        # Assignment info
        st.markdown("""
        <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;
             color:#2a4060!important;line-height:2.2;">
            ASSIGNMENT · CYBERJOAR AI<br>
            OC.41335.2026.59218<br>
            SUBMIT · <a href="mailto:sashrik@cyberjoar.com"
               style="color:#2a4060;text-decoration:none;">sashrik@cyberjoar.com</a><br>
            DEADLINE · 20 APR 17:00 IST
        </div>""", unsafe_allow_html=True)

    return page


# ══════════════════════════════════════════════════════════════════
# ── MODULE 01: LoRa TELEMETRY RECONSTRUCTION ──
# ══════════════════════════════════════════════════════════════════

def generate_gps_path(n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Synthetic multi-harmonic GPS trajectory (lissajous-style) near Delhi."""
    t = np.linspace(0, 5 * np.pi, n)
    lat = (28.6139
           + 0.010 * np.sin(t * 1.3)
           + 0.004 * np.sin(t * 3.7)
           + 0.002 * np.cos(t * 5.1))
    lon = (77.2090
           + 0.015 * np.cos(t)
           + 0.005 * np.cos(t * 2.9)
           + 0.002 * np.sin(t * 4.3))
    lat += rng.normal(0, 0.00025, n)
    lon += rng.normal(0, 0.00025, n)
    return lat.astype(np.float64), lon.astype(np.float64)


def apply_packet_loss(
    lat: np.ndarray, lon: np.ndarray,
    loss_rate: float, rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    """Drop packets randomly (→ NaN). Anchors first two and last always valid."""
    received = rng.random(len(lat)) >= loss_rate
    received[0] = received[1] = received[-1] = True
    return np.where(received, lat, np.nan), np.where(received, lon, np.nan)


def reconstruct(
    lat_obs: np.ndarray, lon_obs: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Velocity-based predictive reconstruction with exponential smoothing.

    Single O(n) forward pass replaces the original O(n²) double-loop.
    Indices 0 and 1 are always anchored valid, so every downstream gap
    is reachable on the very first sweep.

    Formula:
        lat̂[i] = lat[i-1] + α · (lat[i-1] − lat[i-2])   α = 0.72
    Blends dead-reckoning extrapolation with carry-forward to damp jitter
    over consecutive packet-loss runs.
    """
    lat_p = lat_obs.copy()
    lon_p = lon_obs.copy()
    alpha = 0.72

    for i in range(2, len(lat_obs)):
        if np.isnan(lat_p[i]) and np.isfinite(lat_p[i - 1]) and np.isfinite(lat_p[i - 2]):
            vx = lat_p[i - 1] - lat_p[i - 2]
            vy = lon_p[i - 1] - lon_p[i - 2]
            lat_p[i] = lat_p[i - 1] + alpha * vx
            lon_p[i] = lon_p[i - 1] + alpha * vy

    return lat_p, lon_p, np.isnan(lat_obs)


def run_telemetry(n_pts: int, loss_rate: float, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    true_lat, true_lon       = generate_gps_path(n_pts, rng)
    lat_obs, lon_obs         = apply_packet_loss(true_lat, true_lon, loss_rate, rng)
    lat_pred, lon_pred, missing = reconstruct(lat_obs, lon_obs)

    n_lost = int(missing.sum())
    n_rec  = int(np.sum(missing & np.isfinite(lat_pred)))
    errors = np.abs(lat_pred[missing] - true_lat[missing])
    avg_m  = float(np.mean(errors) * 111_320) if n_rec > 0 else 0.0

    return dict(
        true_lat=true_lat, true_lon=true_lon,
        lat_obs=lat_obs,   lon_obs=lon_obs,
        lat_pred=lat_pred, lon_pred=lon_pred,
        missing=missing,   n_pts=n_pts,
        n_lost=n_lost,     n_rec=n_rec,
        loss_pct=100.0 * n_lost / n_pts,
        avg_m=avg_m,
    )


def build_telemetry_fig(data: dict, show_gt: bool) -> go.Figure:
    ok        = ~data["missing"] & np.isfinite(data["lat_obs"])
    pred_only =  data["missing"] & np.isfinite(data["lat_pred"])
    fig = go.Figure()

    if show_gt:
        fig.add_trace(go.Scatter(
            x=data["true_lon"], y=data["true_lat"], mode="lines",
            name="Ground Truth",
            line=dict(color="rgba(90,90,110,0.45)", width=1, dash="dot"),
            hoverinfo="skip",
        ))
    fig.add_trace(go.Scatter(
        x=data["lon_obs"], y=data["lat_obs"], mode="lines",
        name="Verified Path",
        line=dict(color="#22c55e", width=2.5),
        hovertemplate="<b>✅ Verified</b><br>Lat %{y:.6f}<br>Lon %{x:.6f}<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=data["lon_obs"][ok], y=data["lat_obs"][ok], mode="markers",
        name="Verified Packets",
        marker=dict(size=5, color="#22c55e", opacity=0.9),
        hovertemplate="<b>✅ Verified</b><br>Lat %{y:.6f}<br>Lon %{x:.6f}<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=data["lon_pred"], y=data["lat_pred"], mode="lines",
        name="Reconstructed Path",
        line=dict(color="rgba(250,204,21,0.55)", width=2, dash="dash"),
        hoverinfo="skip",
    ))
    if pred_only.any():
        fig.add_trace(go.Scatter(
            x=data["lon_pred"][pred_only], y=data["lat_pred"][pred_only],
            mode="markers", name="🟡 Estimated (Gap Fill)",
            marker=dict(size=10, color="rgba(250,204,21,0.88)", symbol="diamond",
                        line=dict(width=1.5, color="#facc15")),
            hovertemplate="<b>🟡 Estimated</b><br>Lat %{y:.6f}<br>Lon %{x:.6f}<extra></extra>",
        ))
    fig.update_layout(
        **PLOT_BASE, height=520,
        xaxis=dict(**XAXIS_BASE, title="Longitude (°)"),
        yaxis=dict(**YAXIS_BASE, title="Latitude (°)"),
        legend=dict(orientation="h", y=1.07, x=0, xanchor="left",
                    bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
        title=dict(
            text="GPS Asset Path  ·  🟢 Verified  ·  🟡◆ Reconstructed  ·  ···  Ground Truth",
            font=dict(color="#00d4ff", size=12, family="JetBrains Mono"),
        ),
    )
    return fig


def build_playback_fig(data: dict, end_idx: int) -> go.Figure:
    """
    Incremental playback frame up to packet `end_idx`.

    FIX: head-dot guard uses np.isfinite — completely avoids the
    falsy-float bug where `if last_lat` silently skipped valid small/
    negative coordinate values.
    """
    lat_obs  = data["lat_obs"][:end_idx]
    lon_obs  = data["lon_obs"][:end_idx]
    lat_pred = data["lat_pred"][:end_idx]
    lon_pred = data["lon_pred"][:end_idx]
    miss     = data["missing"][:end_idx]
    ok       = ~miss & np.isfinite(lat_obs)
    est      =  miss & np.isfinite(lat_pred)

    lat_range = (data["true_lat"].min(), data["true_lat"].max())
    lon_range = (data["true_lon"].min(), data["true_lon"].max())

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=lon_obs[ok], y=lat_obs[ok], mode="lines+markers",
        line=dict(color="#22c55e", width=2),
        marker=dict(size=4, color="#22c55e"),
        showlegend=False,
    ))
    if est.any():
        fig.add_trace(go.Scatter(
            x=lon_pred[est], y=lat_pred[est], mode="markers",
            marker=dict(size=9, color="rgba(250,204,21,0.88)", symbol="diamond",
                        line=dict(width=1.5, color="#facc15")),
            showlegend=False,
        ))
    # ── FIXED head-dot: np.isfinite, not `if value` ───────────────────────
    head_lat = data["lat_pred"][end_idx - 1]
    head_lon = data["lon_pred"][end_idx - 1]
    if np.isfinite(head_lat) and np.isfinite(head_lon):
        fig.add_trace(go.Scatter(
            x=[head_lon], y=[head_lat], mode="markers", showlegend=False,
            marker=dict(size=14, color="#00d4ff", opacity=0.9,
                        line=dict(width=2, color="#00d4ff")),
        ))

    layout = {**PLOT_BASE}
    layout["margin"] = dict(l=50, r=12, t=12, b=40)
    fig.update_layout(
        **layout, height=300, showlegend=False,
        xaxis=dict(**XAXIS_BASE, title="Lon",
                   range=[lon_range[0] - 0.001, lon_range[1] + 0.001]),
        yaxis=dict(**YAXIS_BASE, title="Lat",
                   range=[lat_range[0] - 0.001, lat_range[1] + 0.001]),
    )
    return fig


# ── FIX: error handling wrapper for entire LoRa tab ──────────────────────────
def tab_lora() -> None:
    try:
        _tab_lora_inner()
    except Exception as exc:
        import traceback
        st.markdown(
            f'<div class="error-card">'
            f'⚠ MODULE ERROR · LoRa Telemetry<br>'
            f'<span style="opacity:0.75;">{exc}</span><br>'
            f'<span style="opacity:0.45;font-size:0.72rem;">'
            f'Try adjusting parameters or clicking Simulate again.</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
        with st.expander("🔍 Debug Traceback"):
            st.code(traceback.format_exc(), language="python")


def _tab_lora_inner() -> None:
    st.markdown(
        '<div class="section-label">Module 01 — LoRa Telemetry Reconstruction</div>',
        unsafe_allow_html=True,
    )
    st.markdown("""<div class="info-card">
    <b>Algorithm:</b> Missing packets detected via <code>NaN</code> gaps in the incoming
    stream. A <b>velocity-based predictor</b> uses coordinates at <code>t-1</code> and
    <code>t-2</code> to extrapolate position at <code>t</code>. An
    <b>exponential smoother (α=0.72)</b> reduces jitter across consecutive losses.
    Estimated nodes render as <b style="color:#facc15">◆ yellow diamonds</b> — visually
    distinct from <b style="color:#22c55e">● green verified</b> packets until the next
    valid frame arrives.
    </div>""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        n_pts   = st.slider("Trajectory Points", 80, 500, 220, 10)
    with c2:
        loss    = st.slider("Packet Loss Rate", 0.05, 0.55, 0.28, 0.01, format="%.2f")
    with c3:
        show_gt = st.toggle("Show Ground Truth", value=True)

    if st.button("⚡  SIMULATE TELEMETRY FEED", key="btn_tel"):
        with st.spinner("📡  Ingesting LoRa stream … detecting fragmented packets … reconstructing gaps …"):
            time.sleep(1.4)
            st.session_state.tel_result = run_telemetry(n_pts, loss, _seed())
        st.success("✅  Telemetry stream reconstructed — all gaps filled via velocity prediction")

    res = st.session_state.tel_result
    if res is None:
        st.markdown(
            '<div class="empty-state">◈ &nbsp; AWAITING SIMULATION TRIGGER &nbsp; ◈'
            '<br><span style="font-size:0.7rem;opacity:0.5;">'
            'Configure parameters above and click simulate</span></div>',
            unsafe_allow_html=True,
        )
        return

    # ── Metrics ──
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Packet Loss",        f"{res['loss_pct']:.1f}%")
    m2.metric("Total Points",       str(res["n_pts"]))
    m3.metric("Gaps Recovered",     str(res["n_rec"]))
    m4.metric("Avg Position Error", f"{res['avg_m']:.2f} m")

    st.plotly_chart(build_telemetry_fig(res, show_gt), use_container_width=True)
    st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)

    # ── Live playback ──
    st.markdown('<div class="section-label">▶ Live Stream Playback</div>', unsafe_allow_html=True)

    pb1, pb2, pb3 = st.columns([1, 2, 1])
    with pb1:
        spd = st.select_slider("Speed", ["0.25×", "0.5×", "1×", "2×", "4×"], value="1×")
    with pb2:
        st.markdown(
            "<div style='padding-top:10px;font-family:JetBrains Mono,monospace;"
            "font-size:0.74rem;color:#3a5068;'>"
            "Replay packet-by-packet — watch estimated gaps fill in real time"
            "</div>",
            unsafe_allow_html=True,
        )
    with pb3:
        # ── FIX: STOP button sets session flag; loop checks it per frame ──
        if st.button("⏹  STOP", key="btn_stop"):
            st.session_state.stop_playback = True

    if st.button("▶  PLAY TELEMETRY STREAM", key="btn_play"):
        st.session_state.stop_playback = False   # reset stale stop signal

        speed_map = {"0.25×": 0.20, "0.5×": 0.11, "1×": 0.06, "2×": 0.028, "4×": 0.010}
        delay = speed_map[spd]
        total = res["n_pts"]
        step  = max(1, total // 60)    # cap at ~60 render frames for any size

        pb_slot    = st.empty()
        chart_slot = st.empty()
        stats_slot = st.empty()

        for end in range(4, total + 1, step):
            # ── Non-blocking stop: check flag each frame ───────────────────
            if st.session_state.get("stop_playback", False):
                pb_slot.markdown(
                    f'<div style="font-family:JetBrains Mono,monospace;font-size:0.7rem;'
                    f'color:#f59e0b;padding:8px 0;letter-spacing:0.1em;">'
                    f'⏹ STOPPED — {end}/{total} packets rendered</div>',
                    unsafe_allow_html=True,
                )
                break

            frac        = end / total
            verified_n  = int((~res["missing"][:end] & np.isfinite(res["lat_obs"][:end])).sum())
            estimated_n = int(( res["missing"][:end] & np.isfinite(res["lat_pred"][:end])).sum())

            pb_slot.markdown(f"""
            <div style="margin:4px 0 10px;">
                <div style="display:flex;justify-content:space-between;
                     font-family:'JetBrains Mono',monospace;font-size:0.68rem;
                     color:#3a5068;margin-bottom:5px;">
                    <span>STREAM PLAYBACK</span>
                    <span>PKT {end}/{total} &nbsp;·&nbsp; {frac*100:.0f}%</span>
                </div>
                <div style="background:#0b1220;border-radius:4px;height:7px;
                     border:1px solid rgba(0,212,255,0.12);overflow:hidden;">
                    <div style="background:linear-gradient(90deg,#00d4ff,#a855f7);
                         height:100%;width:{frac*100:.1f}%;border-radius:4px;"></div>
                </div>
            </div>""", unsafe_allow_html=True)

            chart_slot.plotly_chart(build_playback_fig(res, end), use_container_width=True)

            stats_slot.markdown(f"""
            <div style="display:flex;gap:24px;font-family:'JetBrains Mono',monospace;
                 font-size:0.73rem;padding:4px 0;">
                <span style="color:#22c55e;">● VERIFIED: {verified_n}</span>
                <span style="color:#facc15;">◆ ESTIMATED: {estimated_n}</span>
                <span style="color:#5a7a9a;">LOSS RATE: {estimated_n/end*100:.1f}%</span>
            </div>""", unsafe_allow_html=True)

            time.sleep(delay)
        else:
            # for-loop completed without break → stream finished normally
            pb_slot.markdown(
                f'<div style="font-family:JetBrains Mono,monospace;font-size:0.7rem;'
                f'color:#00d4ff;padding:8px 0;letter-spacing:0.12em;">'
                f'◈ STREAM COMPLETE — {total} PACKETS PROCESSED — '
                f'{res["n_rec"]} GAPS RECONSTRUCTED</div>',
                unsafe_allow_html=True,
            )

    # ── Packet log ──
    with st.expander("📋  Packet Log (first 50 entries)"):
        rows = [
            {
                "#":        i,
                "True Lat": f"{res['true_lat'][i]:.6f}",
                "True Lon": f"{res['true_lon'][i]:.6f}",
                "Pred Lat": f"{res['lat_pred'][i]:.6f}" if np.isfinite(res["lat_pred"][i]) else "—",
                "Pred Lon": f"{res['lon_pred'][i]:.6f}" if np.isfinite(res["lon_pred"][i]) else "—",
                "Status":   "🟡 ESTIMATED" if res["missing"][i] else "✅ VERIFIED",
            }
            for i in range(min(50, res["n_pts"]))
        ]
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


# ══════════════════════════════════════════════════════════════════
# ── MODULE 02: PREDICTIVE TRAFFIC CONGESTION MODELING ──
# ══════════════════════════════════════════════════════════════════

def generate_traffic(
    n: int, intensity: float, spike: bool, rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Synthetic traffic series: random walk + rush-hour harmonics + optional spike.

    FIX: original app__1__.py double-clipped noise before adding rush-hour component,
    artificially compressing dynamic range. Now a single clip is applied after all
    components are combined.
    """
    noise  = rng.normal(0, 2.8 * intensity, n).cumsum()
    t      = np.linspace(0, 2 * np.pi, n)
    rush   = 12 * intensity * (np.sin(t * 3) + 0.5 * np.sin(t * 7))
    series = np.clip(42 + intensity * 0.75 * noise + rush, 5, 98)   # ← single clip

    if spike:
        si = int(rng.integers(20, max(21, n - 25)))
        w  = int(rng.integers(5, 12))
        for j in range(w):
            if si + j < n:
                series[si + j] = min(98, series[si + j] + 28 * intensity)

    return np.arange(n, dtype=float), series.astype(float)


def forecast_traffic(
    series: np.ndarray, horizon: int = 15, window: int = 6,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Hybrid forecast: MA-anchor + global linear trend (polyfit).
    Confidence band = ±1.65σ of recent residuals (≈ 90 % CI).
    """
    n = len(series)
    t = np.arange(n, dtype=float)
    slope, intercept = np.polyfit(t, series, 1)
    ma         = float(np.mean(series[-window:]))
    fitted_end = float(np.polyval((slope, intercept), t[-1]))
    offset     = ma - fitted_end           # bias-correct so forecast starts from MA

    ft        = np.arange(n, n + horizon, dtype=float)
    base      = np.clip(np.polyval((slope, intercept), ft) + offset, 0, 100)
    resid_std = float(np.std(
        series[-window:] - np.polyval((slope, intercept), t[-window:])
    ))
    upper = np.clip(base + 1.65 * resid_std, 0, 100)
    lower = np.clip(base - 1.65 * resid_std, 0, 100)
    return ft, base, upper, lower


def congestion_info(v: float) -> tuple[str, str, str, str, str]:
    if v >= 70:
        return "HIGH",   "#ef4444", "rgba(239,68,68,0.09)",  "rgba(239,68,68,0.32)",  "⚠ IMMEDIATE ACTION REQUIRED"
    if v >= 40:
        return "MEDIUM", "#f59e0b", "rgba(245,158,11,0.09)", "rgba(245,158,11,0.32)", "◉ MONITOR CLOSELY"
    return             "LOW",    "#22c55e", "rgba(34,197,94,0.09)",  "rgba(34,197,94,0.32)",  "✓ NOMINAL FLOW"


def run_traffic(n: int, intensity: float, spike: bool, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    t_past, past         = generate_traffic(n, intensity, spike, rng)
    ft, fc, upper, lower = forecast_traffic(past)
    curr                 = float(past[-1])
    peak                 = float(np.max(fc))
    risk, col, bg, border, msg = congestion_info(max(curr, peak))
    return dict(
        t_past=t_past, past=past,
        ft=ft, fc=fc, upper=upper, lower=lower,
        curr=curr, peak=peak,
        risk=risk, col=col, bg=bg, border=border, msg=msg,
    )


def build_traffic_fig(data: dict) -> go.Figure:
    ft, fc, upper, lower = data["ft"], data["fc"], data["upper"], data["lower"]
    fig = go.Figure()

    # Confidence band (filled polygon)
    fig.add_trace(go.Scatter(
        x=np.concatenate([ft, ft[::-1]]),
        y=np.concatenate([upper, lower[::-1]]),
        fill="toself", fillcolor="rgba(239,68,68,0.10)",
        line=dict(color="rgba(0,0,0,0)"),
        name="Confidence Band (±1.65σ)", hoverinfo="skip",
    ))
    # Observed history
    fig.add_trace(go.Scatter(
        x=data["t_past"], y=data["past"], mode="lines",
        name="Observed Traffic",
        line=dict(color="#00d4ff", width=2.5),
        hovertemplate="Step %{x:.0f} · Load: <b>%{y:.1f}</b><extra>Observed</extra>",
    ))
    # Bridge connector
    fig.add_trace(go.Scatter(
        x=[data["t_past"][-1], ft[0]], y=[data["past"][-1], fc[0]],
        mode="lines", line=dict(color="#3a5068", width=1, dash="dot"),
        showlegend=False, hoverinfo="skip",
    ))
    # Forecast line
    fig.add_trace(go.Scatter(
        x=ft, y=fc, mode="lines+markers",
        name="Forecast (15-step)",
        line=dict(color="#ef4444", width=2.5, dash="dash"),
        marker=dict(size=7, color="#fca5a5", line=dict(width=1.5, color="#ef4444")),
        hovertemplate="t+%{x:.0f} · Forecast: <b>%{y:.1f}</b><extra>Forecast</extra>",
    ))
    # Band edges
    for y_vals, label in [(upper, "Upper Band"), (lower, "Lower Band")]:
        fig.add_trace(go.Scatter(
            x=ft, y=y_vals, mode="lines", name=label,
            line=dict(color="rgba(239,68,68,0.35)", width=1, dash="dot"),
            hoverinfo="skip",
        ))
    # Threshold reference lines
    fig.add_hline(y=70, line=dict(color="rgba(239,68,68,0.38)", width=1, dash="dot"),
                  annotation_text="HIGH",   annotation_position="right",
                  annotation_font=dict(color="#ef4444", size=9))
    fig.add_hline(y=40, line=dict(color="rgba(245,158,11,0.38)", width=1, dash="dot"),
                  annotation_text="MEDIUM", annotation_position="right",
                  annotation_font=dict(color="#f59e0b", size=9))

    layout = {**PLOT_BASE}
    layout["margin"] = dict(l=58, r=72, t=52, b=48)
    layout["hovermode"] = "x unified"
    fig.update_layout(
        **layout, height=520,
        xaxis=dict(**XAXIS_BASE, title="Time Step"),
        yaxis=dict(**YAXIS_BASE, title="Congestion Index (0–100)", range=[0, 108]),
        legend=dict(orientation="h", y=1.07, x=0, xanchor="left",
                    bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
        title=dict(
            text="Traffic Load  ·  🔵 Observed  ·  🔴 Forecast  ·  Shaded = Uncertainty Band",
            font=dict(color="#00d4ff", size=12, family="JetBrains Mono"),
        ),
    )
    return fig


# ── FIX: error handling wrapper for entire Traffic tab ───────────────────────
def tab_traffic() -> None:
    try:
        _tab_traffic_inner()
    except Exception as exc:
        import traceback
        st.markdown(
            f'<div class="error-card">'
            f'⚠ MODULE ERROR · Traffic Congestion<br>'
            f'<span style="opacity:0.75;">{exc}</span><br>'
            f'<span style="opacity:0.45;font-size:0.72rem;">'
            f'Try adjusting parameters or clicking Simulate again.</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
        with st.expander("🔍 Debug Traceback"):
            st.code(traceback.format_exc(), language="python")


def _tab_traffic_inner() -> None:
    st.markdown(
        '<div class="section-label">Module 02 — Predictive Traffic Congestion Modeling</div>',
        unsafe_allow_html=True,
    )
    st.markdown("""<div class="info-card">
    <b>Algorithm:</b> A <b>hybrid forecasting engine</b> blends a
    <code>6-point trailing moving average</code> with a <b>global linear trend</b>
    extracted via <code>numpy.polyfit(deg=1)</code>. Projects <b>15 steps ahead</b>
    with a <b>±1.65σ confidence band</b> from recent residuals.
    Congestion classified as <b style="color:#ef4444">HIGH</b> (&gt;70),
    <b style="color:#f59e0b">MEDIUM</b> (40–70), <b style="color:#22c55e">LOW</b> (&lt;40).
    Anomaly spike simulates real incidents — accidents, road blockages.
    </div>""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        intensity = st.slider("Traffic Intensity", 0.4, 2.5, 1.1, 0.05)
    with c2:
        n_hist    = st.slider("History Length (steps)", 60, 300, 160, 10)
    with c3:
        spike     = st.toggle("Inject Anomaly Spike", value=False)

    if st.button("⚡  RUN TRAFFIC SIMULATION", key="btn_traf"):
        with st.spinner("🚦  Ingesting multi-source feeds … fitting trend model … projecting congestion …"):
            time.sleep(1.4)
            st.session_state.traf_result = run_traffic(n_hist, intensity, spike, _seed())
        st.success("✅  Traffic forecast computed — 15 steps projected with confidence bands")

    res = st.session_state.traf_result
    if res is None:
        st.markdown(
            '<div class="empty-state">◈ &nbsp; AWAITING SIMULATION TRIGGER &nbsp; ◈'
            '<br><span style="font-size:0.7rem;opacity:0.5;">'
            'Configure parameters above and click simulate</span></div>',
            unsafe_allow_html=True,
        )
        return

    # ── Metrics ──
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Current Load",    f"{res['curr']:.1f}")
    m2.metric("Predicted Peak",  f"{res['peak']:.1f}")
    with m3:
        st.markdown(f"""
        <div style="background:{res['bg']};border:1px solid {res['border']};
             border-radius:10px;padding:14px 18px;min-height:90px;">
            <div style="color:#5a7a9a;font-size:0.78rem;margin-bottom:6px;
                 letter-spacing:0.04em;">Risk Level</div>
            <div style="color:{res['col']};font-family:'Orbitron',monospace;
                 font-size:1.55rem;font-weight:700;letter-spacing:0.05em;">{res['risk']}</div>
            <div style="color:{res['col']};font-size:0.65rem;opacity:0.85;
                 font-family:'JetBrains Mono',monospace;margin-top:5px;letter-spacing:0.06em;">
                {res['msg']}
            </div>
        </div>""", unsafe_allow_html=True)
    m4.metric("Forecast Horizon", "15 steps")

    st.plotly_chart(build_traffic_fig(res), use_container_width=True)

    # ── 15-step forecast table ──
    with st.expander("📋  15-Step Forecast Breakdown"):
        rows = [
            {
                "Step":        f"t+{i + 1}",
                "Forecast":    f"{v:.1f}",
                "Upper (95%)": f"{u:.1f}",
                "Lower (95%)": f"{lo:.1f}",
                "Congestion":  congestion_info(v)[0],
            }
            for i, (v, u, lo) in enumerate(zip(res["fc"], res["upper"], res["lower"]))
        ]
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    # ── Zone alert cards ──
    st.markdown(
        '<div class="section-label" style="margin-top:18px;">Congestion Zone Alerts</div>',
        unsafe_allow_html=True,
    )
    a1, a2, a3 = st.columns(3)
    high_n = sum(1 for v in res["fc"] if v >= 70)
    med_n  = sum(1 for v in res["fc"] if 40 <= v < 70)
    low_n  = sum(1 for v in res["fc"] if v < 40)
    _zone_card(a1, high_n, "#ef4444", "rgba(239,68,68,0.08)",  "rgba(239,68,68,0.3)",  "HIGH CONGESTION STEPS")
    _zone_card(a2, med_n,  "#f59e0b", "rgba(245,158,11,0.08)", "rgba(245,158,11,0.3)", "MEDIUM CONGESTION STEPS")
    _zone_card(a3, low_n,  "#22c55e", "rgba(34,197,94,0.08)",  "rgba(34,197,94,0.3)",  "LOW CONGESTION STEPS")


def _zone_card(col, count: int, fg: str, bg: str, border: str, label: str) -> None:
    col.markdown(f"""
    <div style="background:{bg};border:1px solid {border};border-radius:8px;
         padding:14px 16px;text-align:center;">
        <div style="color:{fg};font-family:'Orbitron',monospace;
             font-size:1.5rem;font-weight:700;">{count}</div>
        <div style="color:#5a7a9a;font-size:0.72rem;margin-top:4px;
             font-family:'JetBrains Mono',monospace;">{label}</div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════
def main() -> None:
    inject_css()
    init_state()
    page = render_sidebar()
    render_header()

    if "LoRa" in page:
        tab_lora()
    else:
        tab_traffic()

    st.markdown(
        '<div class="footer">'
        "SENTINEL AI &nbsp;·&nbsp; SIDDHARTH SINGH &nbsp;·&nbsp; "
        "CYBERJOAR AI &nbsp;·&nbsp; OC.41335.2026.59218 &nbsp;·&nbsp; "
        f"sashrik@cyberjoar.com &nbsp;·&nbsp; v{__version__}"
        "</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
