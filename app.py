import streamlit as st
import pandas as pd
import requests
import os

access_token = os.environ.get('FITBIT_ACCESS_TOKEN')
print(access_token)
header = {'Authorization': 'Bearer {}'.format(access_token)}
res = requests.get('https://api.fitbit.com/1.2/user/-/sleep/list.json?afterDate=2022-02-17&sort=asc&limit=100&offset=0', headers=header).json()
print(res)

# def main():

#     st.title('Fitbit Dashboard')
#     return

# # if __name__ == '__main__':
# #     main()
