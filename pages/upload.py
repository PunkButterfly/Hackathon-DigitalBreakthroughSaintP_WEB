import streamlit as st
import pandas as pd
from match import get_response

st.header('Загрузите csv файл с адресами')
addresses = st.file_uploader('Сsv с колонкой "address"')

if addresses:
    addresses = pd.read_csv(addresses)

    input_addresses = addresses["address"].values.tolist()

    response_status, queries, relevant_addresses = get_response(input_addresses)

    corrected_addresses = {'address': [], 'corrected_address': [], 'corrected_building_id': []}

    for input, output in zip(input_addresses, relevant_addresses):
        corrected_addresses['address'].append(input)
        corrected_addresses['corrected_address'].append(output[0]['target_address'])
        corrected_addresses['corrected_building_id'].append(output[0]['target_building_id'])
        st.write(input)
        st.table(output)

    corrected_addresses = pd.DataFrame(corrected_addresses)

    corrected_addresses.to_csv(f'corrected_addresses.csv', header=True, sep=',', index=False, encoding='utf-8')

    with open('corrected_addresses.csv', 'rb') as f:
        st.download_button('Download CSV', f, file_name='corrected_addresses.csv')
