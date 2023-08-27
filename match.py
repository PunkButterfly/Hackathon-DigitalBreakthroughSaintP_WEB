import streamlit as st
import requests
import json


def get_response(inputs, url='http://158.160.21.26:8503/query'):
    payload = {"objects": inputs}
    response = requests.post(url, data=json.dumps(payload)).json()
    #
    status = response['success']
    if not status:
        return "Empty result"

    queries = response['query']
    result_list = response['result']  # [sorted_top_for_query_1, sorted_top_for_query_2 ...]

    return status, queries, result_list


st.set_page_config(page_title="", layout="wide")

st.header('Поиск адреса')

input_addresses = st.text_input(label='Введите адрес или список адресов через ";"', value='', max_chars=150)

if input_addresses:

    input_addresses = input_addresses.split(';')

    response_status, queries, relevant_addresses = get_response(input_addresses)

    # st.selectbox(label='Выберите адрес', options=relevant_addresses, index=0)

    for input, output in zip(input_addresses, relevant_addresses):
        st.write(input)
        st.table(output)
