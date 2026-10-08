# 📈 Pipeline de Análise de Mercado Financeiro & Indicadores Quantitativos (Python)

> Pipeline automatizado em Python para extração, tratamento e cálculo de indicadores técnicos e quantitativos de ativos da B3 (ex: PETR4), voltado para suporte à tomada de decisão em investimentos e análise de risco.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python:** Linguagem principal para desenvolvimento do pipeline.
* **Pandas & NumPy:** Manipulação, limpeza e estruturação de séries temporais financeiras.
* **APIs de Dados Financeiros (Yahoo Finance / YFinance):** Extração automatizada de dados históricos de cotações.
* **Google Colab:** Ambiente de desenvolvimento e execução em nuvem.

---

## 📊 Indicadores Calculados pelo Pipeline
* **Tendência:** Média Móvel Simples de 20 períodos (`SMA_20`).
* **Momentum:** Índice de Força Relativa de 14 períodos (`RSI_14`) para identificação de zonas de sobrecompra e sobrevenda.
* **Risco/Volatilidade:** Volatilidada <img width="654" height="220" alt="petrobras" src="https://github.com/user-attachments/assets/48ad9361-ede8-4427-8466-0ac63827e3db" />
de anualizada de 252 dias (`Volatility_252d`) para mensuração de risco do ativo.

---

## 🖼️ Demonstração da Execução do Pipeline
