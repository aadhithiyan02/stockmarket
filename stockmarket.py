# import streamlit as st
# import pandas as pd 
# from datetime import date
# import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
# from plotly import graph_objs as go
# start="2020-01-01"
# today='2023-01-01'
# st.write("CHecking if all modules work")

# stocks=("AAPL","GOOG","RSE","FDFD")
# selected=st.selectbox("select from the below",stocks)
# years=st.slider("Year of prediction:",1,4)
# period=365*years
# def load(stock):
#     data=yf.download(stock,start,today)
#     data.reset_index(inplace=True)
#     return data


# data_load_state=st.text("load data....")
# data=load('GOOG')
# data_load_state.text("Loading.......Done")

# st.subheader("Raw Data")
# st.write(data.tail(10))

# def plot_raw():
#     fig=go.Figure()
#     fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name="Plotting Raw data"))
#     fig.layout.update(title_text="Time seires",xaxis_rangeslider_visible=True)
#     st.plotly_chart(fig)
    
    
# plot_raw()


# df_train=data[['Date','Close']]
# df_train=df_train.rename(columns={"Date":"ds","Close":"y"})

# m=Prophet()
# m.fit(df_train)
# future=m.make_future_dataframe(periods=period)
# forecast=m.predict(future)
# st.subheader('Forecast Data')
# st.write(forecast.tail())

# st.write("forecast chart")
# fig1=plot_plotly(m,forecast)
# st.plotly_chart(fig1)

# st.write('components')
# fig2=m.plot_components(forecast)
# st.write(fig2)



# import streamlit as st
# import pandas as pd
# from datetime import date
# import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
# from plotly import graph_objs as go

# start = "2020-01-01"
# today = '2023-01-01'
# st.write("Checking if all modules work")

# stocks = {"AAPL": "Apple Inc.", "MSFT": "Microsoft Corporation", "GOOG": "Alphabet Inc."}
# selected_stock = st.selectbox("Select a stock", list(stocks.keys()))

# years = st.slider("Years of prediction:", 1, 4)
# period = 365 * years


# def load(stock):
#     data = yf.download(stock, start, today)
#     data.reset_index(inplace=True)
#     return data


# data_load_state = st.text("Loading data...")
# data = load(selected_stock)
# data_load_state.text("Loading data...Done")

# st.subheader("Raw Data")
# st.write(data.tail(10))


# def plot_raw():
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Plotting Raw data"))
#     fig.layout.update(title_text="Time series", xaxis_rangeslider_visible=True)
#     st.plotly_chart(fig)


# plot_raw()

# df_train = data[['Date', 'Close']]
# df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# m = Prophet()
# m.fit(df_train)
# future = m.make_future_dataframe(periods=period)
# forecast = m.predict(future)
# st.subheader('Forecast Data')
# st.write(forecast.tail())

# st.write("Forecast chart")
# fig1 = plot_plotly(m, forecast)
# st.plotly_chart(fig1)

# st.write('Components')
# fig2 = m.plot_components(forecast)
# st.write(fig2)


import streamlit as st
import pandas as pd
from datetime import date, datetime
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Get the current year
current_year = date.today().year

# Create a list of years from 2020 to the current year
years_list = list(range(2020, current_year + 1))

# User selects a start year
start_year = st.selectbox("Select a start year", years_list)

# Convert the selected start year to a string
start = f"{start_year}-01-01"

# Get the current date as today
today = date.today().strftime("%Y-%m-%d")

st.write("Checking if all modules work")

stocks = {"AAPL": "Apple Inc.", "MSFT": "Microsoft Corporation", "GOOG": "Alphabet Inc."}
selected_stock = st.selectbox("Select a stock", list(stocks.keys()))

years = st.slider("Years of prediction:", 1, 4)
period = 365 * years

def load(stock):
    data = yf.download(stock, start, today)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading data...")
data = load(selected_stock)
data_load_state.text("Loading data...Done")

st.subheader("Raw Data")
st.write(data.tail(10))

def plot_raw():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Plotting Raw data"))
    fig.layout.update(title_text="Time series", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw()

df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)
st.subheader('Forecast Data')
st.write(forecast.tail())

st.write("Forecast chart")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Components')
fig2 = m.plot_components(forecast)
st.write(fig2)
