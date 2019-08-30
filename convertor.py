import requests

api_data = requests.get('http://www.apilayer.net/api/live?access_key=2c68e2525a5851fb8a64fe0c5d5556de&format=1')
data = api_data.json()
# print("Json formatted: \n", data, "\n\n")


def get_usd_uah():
    try:
        entered_num = float(input('Enter currency in UAH:\n'))
    except ValueError:
        entered_num = 0
        print('Incorrect input')
    rate = data['quotes']['USDUAH']
    return entered_num, rate


def exchange_to_usd(currency, rate):
    print(str(currency / rate) + ' USD')


curr, r = get_usd_uah()
exchange_to_usd(curr, r)
