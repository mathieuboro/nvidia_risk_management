import yfinance as yf

def get_data():

    samsung_krw = yf.download('005930.KS', period='6y')['Close'].squeeze()
    usd_krw = yf.download('KRW=X', period='6y')['Close'].squeeze()
    tsmc_data = yf.download('TSM', period='6y')['Close'].squeeze()

    common_index = samsung_krw.index.intersection(usd_krw.index)
    samsung_krw_filtered = samsung_krw[common_index]
    usd_krw_filtered = usd_krw[common_index]
    samsung_usd = samsung_krw_filtered / usd_krw_filtered
    samsung_usd_clean = samsung_usd.dropna()
    samsung = samsung_usd_clean

    tsmc_data.to_csv("tsmc_data.csv")
    samsung.to_csv("samsung_data.csv")