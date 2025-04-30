import streamlit as st
import requests
import json

st.write('# Welcome to *Crypto Price Checker*!!😁')
st.write('# ***Nikolas Zannettou***')

crypto_chosen = st.text_input('Enter a Cryptocurrency (i.e. BTC)')
st.write(f'User input crypto: {crypto_chosen}')

fiat_chosen = st.text_input('Enter a Currency (i.e. USD)')
st.write(f'User input currency: {fiat_chosen}')

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'cf5878ea-2d18-4411-87c9-45cc33b53b61',
}

if crypto_chosen and fiat_chosen:
    response = requests.get(f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={crypto_chosen.upper()}&convert={fiat_chosen.upper()}', headers=headers)

    if response.status_code in [200, 201]:
        data = response.json()

        if 'data' in data and crypto_chosen.upper() in data['data']:
            crypto_price = data['data'][crypto_chosen.upper()][0]['quote'][fiat_chosen.upper()]['price']
            crypto_name = data['data'][crypto_chosen.upper()][0]['name']
            st.write(f"The current price of {crypto_name} is **{crypto_price:.2f} {fiat_chosen.upper()}**.")
            threshold_value = st.number_input('Set your target price', min_value=0.0, step=100.0)

            if st.button('Notify me!'):
                st.write(f"We will notify you when the price of {crypto_name} reaches {threshold_value:.2f} {fiat_chosen.upper()}!")
        else:
            st.error("Invalid crypto symbol or missing data.")


