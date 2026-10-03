# 📈 Financial Market Analytics: Pipeline de Dados & Indicadores Técnicos

Pipeline analítico estruturado para extração, processamento de séries temporais e cálculo de indicadores de volatilidade e *momentum* em ativos do mercado financeiro. O projeto demonstra a integração com APIs de cotações e a construção de métricas essenciais para suporte à tomada de decisão algorítmica e gestão de portfólio.

---

### 🎯 Desafio de Negócio & Aplicação
* **Decisão Baseada em Dados:** Automatização da extração e do tratamento de grandes volumes de dados históricos (OHLCV) para identificar padrões de mercado.
* **Gestão de Risco:** Monitoramento contínuo da volatilidade histórica para calibrar estratégias de alocação de capital e gestão de risco.
* **Análise de *Momentum*:** Implementação de osciladores para detectar anomalias e zonas de exaustão de preços (sobrecompra/sobrevenda).

---

### ⚙️ Arquitetura do Pipeline Analítico
1. **Extração de Dados (Data Ingestion):**
   * Conexão com APIs financeiras (ex: `yfinance`) para captura de dados (Open, High, Low, Close, Volume) de ativos da bolsa.
2. **Processamento & Limpeza (Data Wrangling):**
   * Tratamento de valores nulos (dias não úteis), preenchimento de lacunas de cotação e alinhamento de índices de séries temporais.
3. **Engenharia de Recursos (Feature Engineering):**
   * Cálculo vetorizado de indicadores técnicos para enriquecimento da base de dados antes da fase de modelagem.

---

### 📊 Indicadores Técnicos Desenvolvidos
* **Médias Móveis (SMA & EMA):** Rastreamento de tendências através de janelas deslizantes (ex: cruzamentos de 20 e 50 períodos).
* **RSI (Relative Strength Index):** Oscilador quantitativo calibrado num limite padrão de 14 períodos para avaliar a força relativa dos movimentos.
* **Volatilidade Histórica (Retornos Logarítmicos):** Cálculo do desvio padrão anualizado, métrica fundamental para avaliação de risco financeiro.

---

### 💻 Stack Tecnológico
* **Linguagem:** Python
* **Processamento de Dados:** `Pandas`, `NumPy`
* **Extração & Visualização:** `yfinance`, `Matplotlib`, `Seaborn`

---

📫 **Desenvolvimento & Análise:** Clara Manhães — [LinkedIn](https://www.linkedin.com/in/clara-manhães-dados)
