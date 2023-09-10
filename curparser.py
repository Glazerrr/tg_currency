import requests
import xml.etree.ElementTree as ET
from datetime import datetime as dt

def dateformat():
    day = str(dt.now().day) if len(str(dt.now().day)) == 2 else '0' + str(dt.now().day)
    month = str(dt.now().month) if len(str(dt.now().month)) == 2 else '0' + str(dt.now().month)
    return  day + '/' + month + '/' + str(dt.now().year)

def mainfunc(dateformat):
    adress = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + dateformat()

    response = requests.get(adress)
    if response.status_code == 200:
        xml_content = response.content

    # Парсинг XML
        root = ET.fromstring(xml_content)
        data_dict = {}  # Создаем пустой словарь

    # Находим все элементы Valute
        valute_elements = root.findall(".//Valute")
        for valute_element in valute_elements:
                data_dict[valute_element.find("Name").text] = valute_element.find("Value").text

    # Вывод словаря
        return data_dict

    else:
        return  response.status_code

