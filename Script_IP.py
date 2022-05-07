# Вычисление данных по IP для termux version 1

import requests
# импорт библиотеки для работы с большим шрифтом в консоли
from pyfiglet import Figlet
# Сохранение Карты
#import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(response)

        # Получение данных из json()
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[AS]': response.get('as'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        #area = folium.Map(location=[response.get('lat'), response.get('lon')])
        #area.save(f'{response.get("query")}_{response.get("country")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Проблема с соединением!')


def main():
    # Создание красивого шрифта

    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))

    ip = input('Введите IP: ')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()