import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------
st.set_page_config(
    page_title="Dashboard Financeiro",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# CSS CUSTOMIZADO — TEMA DARK PREMIUM
# -----------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

/* ── BASE ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #E2E8F0;
}

.stApp {
    background: #0A0D14;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(99,102,241,0.15) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(20,184,166,0.10) 0%, transparent 60%);
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: rgba(15, 18, 28, 0.95) !important;
    border-right: 1px solid rgba(99,102,241,0.15);
}

[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #A5B4FC;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.5rem;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div,
[data-testid="stSidebar"] [data-baseweb="slider"] {
    background: rgba(99,102,241,0.08) !important;
    border: 1px solid rgba(99,102,241,0.20) !important;
    border-radius: 10px !important;
}

/* ── TÍTULO PRINCIPAL ── */
.dash-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 28px;
}

.dash-header h1 {
    font-size: 1.9rem;
    font-weight: 700;
    background: linear-gradient(135deg, #E2E8F0 30%, #A5B4FC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1;
}

.dash-header .badge {
    font-size: 0.68rem;
    font-family: 'DM Mono', monospace;
    background: rgba(99,102,241,0.18);
    border: 1px solid rgba(99,102,241,0.35);
    color: #A5B4FC;
    padding: 3px 10px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ── METRIC CARDS ── */
.metric-row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 14px;
    margin-bottom: 28px;
}

.metric-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 20px 18px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent);
    border-radius: 16px 16px 0 0;
}

.metric-card:hover {
    transform: translateY(-3px);
    border-color: rgba(99,102,241,0.30);
}

.metric-label {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.10em;
    color: #64748B;
    margin-bottom: 10px;
    font-weight: 500;
}

.metric-value {
    font-size: 1.55rem;
    font-weight: 700;
    color: #F1F5F9;
    font-family: 'DM Mono', monospace;
    line-height: 1;
    margin-bottom: 6px;
}

.metric-sub {
    font-size: 0.72rem;
    color: #475569;
    margin-top: 4px;
}

.metric-up   { color: #34D399; }
.metric-down { color: #F87171; }
.metric-warn { color: #FBBF24; }

/* ── CHART CARDS ── */
.chart-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 24px 20px 10px;
    margin-bottom: 20px;
}

.chart-title {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.10em;
    color: #64748B;
    font-weight: 600;
    margin-bottom: 4px;
}

/* ── DATA TABLE ── */
[data-testid="stDataFrame"] {
    border-radius: 14px !important;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.07) !important;
}

/* ── STREAMLIT OVERRIDES ── */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 18px 20px !important;
}

div[data-testid="metric-container"] label {
    font-size: 0.68rem !important;
    text-transform: uppercase;
    letter-spacing: 0.10em;
    color: #64748B !important;
}

div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 1.5rem !important;
    color: #F1F5F9 !important;
}

div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
    font-size: 0.72rem !important;
}

.stAlert {
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

h2, h3 {
    font-weight: 600;
    color: #CBD5E1;
}

/* ── SECTION DIVIDER ── */
.section-label {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #475569;
    font-weight: 600;
    margin: 28px 0 14px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.06);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# PALETA PLOTLY DARK
# -----------------------------------
PLOTLY_COLORS = ["#6366F1", "#14B8A6", "#F472B6", "#FBBF24", "#34D399", "#60A5FA"]

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color="#94A3B8", size=12),
    margin=dict(l=10, r=10, t=40, b=10),
    title_font=dict(size=13, color="#94A3B8"),
    colorway=PLOTLY_COLORS,
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        tickfont=dict(color="#475569", size=11),
        linecolor="rgba(255,255,255,0.06)"
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.04)",
        zeroline=False,
        tickfont=dict(color="#475569", size=11)
    ),
    hoverlabel=dict(
        bgcolor="#1E293B",
        bordercolor="rgba(99,102,241,0.4)",
        font=dict(family="DM Mono", color="#E2E8F0")
    )
)

# -----------------------------------
# HEADER
# -----------------------------------
st.markdown("""
<div class="dash-header">
    <h1>Dashboard Financeiro</h1>
    <span class="badge">● Ao vivo</span>
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# LEITURA DA PLANILHA
# -----------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("CLIENTESSTREAMLIT - Financeiro.csv", sep=",")
    df.columns = df.columns.str.strip().str.lower()
    df["valor"] = (
        df["valor"].astype(str).str.replace(",", ".").astype(float)
    )
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

# -----------------------------------
# SIDEBAR — FILTROS
# -----------------------------------
with st.sidebar:
    st.markdown("### 🎛️ Filtros")
    st.markdown("---")

    status = st.multiselect(
        "Status",
        options=df["status"].unique(),
        default=df["status"].unique()
    )

    empresa = st.multiselect(
        "Empresa",
        options=df["empresa"].unique(),
        default=df["empresa"].unique()
    )

    mes = st.multiselect(
        "Mês",
        options=df["mes"].unique(),
        default=df["mes"].unique()
    )

    valor_min = st.slider(
        "Valor mínimo (R$)",
        min_value=int(df["valor"].min()),
        max_value=int(df["valor"].max()),
        value=int(df["valor"].min()),
        format="R$ %d"
    )

    st.markdown("---")
    st.caption("Dashboard Financeiro v2.0")

# -----------------------------------
# FILTRAGEM
# -----------------------------------
df_filtrado = df[
    (df["status"].isin(status)) &
    (df["empresa"].isin(empresa)) &
    (df["mes"].isin(mes)) &
    (df["valor"] >= valor_min)
]

# -----------------------------------
# MÉTRICAS
# -----------------------------------
total_clientes       = len(df_filtrado)
clientes_pagantes    = len(df_filtrado[df_filtrado["status"] == "Pago"])
clientes_inadimp     = len(df_filtrado[df_filtrado["status"] == "Inadimplente"])
faturamento          = df_filtrado["valor"].sum()
ticket_medio         = df_filtrado["valor"].mean() if total_clientes > 0 else 0
taxa_inadimp         = (clientes_inadimp / total_clientes * 100) if total_clientes > 0 else 0

# -----------------------------------
# CARDS DE MÉTRICAS
# -----------------------------------
st.markdown('<div class="section-label">Visão Geral</div>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("👥 Clientes", total_clientes)
with col2:
    st.metric("✅ Pagantes", clientes_pagantes)
with col3:
    st.metric(
        "⚠️ Inadimplentes",
        clientes_inadimp,
        delta=f"-{taxa_inadimp:.1f}% da base",
        delta_color="inverse"
    )
with col4:
    st.metric(
        "💰 Faturamento",
        f"R$ {faturamento:,.0f}"
    )
with col5:
    st.metric(
        "🎯 Ticket Médio",
        f"R$ {ticket_medio:,.0f}"
    )

# -----------------------------------
# GRÁFICOS — LINHA 1
# -----------------------------------
st.markdown('<div class="section-label">Análise de Receita</div>', unsafe_allow_html=True)

col_a, col_b = st.columns([3, 2])

with col_a:
    # Evolução financeira — área preenchida com gradiente
    mes_total = (
        df_filtrado.groupby("mes")["valor"].sum().reset_index()
    )

    fig_linha = go.Figure()
    fig_linha.add_trace(go.Scatter(
        x=mes_total["mes"],
        y=mes_total["valor"],
        mode="lines+markers",
        line=dict(color="#6366F1", width=2.5, shape="spline"),
        fill="tozeroy",
        fillcolor="rgba(99,102,241,0.10)",
        marker=dict(size=7, color="#6366F1", line=dict(color="#A5B4FC", width=1.5)),
        hovertemplate="<b>%{x}</b><br>R$ %{y:,.2f}<extra></extra>"
    ))

    fig_linha.update_layout(
        **PLOTLY_LAYOUT,
        title="Evolução Financeira Mensal",
        height=280
    )

    st.plotly_chart(fig_linha, use_container_width=True)

with col_b:
    # Donut — status
    status_count = df_filtrado["status"].value_counts().reset_index()
    status_count.columns = ["status", "quantidade"]

    fig_donut = go.Figure(go.Pie(
        labels=status_count["status"],
        values=status_count["quantidade"],
        hole=0.65,
        marker=dict(colors=["#34D399", "#F87171", "#FBBF24"]),
        textinfo="percent",
        textfont=dict(size=12, color="#E2E8F0"),
        hovertemplate="<b>%{label}</b><br>%{value} clientes (%{percent})<extra></extra>"
    ))

    fig_donut.add_annotation(
        text=f"<b>{total_clientes}</b><br><span style='font-size:11px'>clientes</span>",
        x=0.5, y=0.5,
        font=dict(size=18, color="#E2E8F0", family="DM Mono"),
        showarrow=False
    )

    fig_donut.update_layout(
        **PLOTLY_LAYOUT,
        title="Status dos Clientes",
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom", y=-0.15,
            xanchor="center", x=0.5,
            font=dict(size=11, color="#94A3B8")
        ),
        height=280
    )

    st.plotly_chart(fig_donut, use_container_width=True)

# -----------------------------------
# GRÁFICOS — LINHA 2
# -----------------------------------
st.markdown('<div class="section-label">Faturamento por Empresa</div>', unsafe_allow_html=True)

empresa_total = (
    df_filtrado.groupby("empresa")["valor"].sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_barra = go.Figure(go.Bar(
    x=empresa_total["empresa"],
    y=empresa_total["valor"],
    marker=dict(
        color=empresa_total["valor"],
        colorscale=[[0, "rgba(99,102,241,0.4)"], [1, "#6366F1"]],
        line=dict(color="rgba(99,102,241,0.6)", width=0.5),
        cornerradius=6
    ),
    hovertemplate="<b>%{x}</b><br>R$ %{y:,.2f}<extra></extra>"
))

fig_barra.update_layout(
    **PLOTLY_LAYOUT,
    title="Faturamento Acumulado por Empresa",
    height=300,
    bargap=0.3
)

st.plotly_chart(fig_barra, use_container_width=True)

# -----------------------------------
# ANÁLISES AUTOMÁTICAS
# -----------------------------------
st.markdown('<div class="section-label">Insights</div>', unsafe_allow_html=True)

if not empresa_total.empty:
    maior = empresa_total.iloc[0]
    st.success(
        f"🏆 **Maior faturamento:** {maior['empresa']} — R$ {maior['valor']:,.2f}"
    )

if taxa_inadimp > 20:
    st.error(
        f"🚨 **Taxa de inadimplência crítica:** {taxa_inadimp:.1f}% dos clientes estão inadimplentes."
    )
elif taxa_inadimp > 10:
    st.warning(
        f"⚠️ **Taxa de inadimplência elevada:** {taxa_inadimp:.1f}% — atenção necessária."
    )
else:
    st.success(
        f"✅ **Taxa de inadimplência saudável:** {taxa_inadimp:.1f}%."
    )

# -----------------------------------
# TABELA DE DADOS
# -----------------------------------
st.markdown('<div class="section-label">Dados Detalhados</div>', unsafe_allow_html=True)

def colorir_status(v):
    if v == "Pago":
        return "color: #34D399; font-weight:600"
    elif v == "Inadimplente":
        return "color: #F87171; font-weight:600"
    return ""

st.dataframe(
    df_filtrado.style
    .format({"valor": "R$ {:,.2f}"})
    .map(colorir_status, subset=["status"]),
    use_container_width=True,
    height=350
)