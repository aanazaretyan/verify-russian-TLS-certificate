import requests
import pandas as pd
from datetime import datetime
import compare

xls = pd.ExcelFile('sample.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

report = {'Организация': {}, 'Ссылка': {}, 'Статус': {}}

organization = ''

for i in range(len(df['Ссылка'])):
    if str(df['Организация'][i]) != 'nan':
        organization = str(df['Организация'][i])

    links = str(df['Ссылка'][i]).replace(',', '').split(' ')
    for link in links:
        link = link.replace('http://', 'https://')

        if link.find('*.') != -1:
            link = link[link.find('*.') + 2:]
        if link.find('https://') == -1:
            link = 'https://' + link
        report['Организация'][len(report['Организация'])] = organization
        report['Ссылка'][len(report['Ссылка'])] = link
        try:
            website = requests.get(link, verify='RootCa_SSL_RSA/rootca_ssl_rsa2022.cer', timeout=5)
            report['Статус'][len(report['Статус'])] = 'Установил российский сертификат'
        except requests.exceptions.SSLError:
            report['Статус'][len(report['Статус'])] = 'НЕ установил российский сертификат'
        except requests.Timeout:
            report['Статус'][len(report['Статус'])] = 'Страница недоступна'
        except requests.exceptions.ConnectionError:
            report['Статус'][len(report['Статус'])] = 'Ошибка соединения'

if compare.is_report_in_directory():
    report['Изменения'] = {}
    old_report = pd.ExcelFile(compare.get_last_report_name())
    old_report = old_report.parse(old_report.sheet_names[0]).to_dict()
    old_report.pop('Unnamed: 0', None)

    report = compare.compare(old_report, report)

report = pd.DataFrame(report)

filename = 'reports/report_' + datetime.now().strftime("%d.%m.%Y-%H:%M:%S") + '.xlsx'

with pd.ExcelWriter(filename) as writer:
    report.to_excel(writer)
