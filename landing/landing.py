import streamlit as st

st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="💰",
    layout="centered"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
            background-color: #0a0a0f;
            color: #f0ede6;
        }

        .stApp {
            background: #0a0a0f;
        }

        /* Remove padding padrão */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            max-width: 900px;
        }

        /* Hero section */
        .hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            padding: 80px 20px 60px;
            position: relative;
        }

        .badge {
            display: inline-block;
            background: rgba(212, 175, 55, 0.12);
            border: 1px solid rgba(212, 175, 55, 0.3);
            color: #d4af37;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.75rem;
            font-weight: 500;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            padding: 6px 16px;
            border-radius: 100px;
            margin-bottom: 32px;
        }

        .hero-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2.8rem, 7vw, 5.5rem);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.03em;
            margin-bottom: 12px;
            color: #f0ede6;
        }

        .hero-title .accent {
            color: #d4af37;
        }

        .hero-subtitle {
            font-family: 'DM Sans', sans-serif;
            font-size: 1.15rem;
            font-weight: 300;
            color: rgba(240, 237, 230, 0.55);
            max-width: 480px;
            line-height: 1.7;
            margin-bottom: 48px;
        }

        /* Botão CTA */
        .stButton > button {
            background: #d4af37 !important;
            color: #0a0a0f !important;
            font-family: 'Syne', sans-serif !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            letter-spacing: 0.04em !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 16px 40px !important;
            cursor: pointer !important;
            transition: all 0.2s ease !important;
            text-transform: uppercase !important;
        }

        .stButton > button:hover {
            background: #f0d060 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 30px rgba(212, 175, 55, 0.35) !important;
        }

        /* Divisor */
        .divider {
            width: 100%;
            height: 1px;
            background: rgba(240, 237, 230, 0.08);
            margin: 60px 0;
        }

        /* Cards de features */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1px;
            background: rgba(240, 237, 230, 0.08);
            border: 1px solid rgba(240, 237, 230, 0.08);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 80px;
        }

        .feature-card {
            background: #0e0e16;
            padding: 32px 28px;
            transition: background 0.2s;
        }

        .feature-card:hover {
            background: #13131e;
        }

        .feature-icon {
            font-size: 1.6rem;
            margin-bottom: 16px;
            display: block;
        }

        .feature-title {
            font-family: 'Syne', sans-serif;
            font-size: 1rem;
            font-weight: 700;
            color: #f0ede6;
            margin-bottom: 8px;
        }

        .feature-desc {
            font-size: 0.875rem;
            color: rgba(240, 237, 230, 0.45);
            line-height: 1.6;
        }

        /* Stats */
        .stats-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
            margin-bottom: 80px;
            text-align: center;
        }

        .stat-number {
            font-family: 'Syne', sans-serif;
            font-size: 2.8rem;
            font-weight: 800;
            color: #d4af37;
            line-height: 1;
        }

        .stat-label {
            font-size: 0.8rem;
            color: rgba(240, 237, 230, 0.4);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-top: 6px;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 40px 0;
            color: rgba(240, 237, 230, 0.2);
            font-size: 0.8rem;
            border-top: 1px solid rgba(240, 237, 230, 0.06);
        }

        /* Esconder elementos padrão do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <span class="badge">✦ Controle Financeiro Inteligente</span>
    <div class="hero-title">
        Seus dados.<br>
        Sua <span class="accent">clareza.</span>
    </div>
    <p class="hero-subtitle">
        Visualize receitas, despesas e tendências em tempo real.
        Tome decisões com base em dados — não em achismos.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    if st.button("→ Acessar Dashboard"):
        st.switch_page("pages/dashboard.py")

# ── DIVISOR ───────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
    <div>
        <div class="stat-number">100%</div>
        <div class="stat-label">Seus dados</div>
    </div>
    <div>
        <div class="stat-number">0</div>
        <div class="stat-label">Planilhas perdidas</div>
    </div>
    <div>
        <div class="stat-number">∞</div>
        <div class="stat-label">Clareza financeira</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FEATURES ──────────────────────────────────────────
st.markdown("""
<div class="features-grid">
    <div class="feature-card">
        <span class="feature-icon">📊</span>
        <div class="feature-title">Visão Geral</div>
        <div class="feature-desc">Resumo completo de receitas e despesas em um único painel.</div>
    </div>
    <div class="feature-card">
        <span class="feature-icon">📈</span>
        <div class="feature-title">Tendências</div>
        <div class="feature-desc">Gráficos temporais para identificar padrões no seu fluxo de caixa.</div>
    </div>
    <div class="feature-card">
        <span class="feature-icon">🎯</span>
        <div class="feature-title">Categorias</div>
        <div class="feature-desc">Entenda onde cada real está sendo gasto.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Dashboard Financeiro · Feito com Streamlit
</div>
""", unsafe_allow_html=True)