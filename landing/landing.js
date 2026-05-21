export default function LandingPage() {
  return (
    <div style={styles.page}>
      <header style={styles.header}>
        <div>
          <h1 style={styles.logo}>Dashboard Financeiro</h1>
          <p style={styles.subtitle}>Controle financeiro simples e moderno</p>
        </div>

        <a
          href="https://github.com/cybercerberox/dashboard-financeiro"
          target="_blank"
          style={styles.githubButton}
        >
          GitHub
        </a>
      </header>

      <main style={styles.main}>
        <section style={styles.leftSide}>
          <div style={styles.badge}>Dashboard Inteligente</div>

          <h2 style={styles.title}>
            Visualize suas finanças de forma simples
          </h2>

          <p style={styles.description}>
            Um dashboard moderno para acompanhar receitas, despesas,
            gráficos e indicadores financeiros em um só lugar.
          </p>

          <div style={styles.cardsContainer}>
            <div style={styles.card}>
              <h3 style={styles.cardTitle}>Gráficos</h3>
              <p style={styles.cardText}>
                Visualização clara e intuitiva dos dados.
              </p>
            </div>

            <div style={styles.card}>
              <h3 style={styles.cardTitle}>Controle</h3>
              <p style={styles.cardText}>
                Gerencie receitas e despesas facilmente.
              </p>
            </div>

            <div style={styles.card}>
              <h3 style={styles.cardTitle}>Responsivo</h3>
              <p style={styles.cardText}>
                Funciona bem em computador e celular.
              </p>
            </div>
          </div>

          <div style={styles.buttonsArea}>
            <a
              href="https://dashboard-financeiro.streamlit.app"
              target="_blank"
              style={styles.primaryButton}
            >
              Ver Dashboard
            </a>

            <a
              href="https://github.com/cybercerberox/dashboard-financeiro"
              target="_blank"
              style={styles.secondaryButton}
            >
              Ver Código
            </a>
          </div>
        </section>

        <section style={styles.rightSide}>
          <div style={styles.dashboardMockup}>
            <div style={styles.mockupHeader}>
              <div style={styles.circleRed}></div>
              <div style={styles.circleYellow}></div>
              <div style={styles.circleGreen}></div>
            </div>

            <div style={styles.mockupCards}>
              <div style={styles.incomeCard}>
                <p style={styles.mockupLabel}>Receitas</p>
                <h3 style={styles.mockupValue}>R$ 12.500</h3>
              </div>

              <div style={styles.expenseCard}>
                <p style={styles.mockupLabel}>Despesas</p>
                <h3 style={styles.mockupValue}>R$ 4.200</h3>
              </div>
            </div>

            <div style={styles.chartArea}>
              <div style={{ ...styles.bar, height: '90px' }}></div>
              <div style={{ ...styles.bar, height: '140px' }}></div>
              <div style={{ ...styles.bar, height: '180px' }}></div>
              <div style={{ ...styles.bar, height: '120px' }}></div>
              <div style={{ ...styles.bar, height: '200px' }}></div>
            </div>
          </div>
        </section>
      </main>

      <footer style={st