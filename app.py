import streamlit as st

st.set_page_config(
    page_title="Manmeet's Diet Plan",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed",   # start collapsed — nav is top bar
)

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&family=Space+Mono:wght@400;700&display=swap');

/* ---- Reset & base ---- */
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif !important; }
.block-container { padding: 1.5rem 2rem 4rem !important; max-width: 1300px !important; }
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ---- Hide sidebar toggle arrow entirely so it doesn't confuse ---- */
[data-testid="collapsedControl"] { display: none !important; }

/* ---- TOP NAV ---- */
.top-nav {
    display: flex;
    align-items: center;
    gap: .4rem;
    flex-wrap: wrap;
    background: #060f1c;
    border: 1px solid rgba(0,229,200,.15);
    border-radius: 1rem;
    padding: .6rem .8rem;
    margin-bottom: 1.5rem;
}
.nav-logo {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1rem;
    color: #00e5c8;
    margin-right: .8rem;
    white-space: nowrap;
}

/* ---- Metric cards ---- */
[data-testid="stMetric"] {
    background: #0b1e2d !important;
    border: 1px solid rgba(0,229,200,.18) !important;
    border-radius: 1rem !important;
    padding: 1rem 1.2rem !important;
    transition: transform .25s, border-color .25s !important;
}
[data-testid="stMetric"]:hover { transform: translateY(-3px) !important; border-color: #00e5c8 !important; }
[data-testid="stMetricLabel"] p { font-size: .72rem !important; color: #7ba8a0 !important; text-transform: uppercase !important; letter-spacing: .1em !important; }
[data-testid="stMetricValue"] { font-family: 'Space Mono', monospace !important; color: #00e5c8 !important; font-size: 1.5rem !important; }
[data-testid="stMetricDelta"] { color: #7ba8a0 !important; font-size: .75rem !important; }

/* ---- Tabs ---- */
.stTabs [data-baseweb="tab-list"] { gap: .5rem; background: transparent; border-bottom: 1px solid rgba(0,229,200,.12); padding-bottom: .4rem; flex-wrap: wrap; }
.stTabs [data-baseweb="tab"] { background: rgba(0,229,200,.06); border: 1px solid rgba(0,229,200,.15); border-radius: 2rem; color: #7ba8a0 !important; font-size: .82rem; padding: .35rem 1.1rem; }
.stTabs [aria-selected="true"] { background: #00e5c8 !important; color: #03080f !important; border-color: #00e5c8 !important; font-weight: 700; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 1.2rem; }

/* ---- Progress bars ---- */
.stProgress > div > div { background: linear-gradient(90deg,#00e5c8,#ffd166) !important; border-radius: 4px; }

/* ---- Slider ---- */
.stSlider [data-baseweb="slider"] { padding: 0 .5rem; }

/* ---- Expanders ---- */
.streamlit-expanderHeader { background: #0b1e2d !important; border: 1px solid rgba(0,229,200,.15) !important; border-radius: .8rem !important; color: #e2f4f0 !important; }
.streamlit-expanderContent { background: #091628 !important; border: 1px solid rgba(0,229,200,.08) !important; border-top: none !important; border-radius: 0 0 .8rem .8rem !important; }

/* ---- Selectbox (used for nav fallback) ---- */
.stSelectbox > div > div { background: #0b1e2d !important; border: 1px solid rgba(0,229,200,.2) !important; border-radius: .6rem !important; color: #e2f4f0 !important; }

/* ---- Alert boxes ---- */
.stAlert { border-radius: .8rem !important; }

/* ---- All markdown text ---- */
.stMarkdown, .stMarkdown p, .stMarkdown li { color: #b0ccc8 !important; line-height: 1.7; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; color: #e2f4f0 !important; }
hr { border-color: rgba(0,229,200,.1) !important; }

/* ---- Animations ---- */
@keyframes fadeUp { from { opacity:0; transform:translateY(18px); } to { opacity:1; transform:translateY(0); } }
@keyframes glowPulse { 0%,100% { text-shadow: 0 0 8px rgba(0,229,200,.3); } 50% { text-shadow: 0 0 18px rgba(0,229,200,.8); } }
@keyframes float { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-6px); } }

/* ── COMPONENT STYLES ── */
.hero-banner {
    background: linear-gradient(135deg,#060f1c 0%,#091628 55%,#03080f 100%);
    border: 1px solid rgba(0,229,200,.2);
    border-radius: 1.5rem;
    padding: 2.2rem 2.8rem;
    margin-bottom: 1.8rem;
    position: relative;
    overflow: hidden;
    animation: fadeUp .6s ease both;
}
.hero-banner::before {
    content: '';
    position: absolute; top: -40%; right: -15%;
    width: 380px; height: 380px;
    background: radial-gradient(circle,rgba(0,229,200,.07) 0%,transparent 65%);
    pointer-events: none;
}
.hero-title { font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800; color:#e2f4f0; line-height:1.08; margin:0 0 .4rem; }
.hero-accent { color:#00e5c8; }
.hero-sub { color:#7ba8a0; font-size:.9rem; margin:.4rem 0 0; }
.hero-badge { display:inline-flex; align-items:center; gap:.5rem; background:rgba(255,107,53,.12); border:1px solid rgba(255,107,53,.3); border-radius:2rem; padding:.3rem .9rem; font-size:.73rem; color:#ff6b35; margin-bottom:.9rem; }

/* Section labels */
.stag { font-size:.68rem; letter-spacing:.22em; text-transform:uppercase; color:#00e5c8; display:flex; align-items:center; gap:.6rem; margin-bottom:.4rem; }
.stag::before { content:''; width:22px; height:1px; background:#00e5c8; }
.stitle { font-family:'Syne',sans-serif; font-size:1.75rem; font-weight:800; color:#e2f4f0; margin:0 0 .25rem; }
.ssub { color:#7ba8a0; font-size:.86rem; margin-bottom:1.4rem; }

/* Cards */
.card-base {
    background: #0b1e2d;
    border: 1px solid rgba(0,229,200,.13);
    border-radius: 1.2rem;
    padding: 1.4rem;
    margin-bottom: .9rem;
    transition: border-color .25s, transform .25s;
    animation: fadeUp .4s ease both;
}
.card-base:hover { border-color: #00e5c8; transform: translateY(-3px); }

/* Blood cards */
.blood-card { border-radius:.9rem; padding:1.1rem 1.3rem; margin-bottom:.7rem; border-left:4px solid; animation:fadeUp .5s ease both; }
.blood-card.critical { background:rgba(255,107,53,.08); border-color:#ff6b35; }
.blood-card.high     { background:rgba(255,107,53,.05); border-color:rgba(255,107,53,.5); }
.blood-card.moderate { background:rgba(255,209,102,.06); border-color:#ffd166; }
.blood-card.clear    { background:rgba(0,229,200,.05); border-color:#00e5c8; }

/* Meal cards */
.meal-card { background:#0b1e2d; border:1px solid rgba(0,229,200,.13); border-radius:1.2rem; padding:1.3rem; margin-bottom:.9rem; transition:all .25s; animation:fadeUp .4s ease both; }
.meal-card:hover { border-color:#00e5c8; background:#0d2336; transform:translateY(-3px); }
.opt-badge { display:inline-flex; align-items:center; justify-content:center; width:28px; height:28px; background:rgba(0,229,200,.15); border-radius:.4rem; font-family:'Space Mono',monospace; font-size:.78rem; color:#00e5c8; font-weight:700; margin-bottom:.7rem; }
.meal-name { font-family:'Syne',sans-serif; font-weight:700; font-size:.98rem; color:#e2f4f0; margin-bottom:.65rem; }
.meal-item { font-size:.81rem; color:#7ba8a0; padding:.18rem 0 .18rem .9rem; position:relative; line-height:1.55; }
.meal-item::before { content:'→'; position:absolute; left:0; color:#00e5c8; font-size:.72rem; top:.05rem; }
.meal-macros { display:flex; gap:.5rem; margin-top:.85rem; padding-top:.85rem; border-top:1px solid rgba(0,229,200,.08); flex-wrap:wrap; }
.mpill { background:rgba(0,229,200,.07); border:1px solid rgba(0,229,200,.16); border-radius:1rem; padding:.18rem .65rem; font-family:'Space Mono',monospace; font-size:.7rem; color:#00e5c8; }
.mpill.o { background:rgba(255,107,53,.07); border-color:rgba(255,107,53,.2); color:#ff6b35; }
.mpill.n { background:transparent; border-color:rgba(0,229,200,.08); color:#5ba898; font-family:'DM Sans',sans-serif; font-size:.7rem; }

/* Day cards */
.day-card { background:#0b1e2d; border:1px solid rgba(0,229,200,.12); border-radius:.9rem; padding:.8rem; transition:all .25s; height:100%; }
.day-card:hover { border-color:#00e5c8; transform:translateY(-3px); }
.day-card.today { border-color:#00e5c8; background:rgba(0,229,200,.07); }
.day-name { font-family:'Syne',sans-serif; font-weight:800; font-size:.88rem; color:#e2f4f0; margin-bottom:.55rem; }
.day-card.today .day-name { color:#00e5c8; animation:glowPulse 2s infinite; }
.day-meal { font-size:.67rem; color:#7ba8a0; line-height:1.45; margin-bottom:.28rem; padding:.22rem .38rem; background:rgba(255,255,255,.03); border-radius:.3rem; }
.day-meal strong { display:block; color:#9dbfbb; font-size:.68rem; }

/* Supplement cards */
.supp-card { background:#0b1e2d; border:1px solid rgba(0,229,200,.13); border-radius:1.1rem; padding:1.2rem; margin-bottom:.8rem; transition:all .25s; }
.supp-card:hover { border-color:#00e5c8; transform:translateX(3px); }

/* Info / warn boxes */
.warn-box { background:rgba(255,107,53,.07); border:1px solid rgba(255,107,53,.25); border-radius:.85rem; padding:.9rem 1.1rem; margin:.8rem 0; font-size:.84rem; color:#ff8c70; line-height:1.6; }
.warn-box strong { display:block; margin-bottom:.18rem; font-size:.88rem; color:#ff6b35; }
.info-box { background:rgba(0,229,200,.05); border:1px solid rgba(0,229,200,.18); border-radius:.85rem; padding:.9rem 1.1rem; margin:.8rem 0; font-size:.84rem; color:#7ba8a0; line-height:1.6; }
.info-box strong { color:#00e5c8; display:block; margin-bottom:.18rem; }

/* Timeline */
.tl-wrap { position:relative; padding-left:2.4rem; }
.tl-wrap::before { content:''; position:absolute; left:18px; top:0; bottom:0; width:1px; background:linear-gradient(to bottom,#00e5c8,#ff6b35,#ffd166); opacity:.3; }
.tl-item { position:relative; margin-bottom:1.1rem; }
.tl-dot { position:absolute; left:-2.4rem; top:0; width:36px; height:36px; border-radius:50%; background:#0b1e2d; border:1px solid rgba(0,229,200,.3); display:flex; align-items:center; justify-content:center; font-size:.95rem; }
.tl-time { font-family:'Space Mono',monospace; font-size:.68rem; color:#7ba8a0; margin-bottom:.15rem; }
.tl-action { font-size:.84rem; color:#e2f4f0; font-weight:500; margin-bottom:.12rem; }
.tl-purpose { font-size:.76rem; color:#5ba898; }

/* Nutrient rows */
.nt-row { display:flex; align-items:center; justify-content:space-between; padding:.6rem .95rem; border-radius:.55rem; margin-bottom:.38rem; background:#0b1e2d; border:1px solid rgba(0,229,200,.07); font-size:.81rem; transition:all .2s; }
.nt-row:hover { border-color:rgba(0,229,200,.22); }
.nt-name { color:#e2f4f0; font-weight:500; flex:1.2; }
.nt-val  { font-family:'Space Mono',monospace; font-size:.76rem; color:#00e5c8; flex:1; text-align:center; }
.nt-tgt  { color:#7ba8a0; font-size:.73rem; flex:1; text-align:center; }
.nt-badge { border-radius:1rem; padding:.18rem .65rem; font-size:.68rem; white-space:nowrap; }
.nt-badge.g { background:rgba(0,229,200,.1); color:#00e5c8; border:1px solid rgba(0,229,200,.2); }
.nt-badge.a { background:rgba(255,209,102,.1); color:#ffd166; border:1px solid rgba(255,209,102,.2); }
.nt-badge.r { background:rgba(255,107,53,.1); color:#ff6b35; border:1px solid rgba(255,107,53,.2); }

/* Kitchen rules */
.krule { display:flex; align-items:flex-start; gap:.75rem; padding:.75rem .95rem; background:#0b1e2d; border:1px solid rgba(0,229,200,.08); border-radius:.65rem; margin-bottom:.45rem; font-size:.82rem; color:#b0ccc8; line-height:1.5; }
.krule strong { color:#00e5c8; }

/* Doctor items */
.doc-item { background:rgba(255,107,53,.07); border-left:4px solid #ff6b35; border-radius:0 .8rem .8rem 0; padding:.95rem 1.1rem; margin-bottom:.65rem; font-size:.84rem; color:#b0ccc8; line-height:1.6; }
.doc-item strong { color:#ff6b35; display:block; margin-bottom:.18rem; }

/* Retest cards */
.rt-card { background:#0b1e2d; border:1px solid rgba(255,209,102,.2); border-radius:.95rem; padding:1.1rem; margin-bottom:.75rem; transition:all .25s; }
.rt-card:hover { border-color:#ffd166; transform:translateY(-2px); }
.rt-when { font-family:'Space Mono',monospace; font-size:.73rem; color:#ffd166; margin-bottom:.35rem; }
.rt-what { font-size:.82rem; color:#b0ccc8; margin-bottom:.35rem; }
.rt-tgt  { font-size:.76rem; color:#7ba8a0; }

/* Check items */
.chk-item { display:flex; align-items:flex-start; gap:.75rem; padding:.65rem .9rem; background:#0b1e2d; border:1px solid rgba(0,229,200,.08); border-radius:.65rem; margin-bottom:.45rem; font-size:.84rem; color:#b0ccc8; }
.chk-dot { width:17px; height:17px; border-radius:50%; border:2px solid #00e5c8; flex-shrink:0; margin-top:.1rem; }

/* Row util */
.row-kv { display:flex; justify-content:space-between; align-items:center; padding:.58rem .9rem; border-bottom:1px solid rgba(0,229,200,.07); }
.row-kv:last-child { border-bottom:none; }
.kv-label { color:#7ba8a0; font-size:.82rem; }
.kv-val { font-family:'Space Mono',monospace; font-size:.79rem; color:#e2f4f0; }
.kv-val.hi { color:#00e5c8; }

/* Removed/Added items */
.r-item { background:rgba(255,107,53,.06); border:1px solid rgba(255,107,53,.15); border-radius:.65rem; padding:.65rem .95rem; margin-bottom:.38rem; }
.r-item .ri-name { font-size:.84rem; color:#e2f4f0; font-weight:500; }
.r-item .ri-why { font-size:.73rem; color:#7ba8a0; }
.a-item { background:rgba(0,229,200,.05); border:1px solid rgba(0,229,200,.15); border-radius:.65rem; padding:.65rem .95rem; margin-bottom:.38rem; }
.a-item .ai-name { font-size:.84rem; color:#e2f4f0; font-weight:500; }
.a-item .ai-why { font-size:.73rem; color:#7ba8a0; }

/* Proj cards */
.proj-card { background:#0b1e2d; border:1px solid rgba(0,229,200,.13); border-radius:1rem; padding:1.1rem; text-align:center; transition:all .25s; }
.proj-card:hover { border-color:#ffd166; transform:translateY(-3px); }
.proj-card.gold { border-color:rgba(255,209,102,.35); }

/* Chart wrapper */
.chart-wrap { background:#0b1e2d; border:1px solid rgba(0,229,200,.15); border-radius:1rem; padding:1.4rem; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE FOR PAGE ────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "🏠 Overview"

# ── TOP NAV BAR ───────────────────────────────────────────────────────────────
pages = [
    "🏠 Overview", "🩸 Blood Report", "🍽️ Meals", "📅 Weekly Plan",
    "💊 Supplements", "💧 Water & Schedule", "📊 Nutrients", "✅ Checklist", "🏥 Doctor & Retest"
]

st.markdown('<div class="top-nav"><span class="nav-logo">M · DIET</span>', unsafe_allow_html=True)
nav_cols = st.columns([1.2] + [1] * len(pages))
with nav_cols[0]:
    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
for i, p in enumerate(pages):
    with nav_cols[i + 1]:
        is_active = st.session_state.page == p
        btn_style = (
            "background:#00e5c8;color:#03080f;border:none;border-radius:2rem;"
            "padding:.3rem .7rem;font-size:.72rem;font-weight:700;cursor:pointer;white-space:nowrap;width:100%"
            if is_active else
            "background:rgba(0,229,200,.07);color:#7ba8a0;border:1px solid rgba(0,229,200,.15);"
            "border-radius:2rem;padding:.3rem .7rem;font-size:.72rem;cursor:pointer;white-space:nowrap;width:100%"
        )
        if st.button(p, key=f"nav_{p}", use_container_width=True):
            st.session_state.page = p
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

page = st.session_state.page

# ── HERO (always shown) ───────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">⚡ Blood-Report Updated — 11 April 2026</div>
  <div class="hero-title">Manmeet's <span class="hero-accent">Updated</span><br>Nutrition Blueprint</div>
  <p class="hero-sub">Precision-engineered around bloodwork · Uric acid · Liver enzymes · Iron deficiency · Lipids — all addressed</p>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# HELPERS
# ════════════════════════════════════════════════════════════════════════
def meal_cards(options):
    for ltr, name, items, kcal, prot, purine, note in options:
        ihtml = "".join(f'<div class="meal-item">{i}</div>' for i in items)
        st.markdown(
            f"<div class='meal-card'>"
            f"<div class='opt-badge'>{ltr}</div>"
            f"<div class='meal-name'>{name}</div>"
            f"{ihtml}"
            f"<div class='meal-macros'>"
            f"<span class='mpill'>{kcal}</span>"
            f"<span class='mpill o'>{prot}</span>"
            f"<span class='mpill n'>Purine: {purine}</span>"
            f"<span class='mpill n'>💡 {note}</span>"
            f"</div></div>",
            unsafe_allow_html=True
        )

def row_kv(label, val, hi=False):
    cls = "kv-val hi" if hi else "kv-val"
    st.markdown(f"<div class='row-kv'><span class='kv-label'>{label}</span><span class='{cls}'>{val}</span></div>", unsafe_allow_html=True)

def chart_js(html_str, height=300):
    # CDN MUST come first — inline new Chart() calls run immediately after,
    # so Chart.js must already be defined in the iframe when they execute.
    st.components.v1.html(
        f"""<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
        <div style="background:#0b1e2d;border:1px solid rgba(0,229,200,.15);border-radius:1rem;padding:1.4rem">
        {html_str}
        </div>""",
        height=height
    )

# ════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ════════════════════════════════════════════════════════════════════════
if page == "🏠 Overview":
    st.markdown('<div class="stag">Identity</div><div class="stitle">Profile & Targets</div>'
                '<p class="ssub">As of 10 April 2026 · Blood report 11 April 2026</p>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Current Weight", "111.6 kg", "−2.4 kg")
    c2.metric("Goal Weight", "90 kg", "21.6 kg to go")
    c3.metric("Daily Target", "1,850 kcal", "−700 kcal deficit")
    c4.metric("Protein Target", "175–180 g", "1.5 g/kg ✅")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="stag">Profile</div>', unsafe_allow_html=True)
        st.markdown("<div style='background:#0b1e2d;border:1px solid rgba(0,229,200,.13);border-radius:1rem;padding:.5rem 0'>", unsafe_allow_html=True)
        for lbl, val in [
            ("Name","Manmeet Singh Marwah"), ("Age","24 years"), ("Gender","Male"),
            ("Height","6 ft (182.88 cm)"), ("Start Weight","114 kg (2 Apr)"),
            ("Activity","~3,000 steps/day"), ("Sleep","5AM → 1PM"),
            ("Allergies","Peanuts 🚫"), ("Dislikes","Karela, Tinda, Mushrooms"),
        ]:
            row_kv(lbl, val)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stag">Daily Targets</div>', unsafe_allow_html=True)
        for name, val, color in [
            ("Protein","175–180 g/day","#00e5c8"), ("Fat","55–65 g/day","#ffd166"),
            ("Water","≥ 3.5 L/day","#00e5c8"), ("TDEE","~2,575 kcal","#7ba8a0"),
            ("Target Intake","~1,850 kcal","#00e5c8"), ("Deficit","~700 kcal/day","#ff6b35"),
        ]:
            st.markdown(
                f"<div style='display:flex;justify-content:space-between;align-items:center;"
                f"padding:.65rem 1rem;border-radius:.6rem;background:#0b1e2d;"
                f"border:1px solid rgba(0,229,200,.08);margin-bottom:.4rem'>"
                f"<span style='font-size:.84rem;color:#b0ccc8'>{name}</span>"
                f"<span style='font-family:Space Mono,monospace;font-size:.81rem;color:{color};font-weight:700'>{val}</span>"
                f"</div>",
                unsafe_allow_html=True
            )
        st.markdown('<div class="warn-box"><strong>🥜 Almond Rule — Max 5/day Total</strong>'
                    'You mentioned eating 10 on some days → +35 kcal, +3g fat extra.</div>',
                    unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="stag">Forecast</div><div class="stitle">Weight Projection</div>', unsafe_allow_html=True)
    chart_js("""
    <canvas id="wc" height="110" role="img" aria-label="Weight projection Apr–Nov"></canvas>
    <script>
    new Chart(document.getElementById('wc'),{type:'line',
      data:{labels:['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov'],
        datasets:[
          {label:'Weight (kg)',data:[111.6,108.4,105.1,101.8,98.5,95.3,92.0,88.8],
           borderColor:'#00e5c8',backgroundColor:'rgba(0,229,200,.07)',
           pointBackgroundColor:'#00e5c8',pointBorderColor:'#03080f',pointBorderWidth:2,pointRadius:5,fill:true,tension:.4},
          {label:'Goal 90 kg',data:[90,90,90,90,90,90,90,90],
           borderColor:'rgba(255,209,102,.45)',borderDash:[6,4],pointRadius:0,fill:false}
        ]},
      options:{responsive:true,plugins:{legend:{display:false},
        tooltip:{backgroundColor:'#0b1e2d',titleColor:'#00e5c8',bodyColor:'#e2f4f0',borderColor:'rgba(0,229,200,.2)',borderWidth:1}},
        scales:{x:{grid:{color:'rgba(255,255,255,.04)'},ticks:{color:'#7ba8a0'}},
                y:{min:85,max:115,grid:{color:'rgba(255,255,255,.04)'},ticks:{color:'#7ba8a0',callback:v=>v+' kg'}}}}});
    </script>""", height=290)

    c1, c2, c3, c4 = st.columns(4)
    for col, (when, what, note, gold) in zip(
        [c1, c2, c3, c4],
        [("Week 1–2","1.5–2.5 kg drop","Water + initial fat ✅",False),
         ("Month 1","~3–4 kg fat","Deficit kicking in",False),
         ("Ongoing","0.6–0.8 kg/week","Sustainable pace",False),
         ("Oct 2026","🎯 Goal: 90 kg","~6–7 months",True)]
    ):
        with col:
            border = "border-color:rgba(255,209,102,.4)" if gold else ""
            st.markdown(
                f"<div class='proj-card' style='{border}'>"
                f"<div class='rt-when'>{when}</div>"
                f"<div style='font-family:Syne,sans-serif;font-weight:700;font-size:.95rem;color:#e2f4f0;margin-bottom:.3rem'>{what}</div>"
                f"<div class='rt-tgt'>{note}</div></div>",
                unsafe_allow_html=True
            )

# ════════════════════════════════════════════════════════════════════════
# PAGE: BLOOD REPORT
# ════════════════════════════════════════════════════════════════════════
elif page == "🩸 Blood Report":
    st.markdown('<div class="stag">Bloodwork</div><div class="stitle">Health Conditions — 11 Apr 2026</div>'
                '<p class="ssub">Dr Lal PathLabs · Lab No. 514079123 · 3 critical conditions</p>', unsafe_allow_html=True)

    sections = [
        ("🔴 CRITICAL", "critical", "#ff6b35", [
            ("High Uric Acid","Serum Uric Acid","8.53 mg/dL","3.50–7.20"),
            ("Elevated Liver Enzymes (NAFLD likely)","ALT (SGPT)","95.2 U/L","< 50 U/L"),
            ("Iron Deficiency Anaemia","Iron / MCV / MCH","55.6 / 81.6 / 25.1","65+ / 83+ / 27+"),
        ]),
        ("🟠 HIGH", "high", "#ff8c55", [
            ("High Triglycerides","Triglycerides","175 mg/dL","< 150 mg/dL"),
        ]),
        ("⚠️ MODERATE", "moderate", "#ffd166", [
            ("Low HDL","HDL Cholesterol","39 mg/dL","> 40"),
            ("High LDL","LDL Cholesterol","131 mg/dL","< 100"),
            ("Systemic Inflammation","HsCRP","6.70 mg/L","< 1.00"),
            ("Vitamin D Insufficient","25-OH Vit D","68.70 nmol/L","75–250"),
            ("B12 Low-Normal","Vitamin B12","227 pg/mL","211–946"),
            ("Mildly High Urea / BUN","Urea / BUN","43.7 / 20.4","< 43 / < 20"),
        ]),
        ("✅ CLEAR", "clear", "#00e5c8", [
            ("Thyroid","TSH / FT3 / FT4","3.29 / 4.28 / 1.43","Normal"),
            ("Blood Sugar","Fasting / HbA1c","84.2 / 5.5%","Normal"),
            ("Kidney Function","Creatinine / GFR","0.93 / 117","Normal"),
        ]),
    ]
    for sev, cls, color, items in sections:
        st.markdown(f"<div style='font-size:.73rem;font-weight:700;letter-spacing:.1em;color:#7ba8a0;text-transform:uppercase;margin:1.1rem 0 .55rem'>{sev}</div>", unsafe_allow_html=True)
        cols = st.columns(min(len(items), 3))
        for i, (cond, marker, val, ref) in enumerate(items):
            with cols[i % 3]:
                st.markdown(
                    f"<div class='blood-card {cls}'>"
                    f"<div style='font-size:.81rem;color:{color};font-weight:500;margin-bottom:.25rem'>{cond}</div>"
                    f"<div style='font-family:Space Mono,monospace;font-size:.72rem;color:#7ba8a0;margin-bottom:.18rem'>{marker}</div>"
                    f"<div style='font-family:Syne,sans-serif;font-size:1.35rem;font-weight:700;color:{color}'>{val}</div>"
                    f"<div style='font-size:.7rem;color:#7ba8a0;margin-top:.18rem'>Ref: {ref}</div>"
                    f"</div>",
                    unsafe_allow_html=True
                )

    st.markdown("<br>", unsafe_allow_html=True)
    chart_js("""
    <div style="max-width:460px;margin:0 auto">
    <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.15em;color:#7ba8a0;margin-bottom:.8rem;text-align:center">Marker Status — % of limit</div>
    <canvas id="radar" role="img" aria-label="Blood marker radar"></canvas></div>
    <script>new Chart(document.getElementById('radar'),{type:'radar',
      data:{labels:['Uric Acid','ALT/Liver','Iron','Triglycerides','HDL','LDL','HsCRP','Vitamin D','Thyroid','Blood Sugar'],
        datasets:[
          {label:'Your values',data:[118,190,85,117,97,131,670,92,100,100],
           borderColor:'#ff6b35',backgroundColor:'rgba(255,107,53,.12)',pointBackgroundColor:'#ff6b35',pointRadius:4,borderWidth:2},
          {label:'Target',data:[100,100,100,100,100,100,100,100,100,100],
           borderColor:'rgba(0,229,200,.4)',backgroundColor:'transparent',pointRadius:0,borderDash:[5,5],borderWidth:1}
        ]},
      options:{responsive:true,plugins:{legend:{labels:{color:'#7ba8a0',font:{size:10}}},
        tooltip:{backgroundColor:'#0b1e2d',titleColor:'#00e5c8',bodyColor:'#e2f4f0',borderColor:'rgba(0,229,200,.2)',borderWidth:1}},
        scales:{r:{grid:{color:'rgba(255,255,255,.06)'},angleLines:{color:'rgba(255,255,255,.06)'},
          pointLabels:{color:'#7ba8a0',font:{size:9}},ticks:{display:false},suggestedMin:0,suggestedMax:200}}}});
    </script>""", height=400)

# ════════════════════════════════════════════════════════════════════════
# PAGE: MEALS
# ════════════════════════════════════════════════════════════════════════
elif page == "🍽️ Meals":
    st.markdown('<div class="stag">Food</div><div class="stitle">Meal Options</div>'
                '<p class="ssub">All meals updated for uric acid + liver health · Mutton & Prawns removed</p>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><strong>✅ Add to every meal:</strong> Turmeric + black pepper · Lemon on vegetables · Garlic in all cooking</div>', unsafe_allow_html=True)

    # PLATEAU ALERT
    st.markdown("""
    <div style='background:rgba(255,209,102,.08);border:1px solid rgba(255,209,102,.3);border-radius:1rem;
        padding:1.2rem 1.5rem;margin-bottom:1.5rem;display:flex;align-items:flex-start;gap:1rem'>
        <div style='font-size:1.5rem;flex-shrink:0'>⚖️</div>
        <div>
            <div style='font-family:Syne,sans-serif;font-weight:800;font-size:1rem;color:#ffd166;margin-bottom:.35rem'>
                Plateau Alert — Weight Stuck at 110.7 kg</div>
            <div style='font-size:.83rem;color:#b0a070;line-height:1.6'>
                Body adapted to same ~1,850 kcal and identical food patterns within 2–3 weeks.
                Fix: <strong style='color:#ffd166'>calorie cycling + dramatically more variety</strong> to keep metabolism guessing.
                New meal options below are expanded to break the plateau.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # OLD WEEK CHART — collapsible
    with st.expander("📅 Old Week Diet Chart (Original — April 11) — click to expand / collapse", expanded=False):
        st.markdown("""
        <div style='background:rgba(0,229,200,.03);border:1px solid rgba(0,229,200,.1);border-radius:.8rem;padding:1rem;margin-bottom:.8rem'>
        <div style='font-size:.72rem;color:#7ba8a0;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.8rem'>
        Original rotation · Fixed 1,850 kcal daily · Simpler food library</div>
        """, unsafe_allow_html=True)
        old_weekly = [
            ("Mon","🅐 Classic Chicken Bowl","🅑 Curd Bowl","🅐 Chicken+Roti+Palak 🌱",True),
            ("Tue","🅑 Egg Bhurji Plate","🅓 Boiled Eggs+Veggies","🅑 Chicken+Mixed Veggies",False),
            ("Wed","🅒 Paneer Bhurji Plate","🅑 Curd Bowl","🅒 Chicken+Dahi Rice",False),
            ("Thu","🅐 Classic Chicken Bowl","🅒 Makhana+Egg","🅓 Chicken+Palak+Veggies 🌱",False),
            ("Fri","🅓 Hi-Pro Chicken Bowl","🅐 Seeds+Veggies","🅑 Chicken+Mixed Veggies",False),
            ("Sat","🅔 Chicken Salad Bowl","🅔 Banana+Curd","🅔 Paneer+Egg White 🌱",False),
            ("Sun","🅑 Egg Bhurji Plate","🅓 Boiled Eggs+Veggies","🅐 Chicken+Roti+Palak 🌱",False),
        ]
        cols = st.columns(7)
        for col,(day,m1,sn,dn,today) in zip(cols,old_weekly):
            with col:
                cls = "day-card today" if today else "day-card"
                st.markdown(f"<div class='{cls}'><div class='day-name'>{day}</div>"
                    f"<div class='day-meal'><strong>Meal 1</strong>{m1}</div>"
                    f"<div class='day-meal'><strong>Snack</strong>{sn}</div>"
                    f"<div class='day-meal'><strong>Dinner</strong>{dn}</div></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # NEW WEEK CHART HEADER
    st.markdown("""
    <div style='display:flex;align-items:center;gap:.8rem;margin:1.5rem 0 .5rem'>
        <div style='width:3px;height:28px;background:linear-gradient(to bottom,#ffd166,#00e5c8);border-radius:2px'></div>
        <div>
            <div style='font-family:Syne,sans-serif;font-weight:800;font-size:1.1rem;color:#e2f4f0'>
                New Week Diet Chart — Plateau-Breaking</div>
            <div style='font-size:.78rem;color:#7ba8a0'>
                Calorie cycling · Expanded food library · Dals, new veg, new marinades</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Calorie cycling protocol
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("""<div style='background:rgba(255,107,53,.08);border:1px solid rgba(255,107,53,.25);
            border-radius:.9rem;padding:1rem;text-align:center'>
            <div style='font-size:1.4rem;margin-bottom:.3rem'>🔴</div>
            <div style='font-family:Space Mono,monospace;font-size:1.3rem;font-weight:700;color:#ff6b35'>~1,650</div>
            <div style='font-size:.78rem;color:#e2f4f0;font-weight:600;margin:.2rem 0'>Low Days</div>
            <div style='font-size:.72rem;color:#7ba8a0'>Mon · Wed · Fri<br>Push deficit deeper</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div style='background:rgba(0,229,200,.06);border:1px solid rgba(0,229,200,.2);
            border-radius:.9rem;padding:1rem;text-align:center'>
            <div style='font-size:1.4rem;margin-bottom:.3rem'>⭐</div>
            <div style='font-family:Space Mono,monospace;font-size:1.3rem;font-weight:700;color:#00e5c8'>~1,850</div>
            <div style='font-size:.78rem;color:#e2f4f0;font-weight:600;margin:.2rem 0'>Normal Days</div>
            <div style='font-size:.72rem;color:#7ba8a0'>Tue · Thu · Sun<br>Sustain baseline</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div style='background:rgba(255,209,102,.08);border:1px solid rgba(255,209,102,.25);
            border-radius:.9rem;padding:1rem;text-align:center'>
            <div style='font-size:1.4rem;margin-bottom:.3rem'>🟢</div>
            <div style='font-family:Space Mono,monospace;font-size:1.3rem;font-weight:700;color:#ffd166'>~2,000</div>
            <div style='font-size:.78rem;color:#e2f4f0;font-weight:600;margin:.2rem 0'>Refeed Days</div>
            <div style='font-size:.72rem;color:#7ba8a0'>Sat · Sun<br>Reset leptin, restart loss</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="info-box" style="margin-top:1rem"><strong>💡 Refeed Rule:</strong> Add 1 extra roti OR daliya OR oats. Increase carbs, NOT fat. This is science — resets leptin and hunger hormones, not a cheat day. Average weekly = ~1,780 kcal — still in solid deficit.</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["🌅 Meal 1 — 2:30 PM", "🥜 Snack — 6:30 PM", "🌙 Dinner — 9:30 PM"])

    with tab1:
        meal_cards([
            ("A","Classic Grilled Chicken Bowl",["200g chicken breast (Kilrr marinade or hung curd+garlic)","2 whole eggs + 2 egg whites","150g curd","1 banana","5 almonds","Cucumber+tomato salad with lemon+chaat masala"],"~650 kcal","~83g protein","Low-Moderate ✅","Primary rotation"),
            ("B","Spiced Egg Bhurji Plate",["3 whole eggs + 3 egg whites (bhurji: onion+tomato+capsicum)","150g curd","1 whole wheat roti","Cucumber + lemon","1 banana"],"~590 kcal","~58g protein","Low ✅","Compensate protein at dinner"),
            ("C","Paneer Bhurji Plate (replaces Mutton)",["200g paneer bhurji (tomato+capsicum+ginger+cumin)","3 egg whites (boiled)","150g curd","1 banana","5 almonds + 2 walnuts"],"~640 kcal","~67g protein","Excellent ✅✅","Best for uric acid"),
            ("D","High Protein Chicken Bowl",["200g chicken breast (garlic+ginger+turmeric)","3 whole eggs (boiled)","150g curd","1 apple","5 almonds"],"~660 kcal","~85g protein","Low-Moderate ✅","Best protein day"),
            ("E","Chicken Salad Bowl (lighter)",["200g chicken breast (shredded, grilled)","2 whole eggs + 1 egg white","100g cucumber + 50g capsicum + 1 tomato (raw)","150g curd","1 banana"],"~600 kcal","~78g protein","Low ✅","Lowest calorie, highest fibre"),
        ])
        st.markdown('<div style="display:flex;align-items:center;gap:.6rem;margin:1.2rem 0 .8rem;padding-top:.8rem;border-top:1px solid rgba(255,209,102,.2)"><div style="font-size:.7rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:#ffd166">🆕 NEW — Plateau-Breaking Options</div></div>', unsafe_allow_html=True)
        meal_cards([
            ("F","Savoury Oats Bowl 🆕",["40g rolled oats cooked in water (not milk)","3 egg whites (boiled or bhurji style)","150g curd","1 banana","Top oats with: jeera + turmeric + 50g capsicum + tomato"],"~590 kcal","~48g protein","None ✅","Best for LDL + Triglycerides"),
            ("G","Moong Dal Cheela Plate 🆕",["2 moong dal cheelas (50g soaked moong dal, grated lauki inside)","3 egg whites (boiled)","150g curd","1 banana + cucumber salad"],"~580 kcal","~52g protein","Low ✅✅","Excellent for liver + uric acid"),
            ("H","Shakshuka Plate 🆕",["3 whole eggs in tomato+capsicum+onion base (turmeric+cumin)","150g curd","1 banana","5 almonds"],"~570 kcal","~45g protein","None ✅","High lycopene, anti-inflammatory"),
            ("I","Chicken Soup Meal 🆕 (Low Day)",["150g chicken breast in thin broth (lauki+garlic+ginger+turmeric)","2 boiled eggs","150g curd","1 fruit"],"~520 kcal","~72g protein","Low ✅","Best Low Day Meal 1 option"),
        ])
    with tab2:
        st.markdown('<div class="warn-box"><strong>🚨 Almond Rule</strong> Max 5 almonds per DAY total. If Meal 1 had almonds → skip from snack.</div>', unsafe_allow_html=True)
        meal_cards([
            ("A","Seeds + Raw Veggie Bowl",["1 tbsp mixed seeds (flax+sunflower+pumpkin)","5 almonds + 2 walnuts","Raw: cucumber+capsicum+tomato (chaat masala+lemon)"],"~185 kcal","~7g protein","Low","Low-almond days only 🚨"),
            ("B","Spiced Curd Bowl",["150g curd","Grated cucumber + roasted jeera + rock salt + mint","2 walnuts"],"~160 kcal","~7g protein","None ✅✅","Lowers uric acid"),
            ("C","Roasted Makhana + Egg",["30g makhana (rock salt+black pepper+turmeric)","1 boiled egg","Green tea / black coffee (no sugar)"],"~180 kcal","~10g protein","Low ✅","Anti-inflammatory"),
            ("D","Boiled Egg + Veggie",["2 boiled eggs","100g cucumber + 50g capsicum (raw, lemon)","1 tbsp mixed seeds"],"~200 kcal","~14g protein","Low ✅","Best on low-protein Meal 1 days"),
            ("E","Banana + Curd (quick)",["1 banana","100g curd","1 tbsp mixed seeds"],"~200 kcal","~5g protein","None ✅✅","Potassium boost"),
        ])
        st.markdown('<div style="display:flex;align-items:center;gap:.6rem;margin:1.2rem 0 .8rem;padding-top:.8rem;border-top:1px solid rgba(255,209,102,.2)"><div style="font-size:.7rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:#ffd166">🆕 NEW — Plateau-Breaking Options</div></div>', unsafe_allow_html=True)
        meal_cards([
            ("F","Methi Poha + Egg 🆕",["30g poha cooked with fresh methi leaves + mustard seeds + turmeric + lemon","1 boiled egg"],"~190 kcal","~9g protein","Low ✅","Iron-boosting snack"),
            ("G","Lauki Soup + Egg 🆕 (Low Day)",["200g lauki boiled/blended: garlic+jeera+pepper+turmeric","1 boiled egg on side"],"~120 kcal","~8g protein","None ✅✅","Best low-cal day snack, liver-cooling"),
            ("H","Egg White Chaat 🆕",["4 boiled egg whites sliced","Toss: onion+tomato+cucumber+chaat masala+lemon+coriander"],"~110 kcal","~14g protein","None ✅","Zero oil, very high protein"),
        ])
    with tab3:
        st.markdown('<div class="info-box"><strong>✅ Always in dinner:</strong> Good Monk 2 sachets in curd · Turmeric+black pepper · Garlic · Lemon<br>🌱 Add 100g palak 3–4 days/week — addresses Iron Deficiency Anaemia</div>', unsafe_allow_html=True)
        meal_cards([
            ("A","Chicken + Roti + Palak 🌱",["200g chicken breast","3 egg whites + 150g curd + 2 Good Monk sachets","100g palak (garlic+mustard seeds+lemon)","100g cucumber + 1 whole wheat roti"],"~1,010 kcal","~90g protein","Low-Moderate ✅","Iron ~12mg (palak + chicken)"),
            ("B","Chicken + Mixed Veggies",["200g chicken breast","3 egg whites + 150g curd + 2 Good Monk sachets","50g capsicum + 50g beans + 150g boiled cauliflower","100g cucumber"],"~950 kcal","~85g protein","Low ✅","Veggie days"),
            ("C","Chicken + Dahi Rice (comfort)",["200g chicken breast","2 egg whites + 150g curd + 2 Good Monk sachets","60g cooked rice (dahi rice style)","Cucumber + tomato salad"],"~1,020 kcal","~78g protein","Low-Moderate","Max 1–2× per week"),
            ("D","Chicken + Palak + Veggie Combo 🌱",["200g chicken breast","4 egg whites + 150g curd + 2 Good Monk sachets","100g palak + 50g capsicum + 50g beans (lemon+garlic)","100g cucumber"],"~970 kcal","~92g protein","Low ✅","Best iron day ~14mg"),
            ("E","Paneer + Egg White Dinner 🌱",["150g paneer bhurji (tomato+capsicum+ginger)","4 egg whites + 150g curd + 2 Good Monk sachets","100g palak (garlic+lemon)","100g cucumber"],"~960 kcal","~82g protein","None ✅✅","Chicken break day"),
        ])
        st.markdown('<div style="display:flex;align-items:center;gap:.6rem;margin:1.2rem 0 .8rem;padding-top:.8rem;border-top:1px solid rgba(255,209,102,.2)"><div style="font-size:.7rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:#ffd166">🆕 NEW — Plateau-Breaking Dinners</div></div>', unsafe_allow_html=True)
        meal_cards([
            ("F","Chicken + Moong Dal + Veggies 🆕",["150g chicken breast","100g cooked moong dal (garlic+jeera+turmeric+lemon)","3 egg whites + 150g curd + Good Monk","100g lauki or bhindi sabzi + 100g cucumber"],"~980 kcal","~85g protein","Low ✅✅","Best for uric acid + liver + LDL"),
            ("G","Chicken + Chana Dal + Ragi Roti 🆕",["150g chicken breast","100g cooked chana dal","150g curd + Good Monk","1 ragi roti + 100g cucumber + 50g beetroot salad"],"~1,010 kcal","~80g protein","Low ✅","High fibre, high calcium"),
            ("H","Tikka Chicken + Chana Dal + Jowar Roti 🆕",["200g tikka-style chicken breast","80g cooked chana dal","150g curd + 2 Good Monk sachets","1 jowar roti + cucumber salad"],"~1,020 kcal","~90g protein","Low ✅","Maximum variety"),
            ("I","Chicken Soup + Daliya Khichdi 🆕 (Low Day)",["200g chicken breast in thin broth (lauki+garlic+ginger+pepper)","60g daliya khichdi (peas+carrot+jeera)","150g curd + Good Monk + cucumber"],"~900 kcal","~80g protein","Low ✅","Best for low-cal days"),
            ("J","Methi Chicken + Palak + Roti 🆕",["200g chicken cooked with 50g fresh methi leaves+onion+garlic","3 egg whites + 150g curd + Good Monk","100g palak sabzi + 1 wheat or ragi roti"],"~1,010 kcal","~92g protein","Low ✅","Iron triple hit: chicken+methi+palak"),
        ])

# ════════════════════════════════════════════════════════════════════════
# PAGE: WEEKLY PLAN
# ════════════════════════════════════════════════════════════════════════
elif page == "📅 Weekly Plan":
    st.markdown('<div class="stag">Schedule</div><div class="stitle">Weekly Rotation</div>'
                '<p class="ssub">Old week collapses below · New plateau-breaking rotation with calorie cycling is the active plan</p>', unsafe_allow_html=True)

    # PLATEAU ALERT
    st.markdown("""
    <div style='background:rgba(255,209,102,.08);border:1px solid rgba(255,209,102,.3);border-radius:1rem;
        padding:1.1rem 1.4rem;margin-bottom:1.5rem;display:flex;align-items:flex-start;gap:.9rem'>
        <div style='font-size:1.4rem;flex-shrink:0'>⚖️</div>
        <div>
            <div style='font-family:Syne,sans-serif;font-weight:800;font-size:.95rem;color:#ffd166;margin-bottom:.3rem'>
                Plateau Alert — Weight Stuck at 110.7 kg</div>
            <div style='font-size:.82rem;color:#b0a070;line-height:1.6'>
                Body adapted to same 1,850 kcal and identical food pattern. Fix: calorie cycling + maximum variety.
                <strong style='color:#ffd166'>Average weekly = ~1,780 kcal — still in solid deficit, but body can't adapt.</strong>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # OLD WEEK — collapsible
    with st.expander("📅 Old Week Diet Chart (Original — April 11) — click to expand / collapse", expanded=False):
        st.markdown('<div style="font-size:.72rem;color:#7ba8a0;margin-bottom:.8rem">Fixed 1,850 kcal daily · Same food pattern every week · Led to metabolic adaptation at 110.7 kg</div>', unsafe_allow_html=True)
        old_weekly = [
            ("Mon","🅐 Classic Chicken","🅑 Curd Bowl","🅐 Chicken+Roti+Palak 🌱",True),
            ("Tue","🅑 Egg Bhurji","🅓 Boiled Eggs","🅑 Chicken+Veggies",False),
            ("Wed","🅒 Paneer Bhurji","🅑 Curd Bowl","🅒 Chicken+Dahi Rice",False),
            ("Thu","🅐 Classic Chicken","🅒 Makhana+Egg","🅓 Chicken+Palak 🌱",False),
            ("Fri","🅓 Hi-Pro Chicken","🅐 Seeds+Veggies","🅑 Chicken+Veggies",False),
            ("Sat","🅔 Chicken Salad","🅔 Banana+Curd","🅔 Paneer+EggWhite 🌱",False),
            ("Sun","🅑 Egg Bhurji","🅓 Boiled Eggs","🅐 Chicken+Roti+Palak 🌱",False),
        ]
        cols = st.columns(7)
        for col,(day,m1,sn,dn,today) in zip(cols,old_weekly):
            with col:
                cls = "day-card today" if today else "day-card"
                st.markdown(f"<div class='{cls}'><div class='day-name'>{day}</div>"
                    f"<div class='day-meal'><strong>Meal 1</strong>{m1}</div>"
                    f"<div class='day-meal'><strong>Snack</strong>{sn}</div>"
                    f"<div class='day-meal'><strong>Dinner</strong>{dn}</div></div>", unsafe_allow_html=True)
        st.markdown('<div class="warn-box" style="margin-top:1rem"><strong>⚠️ Why this stopped working</strong>Repeating identical meals at the same calorie level every day caused metabolic adaptation. Body learned to run efficiently at exactly 1,850 kcal — weight loss stalled at 110.7 kg.</div>', unsafe_allow_html=True)

    # NEW WEEK HEADER
    st.markdown("""
    <div style='display:flex;align-items:center;gap:.8rem;margin:1.5rem 0 1rem'>
        <div style='width:3px;height:30px;background:linear-gradient(to bottom,#ffd166,#00e5c8);border-radius:2px'></div>
        <div>
            <div style='font-family:Syne,sans-serif;font-weight:800;font-size:1.15rem;color:#e2f4f0'>
                New Week Diet Chart — Active Plateau-Breaking Plan</div>
            <div style='font-size:.78rem;color:#7ba8a0'>
                Calorie cycling · Maximum food variety · Dals + new veg + new marinades · Updated April 2026</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Calorie type legend
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown('<div style="background:rgba(255,107,53,.08);border:1px solid rgba(255,107,53,.25);border-radius:.8rem;padding:.8rem;text-align:center"><div style="font-family:Space Mono,monospace;font-weight:700;color:#ff6b35;font-size:1.1rem">🔴 ~1,650</div><div style="font-size:.72rem;color:#b0ccc8;margin-top:.2rem">Low Days · Mon · Wed · Fri<br>No roti/rice at dinner</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div style="background:rgba(0,229,200,.06);border:1px solid rgba(0,229,200,.2);border-radius:.8rem;padding:.8rem;text-align:center"><div style="font-family:Space Mono,monospace;font-weight:700;color:#00e5c8;font-size:1.1rem">⭐ ~1,850</div><div style="font-size:.72rem;color:#b0ccc8;margin-top:.2rem">Normal Days · Tue · Thu<br>Standard meals</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div style="background:rgba(255,209,102,.08);border:1px solid rgba(255,209,102,.25);border-radius:.8rem;padding:.8rem;text-align:center"><div style="font-family:Space Mono,monospace;font-weight:700;color:#ffd166;font-size:1.1rem">🟢 ~2,000</div><div style="font-size:.72rem;color:#b0ccc8;margin-top:.2rem">Refeed Days · Sat · Sun<br>+1 roti or oats extra</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # New weekly grid
    new_weekly = [
        ("Mon","🔴","~1,650","🅐 Classic Chicken (1 egg less, no roti)","🅑 Curd Bowl + 2 walnuts","🅐 Chicken+Palak+Veggies (no roti) 🌱",True),
        ("Tue","⭐","~1,850","🅑 Methi Egg Bhurji + Ragi Roti + curd","🅓 Boiled Eggs+Veggies","🅒 Chicken+Moong Dal+Veggies 🫘",False),
        ("Wed","🔴","~1,650","🅒 Paneer Bhurji+Egg Whites+curd (no roti)","🅑 Spiced Curd Bowl","🅘 Chicken Soup+Daliya Khichdi 🌱",False),
        ("Thu","⭐","~1,850","🅐 Hariyali Chicken+2 eggs+curd+banana","🅒 Makhana+Egg","🅓 Chicken+Bhindi+Jowar Roti 🌱",False),
        ("Fri","🔴","~1,650","🅗 Shakshuka (3 eggs)+curd+apple","🅗 Egg White Chaat","🅑 Lemon Pepper Chicken+Palak (no roti)",False),
        ("Sat","🟢","~2,000","🅕 Savoury Oats+3 egg whites+banana","🅔 Banana+Curd+seeds","🅗 Tikka Chicken+Chana Dal+Ragi Roti 🌱",False),
        ("Sun","🟢","~2,000","🅑 Egg Curry+Jowar Roti+curd+banana","🅓 Boiled Eggs+Veggies","🅐 Ginger Garlic Chicken+Baingan+Daliya 🌱",False),
    ]
    type_colors = {"🔴":"#ff6b35","⭐":"#00e5c8","🟢":"#ffd166"}
    cols = st.columns(7)
    for col,(day,dtype,kcal,m1,sn,dn,today) in zip(cols,new_weekly):
        with col:
            tc = type_colors.get(dtype,"#7ba8a0")
            border = f"border-color:{tc}" if today else f"border-color:rgba(255,255,255,.08)"
            st.markdown(
                f"<div class='day-card' style='{border};background:#0b1e2d'>"
                f"<div class='day-name' style='color:{tc}'>{day}</div>"
                f"<div style='font-family:Space Mono,monospace;font-size:.62rem;color:{tc};margin-bottom:.5rem'>{dtype} {kcal}</div>"
                f"<div class='day-meal'><strong>Meal 1</strong>{m1}</div>"
                f"<div class='day-meal'><strong>Snack</strong>{sn}</div>"
                f"<div class='day-meal'><strong>Dinner</strong>{dn}</div>"
                f"</div>", unsafe_allow_html=True)

    st.markdown('<br><div class="info-box"><strong>🔴 Low Days rule:</strong> No roti, no rice, no dal at dinner. Protein + vegetables only. Reduce Meal 1 by 1 egg or skip roti.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><strong>🟢 Refeed Days rule:</strong> Add 1 extra roti OR 60g daliya OR 40g oats. Increase carbs NOT fat. Zero fried food, zero sugar — this is science not a cheat day.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><strong>🌱 Palak appears Mon, Thu, Fri, Sun = 4 days/week.</strong> Iron deficiency management continues. 🫘 Dal appears Tue, Wed, Thu = 3 days/week for fibre + LDL reduction.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><strong>🔄 Rotate every 2 weeks:</strong> Swap which days are Low/Normal/Refeed so the body never fully adapts again.</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='font-size:.73rem;font-weight:700;letter-spacing:.1em;color:#ff6b35;text-transform:uppercase;margin-bottom:.55rem'>❌ REMOVED</div>", unsafe_allow_html=True)
        for food, reason, when in [
            ("Prawns","Very high purine","Until UA < 6.0"),
            ("Mutton","High purine","Until UA < 6.0"),
            ("Fried food","ALT/NAFLD/Triglycerides","Permanently"),
            ("Sweetened drinks","TG + fructose → UA","Permanently"),
            ("Peanuts","Allergy","Never"),
        ]:
            st.markdown(f"<div class='r-item'><div class='ri-name'>{food} <span style='color:#ff6b35;font-size:.75rem'>{when}</span></div><div class='ri-why'>{reason}</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='font-size:.73rem;font-weight:700;letter-spacing:.1em;color:#00e5c8;text-transform:uppercase;margin-bottom:.55rem'>✅ ADDED (Plateau Update)</div>", unsafe_allow_html=True)
        for food, reason, when in [
            ("Moong/Chana Dal","Fibre + LDL + TG reduction","2–3×/week"),
            ("Methi leaves","LDL + Iron ✔️","3×/week"),
            ("Lauki/Bhindi/Baingan","New veg rotation","2–3×/week"),
            ("Ragi/Jowar roti","Iron + calcium, low GI","Replace wheat 2×/week"),
            ("Rolled oats (savoury)","Beta-glucan lowers LDL directly","2–3×/week"),
            ("Beetroot (raw salad)","Iron + anti-inflammatory","2×/week"),
        ]:
            st.markdown(f"<div class='a-item'><div class='ai-name'>{food} <span style='color:#00e5c8;font-size:.75rem'>{when}</span></div><div class='ai-why'>{reason}</div></div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# PAGE: SUPPLEMENTS
# ════════════════════════════════════════════════════════════════════════
elif page == "💊 Supplements":
    st.markdown('<div class="stag">Stack</div><div class="stitle">Supplement Protocol</div>'
                '<p class="ssub">Revised post blood report · HK Vitals timing is critical for iron absorption</p>', unsafe_allow_html=True)

    supps = [
        ("🐟","Omega-3 Fish Oil","WOW Life Sciences 1300mg","2 capsules/day","9:30 PM with dinner (fat present)","Triglycerides ↓, HsCRP ↓, brain","#00e5c8","✅ Keep — critical now"),
        ("🧲","Magnesium Glycinate","Tata 1mg · 220mg elemental","1 tablet/day","1:00 AM with water","Sleep quality, insulin sensitivity","#00e5c8","✅ Keep"),
        ("🌾","Isabgol (Psyllium)","Psyllium Husk","1 tsp — NOW DAILY","11:00 PM · 350ml water","Fibre, LDL ↓, TG ↓, gut motility","#ffd166","🔼 Upgraded to DAILY"),
        ("💊","HK Vitals Multivitamin","Zinc + C + Iron complex","1 tablet/day","11:30 PM — AWAY from dairy","Iron absorption (no calcium!)","#00e5c8","✅ Keep — timing critical"),
        ("☀️","Vitamin D3","Weekly megadose","60,000 IU/week","Once weekly with fat-containing meal","68.70 nmol/L — insufficient","#00e5c8","✅ Continue"),
    ]
    cols = st.columns(3)
    for i, (icon, name, brand, dose, timing, purpose, color, status) in enumerate(supps):
        sc = "rgba(0,229,200,.1)" if color == "#00e5c8" else "rgba(255,209,102,.1)"
        bc = "rgba(0,229,200,.2)" if color == "#00e5c8" else "rgba(255,209,102,.2)"
        with cols[i % 3]:
            st.markdown(
                f"<div class='supp-card'>"
                f"<div style='font-size:1.55rem;margin-bottom:.55rem'>{icon}</div>"
                f"<div style='font-family:Syne,sans-serif;font-weight:700;font-size:.94rem;color:#e2f4f0'>{name}</div>"
                f"<div style='font-size:.73rem;color:#7ba8a0;margin-bottom:.55rem'>{brand}</div>"
                f"<div style='font-family:Space Mono,monospace;font-size:.76rem;color:#00e5c8;"
                f"background:rgba(0,229,200,.08);border-radius:.4rem;padding:.18rem .55rem;display:inline-block;margin-bottom:.4rem'>{dose}</div><br>"
                f"<div style='font-size:.73rem;color:#7ba8a0'>⏰ {timing}</div>"
                f"<div style='font-size:.76rem;color:#7ba8a0;margin-top:.45rem;padding-top:.45rem;border-top:1px solid rgba(0,229,200,.08)'>{purpose}</div>"
                f"<div style='font-size:.7rem;display:inline-block;margin-top:.4rem;padding:.18rem .6rem;"
                f"border-radius:1rem;background:{sc};color:{color};border:1px solid {bc}'>{status}</div>"
                f"</div>",
                unsafe_allow_html=True
            )

    st.markdown('<div class="warn-box"><strong>⚠️ HK Vitals Iron Absorption Rule</strong>'
                'Do NOT take near curd, milk, or any calcium-rich food. Calcium directly blocks iron absorption. '
                '11:30 PM timing ensures 2+ hours after dinner.</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# PAGE: WATER & SCHEDULE
# ════════════════════════════════════════════════════════════════════════
elif page == "💧 Water & Schedule":
    st.markdown('<div class="stag">Hydration + Timing</div><div class="stitle">Daily Schedule</div>'
                '<p class="ssub">3.5L minimum — non-negotiable for uric acid 8.53 and elevated BUN</p>', unsafe_allow_html=True)

    schedule = [
        ("1:00 PM","🍋","On Waking","Warm lemon water — ½ lemon in 300ml warm water","Uric acid flush, alkalise, kickstart digestion"),
        ("1:00–2:00 PM","💧","","2 glasses of water","Hydration post-sleep"),
        ("2:30 PM","🌅","MEAL 1","~650 kcal · ~80–85g protein · low purine","Protein loading, start of eating window"),
        ("4:00–5:00 PM","💧","","2 glasses of water","Mid-day hydration"),
        ("6:30–7:00 PM","🥜","SNACK","~170–200 kcal · Low purine","Bridge gap, prevent hunger spike"),
        ("7:00–9:00 PM","💧","","2 glasses of water","Pre-dinner hydration"),
        ("9:30 PM","🌙","DINNER","~1,000–1,020 kcal · Always Good Monk in curd","Final meal, high protein, anti-inflammatory"),
        ("11:00 PM","🌾","","Isabgol 1 tsp in 350ml water + 1 extra glass","Fibre, LDL ↓ — must take with plenty of water"),
        ("11:30 PM","💊","","HK Vitals (1 tablet) — NOT near dairy","Iron absorption, away from calcium"),
        ("1:00 AM","🧲","","Magnesium Glycinate (1 tablet) + 1 glass water","Sleep quality, insulin sensitivity"),
        ("2:00–3:00 AM","💧","","1 glass water","Overnight hydration, uric acid dilution"),
    ]
    st.markdown('<div class="tl-wrap">', unsafe_allow_html=True)
    for time, icon, label, action, purpose in schedule:
        lh = f"<span style='color:#00e5c8;font-weight:700'> — {label}</span>" if label else ""
        st.markdown(
            f"<div class='tl-item'>"
            f"<div class='tl-dot'>{icon}</div>"
            f"<div><div class='tl-time'>{time}{lh}</div>"
            f"<div class='tl-action'>{action}</div>"
            f"<div class='tl-purpose'>{purpose}</div></div>"
            f"</div>",
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box"><strong>💧 Target: 11–12 glasses = 3.3–3.6L daily</strong>'
                '300ml lemon water on waking + 10 glasses × 300ml = 3.3L minimum. Non-negotiable for uric acid 8.53 and BUN.</div>',
                unsafe_allow_html=True)

    st.markdown('<br><div class="stag">Tracker</div><div class="stitle">Water Log — Today</div>', unsafe_allow_html=True)
    wc = st.slider("Glasses today (300ml each)", 0, 12, 0)
    ml = wc * 300
    c1, c2, c3 = st.columns(3)
    c1.metric("Glasses", f"{wc}/12")
    c2.metric("Volume", f"{ml} ml")
    c3.metric("Goal", "3,500 ml", f"{ml - 3500} ml" if ml < 3500 else "✅ Done!")
    st.progress(min(ml / 3500, 1.0))
    if wc < 6:
        st.warning("⚠️ Well below target — your uric acid (8.53) and elevated BUN both need good hydration every day.")
    elif wc >= 10:
        st.success("✅ Great hydration today! Kidneys, uric acid, and BUN all benefit.")

# ════════════════════════════════════════════════════════════════════════
# PAGE: NUTRIENTS
# ════════════════════════════════════════════════════════════════════════
elif page == "📊 Nutrients":
    st.markdown('<div class="stag">Lab Report</div><div class="stitle">Nutrient Breakdown</div>'
                '<p class="ssub">Daily estimates based on updated meal plan</p>', unsafe_allow_html=True)

    nutrients = [
        ("Protein","~170–178g","175–180g","g","Near Target"),
        ("Fat","~55–62g","55–65g","g","On Target"),
        ("Omega-3 EPA+DHA","~1,800mg (supp)","250–500mg","g","Therapeutic dose"),
        ("Vitamin C","~180–200mg","65mg","g","Excellent (boosts iron)"),
        ("Potassium","~2,800–3,000mg","3,500mg","a","Improved via daily banana"),
        ("Zinc","~15–18mg","12mg","g","Covered"),
        ("Vitamin B12","~7–8 mcg","2.2 mcg","a","Low-normal — timing fix"),
        ("Iron (dietary)","~10–14mg","17mg","a","Gap — palak + HK Vitals"),
        ("Purine Load","Low-Moderate","UA target < 6.0","g","Mutton + Prawns removed"),
        ("Fibre","~22–27g","25–30g","a","Improving via isabgol daily"),
    ]

    st.markdown(
        "<div style='display:flex;justify-content:space-between;padding:.45rem .95rem;margin-bottom:.3rem'>"
        "<span style='font-size:.68rem;color:#7ba8a0;text-transform:uppercase;letter-spacing:.1em;flex:1.2'>Nutrient</span>"
        "<span style='font-size:.68rem;color:#7ba8a0;flex:1;text-align:center'>Your Intake</span>"
        "<span style='font-size:.68rem;color:#7ba8a0;flex:1;text-align:center'>Target</span>"
        "<span style='font-size:.68rem;color:#7ba8a0;min-width:140px;text-align:right'>Status</span></div>",
        unsafe_allow_html=True
    )
    for name, intake, target, bc, status in nutrients:
        dot = "✅" if bc == "g" else "⚠️"
        st.markdown(
            f"<div class='nt-row'>"
            f"<span class='nt-name'>{name}</span>"
            f"<span class='nt-val'>{intake}</span>"
            f"<span class='nt-tgt'>{target}</span>"
            f"<span class='nt-badge {bc}'>{dot} {status}</span>"
            f"</div>",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    chart_js("""
    <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.15em;color:#7ba8a0;margin-bottom:.8rem">% of daily target achieved (green ≥100%, amber 80–99%, red &lt;80%)</div>
    <canvas id="bar" height="120" role="img" aria-label="Nutrient % chart"></canvas>
    <script>new Chart(document.getElementById('bar'),{type:'bar',
      data:{labels:['Protein','Fat','Vit C','Potassium','Zinc','B12','Iron','Fibre'],
        datasets:[{label:'% of target',data:[98,93,292,83,138,345,76,88],
          backgroundColor:function(ctx){var v=ctx.raw;return v>=100?'rgba(0,229,200,.72)':v>=80?'rgba(255,209,102,.72)':'rgba(255,107,53,.72)';},
          borderRadius:6,borderSkipped:false}]},
      options:{responsive:true,plugins:{legend:{display:false},
        tooltip:{backgroundColor:'#0b1e2d',titleColor:'#00e5c8',bodyColor:'#e2f4f0',borderColor:'rgba(0,229,200,.2)',borderWidth:1,
          callbacks:{label:function(c){return c.raw+'% of target'}}}},
        scales:{x:{grid:{color:'rgba(255,255,255,.04)'},ticks:{color:'#7ba8a0',font:{size:11}}},
                y:{grid:{color:'rgba(255,255,255,.04)'},ticks:{color:'#7ba8a0',callback:function(v){return v+'%'}},max:400}}}});
    </script>""", height=320)

    st.markdown('<br><div class="stag">Rules</div><div class="stitle">Anti-Inflammatory Kitchen Rules</div>', unsafe_allow_html=True)
    for icon, rule, detail in [
        ("🟡","Turmeric + black pepper","in every cooked dish — non-negotiable daily habit"),
        ("🧄","Garlic","in every marinade and stir-fry — liver protective, anti-inflammatory"),
        ("🍋","Lemon","on all vegetables and salads — boosts iron absorption significantly"),
        ("🫚","No frying","Grill, pan-cook, boil, stir-fry with minimal oil only"),
        ("🛢️","Oil limit","Max 1 tsp (5ml) per meal — prefer dry cooking or spray"),
        ("🧂","Rock salt / pink salt","preferred over regular table salt — lower sodium"),
        ("🫛","Ginger","in bhurji and marinades when possible — anti-inflammatory"),
    ]:
        st.markdown(f"<div class='krule'><div style='font-size:1rem;flex-shrink:0'>{icon}</div><div><strong>{rule}</strong> — {detail}</div></div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# PAGE: CHECKLIST
# ════════════════════════════════════════════════════════════════════════
elif page == "✅ Checklist":
    st.markdown('<div class="stag">Daily Habits</div><div class="stitle">Daily Checklist</div>'
                '<p class="ssub">Every single one matters for your blood markers — treat these as non-negotiable</p>', unsafe_allow_html=True)

    checklist = [
        ("morning","🍋","Warm lemon water on waking (1 PM)"),
        ("morning","💧","3.5L+ water throughout the day"),
        ("morning","☀️","15 min sunlight around 1–2 PM"),
        ("meals","🟡","Turmeric + black pepper in cooking (every dish)"),
        ("meals","🧄","Garlic in at least one cooked dish"),
        ("meals","🍋","Lemon on vegetables and salad"),
        ("meals","🥜","Max 5 almonds total — NOT double-dipping Meal 1 + Snack"),
        ("meals","🍌","Banana daily (potassium + uric acid management)"),
        ("meals","🌱","Palak 3–4× this week (iron deficiency — critical)"),
        ("dinner","🦠","Good Monk 2 sachets in dinner curd"),
        ("dinner","🐟","Omega-3 with dinner"),
        ("night","🌾","Isabgol at 11 PM with full glass of water (350ml)"),
        ("night","💊","HK Vitals at 11:30 PM — AWAY from dairy"),
        ("night","🧲","Magnesium Glycinate at 1 AM"),
        ("night","💧","1 glass water overnight (2–3 AM)"),
    ]
    cats = {"morning":"🌅 Morning","meals":"🍽️ Meals","dinner":"🌙 Dinner","night":"🌑 Night"}
    cur = None
    for cat, icon, text in checklist:
        if cat != cur:
            cur = cat
            st.markdown(f"<div style='font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#00e5c8;margin:1.1rem 0 .45rem'>{cats[cat]}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chk-item'><div class='chk-dot'></div><span>{icon} {text}</span></div>", unsafe_allow_html=True)

    st.markdown('<div class="info-box" style="margin-top:1.4rem"><strong>💡 Every kg lost = ALL markers improve</strong>'
                'Fat-driven inflammation drops → uric acid falls → lipids improve → insulin sensitivity rises. '
                'The diet IS the treatment — no shortcuts needed.</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════
# PAGE: DOCTOR & RETEST
# ════════════════════════════════════════════════════════════════════════
elif page == "🏥 Doctor & Retest":
    st.markdown('<div class="stag">Medical</div><div class="stitle">Doctor Visit Checklist</div>'
                '<p class="ssub">Three conditions requiring a doctor visit — please do not skip any of them</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class='doc-item'><strong>🔴 ALT (SGPT) 95.2 U/L — Gastroenterologist visit</strong>
    Show to GP or Gastroenterologist. May need abdomen ultrasound to confirm NAFLD and check if iron supplementation should be paused.</div>
    <div class='doc-item'><strong>🔴 Uric Acid 8.53 mg/dL — Doctor consultation</strong>
    Diet alone may not be enough at this level. Medication (Febuxostat or Allopurinol) may be recommended if level doesn't drop in 4–6 weeks on diet.</div>
    <div class='doc-item'><strong>🔴 Iron Deficiency Anaemia confirmed</strong>
    Doctor may prescribe Ferrous Ascorbate or similar for faster correction than food alone can achieve.</div>
    <div class='info-box'><strong>📋 Take to appointment:</strong> Full Dr Lal PathLabs report · Lab No. 514079123 · Dated 11 April 2026</div>
    """, unsafe_allow_html=True)

    st.markdown('<br><div class="stag">Timeline</div><div class="stitle">Retest Schedule</div>', unsafe_allow_html=True)
    for when, what, target in [
        ("6 weeks — Late May 2026","Uric Acid, ALT/SGPT, Iron studies, Vitamin D","Uric acid < 7.0 · ALT trending down"),
        ("3 months — July 2026","Full lipid profile, HsCRP, B12, Vitamin D, Iron","TG < 150 · LDL < 120 · HDL > 42"),
        ("6 months — October 2026","Full panel + body composition","Weight ~98–100 kg · All markers improving"),
    ]:
        st.markdown(
            f"<div class='rt-card'>"
            f"<div class='rt-when'>📅 {when}</div>"
            f"<div class='rt-what'><strong style='color:#e2f4f0'>Test:</strong> {what}</div>"
            f"<div class='rt-tgt'>🎯 Target: {target}</div>"
            f"</div>",
            unsafe_allow_html=True
        )

    st.markdown('<br><div class="stitle">🚫 Permanently Excluded</div>', unsafe_allow_html=True)
    for food, reason, when in [
        ("Mutton","High purine","Until uric acid < 6.0 mg/dL"),
        ("Prawns","Very high purine","Until uric acid < 6.0 mg/dL"),
        ("Fried food","ALT / NAFLD / Triglycerides","Permanently avoid"),
        ("Peanuts","Allergy","Never"),
        ("Sweetened drinks / soda","TG + fructose → uric acid","Permanently avoid"),
        ("Packaged / processed food","ALT / Triglycerides / Sodium","Permanently avoid"),
    ]:
        st.markdown(
            f"<div style='display:flex;justify-content:space-between;align-items:center;padding:.65rem 1rem;"
            f"background:rgba(255,107,53,.05);border:1px solid rgba(255,107,53,.12);border-radius:.65rem;margin-bottom:.38rem'>"
            f"<span style='color:#e2f4f0;font-size:.84rem;font-weight:500'>{food}</span>"
            f"<span style='color:#7ba8a0;font-size:.76rem;text-align:center;flex:1;padding:0 1rem'>{reason}</span>"
            f"<span style='color:#ff6b35;font-size:.73rem;font-family:Space Mono,monospace'>{when}</span>"
            f"</div>",
            unsafe_allow_html=True
        )

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""<hr>
<div style='text-align:center;font-size:.73rem;color:#7ba8a0;padding:.8rem 0'>
  Plan: <span style='color:#00e5c8'>11 April 2026</span> · Dr Lal PathLabs + USDA + ICMR 2020 ·
  AI Nutritionist on Claude for <span style='color:#00e5c8'>Manmeet</span> 🎯
</div>""", unsafe_allow_html=True)
