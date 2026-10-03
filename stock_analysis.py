import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(ticker, start_date, end_date):
    """Extrai dados históricos de um ativo utilizando a API do Yahoo Finance."""
    print(f"A extrair dados para {ticker}...")
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

def calculate_technical_indicators(df):
    """Calcula Médias Móveis (SMA), RSI e Volatilidade."""
    data = df.copy()
    
    # 1. Médias Móveis Simples (SMA - 20 e 50 períodos)
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    # 2. Volatilidade Histórica (Retornos Logarítmicos Anualizados)
    data['Log_Ret'] = np.log(data['Close'] / data['Close'].shift(1))
    data['Volatility_252d'] = data['Log_Ret'].rolling(window=252).std() * np.sqrt(252)
    
    # 3. Relative Strength Index (RSI - 14 períodos)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI_14'] = 100 - (100 / (1 + rs))
    
    # Remove as linhas iniciais com valores nulos resultantes do cálculo das janelas
    return data.dropna()

if __name__ == "__main__":
    # Execução do Pipeline para a Petrobras (PETR4.SA)
    ticker_symbol = "PETR4.SA"
    
    # Extração de dados
    raw_data = get_stock_data(ticker_symbol, "2023-01-01", "2024-01-01")
    
    # Processamento e Engenharia de Recursos
    processed_data = calculate_technical_indicators(raw_data)
    
    print("\n--- Amostra dos Dados Processados ---")
    print(processed_data[['Close', 'SMA_20', 'RSI_14', 'Volatility_252d']].tail())
    print("\nPipeline executado com sucesso. Indicadores quantitativos calculados.")
