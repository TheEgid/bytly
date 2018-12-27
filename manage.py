import os
import requests
from dotenv import load_dotenv

def make_bitlink(token, long_link):
    url = 'https://api-ssl.bitly.com//v4/bitlinks'
    headers = {'Authorization': 'Bearer ' + token}
    _input_url = {"long_url": long_link}
    response = requests.post(url, headers=headers, json=_input_url)
    if response.ok:
        bitlink = response.json()
        return bitlink['link']
    else:
        return None

def get_url_without_protokol(link):
    delimiter = '://'
    protocol = link.find(delimiter)
    return link.replace(link[0:protocol+len(delimiter)], '')

def fetch_clicks(clicks_list):
    fetch_clicks_list = [x['clicks'] for x in clicks_list]
    return sum(fetch_clicks_list)

def extract_fetch_clicks(token, bitlink):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    headers = {'Authorization': 'Bearer ' + token}
    params = {'unit': 'day',
              'units': -1
              }
    url = url + get_url_without_protokol(bitlink) + '/clicks'
    response = requests.get(url, headers=headers, params=params)
    if response.ok:
        bitlink = response.json()
        return fetch_clicks(bitlink['link_clicks'])
    else:
        return None

def stage_bitly_cooperation(token, link):
    try:
        if link.find('bit.ly') > 0:
            return extract_fetch_clicks(token, link)
        else:
            return make_bitlink(token, link)
    except():
        return None


if __name__ == '__main__':
    long_url = input("Введите ссылку: ")
    #long_url = 'http://bit.ly/2zRAPbG'
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    bitly_cooperation = stage_bitly_cooperation(TOKEN, long_url)
    if bitly_cooperation is None:
        raise ValueError('link is incorrect!')
    else:
        print(bitly_cooperation)

    # TOKEN = '4db60a4a2cb1c91038403038d07ba892a3b3fa69'
    # long_url = 'https://thebell.io/grubyj-proschet-yurista-trampa-pochemu-majkl-koen-poluchil-3-goda-tyurmy-i-shtraf-v-2-mln/'
    # long_url = input("Введите ссылку: ")
    # long_url = 'http://bit.ly/2zRAPbG'
