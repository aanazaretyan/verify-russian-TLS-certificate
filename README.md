# Проверка поддержки страницами российского сертификата

В связи со случаями отказа иностранных удостоверяющих центров работать с российскими веб-приложениями, появилась
необходимость создавать УЦ, подчинённый органам власти РФ.

Программа может автоматизировать процесс контроля над веб-приложениями, чтобы отслеживать, какие веб-приложения из
списка имеют риски лишиться защищённого соединения.

### Возможности

* Проверка поддержки российского сертификата
* Контроль изменений статуса поддержки

### Использование

1) Активировать виртуальное окружение (опционно)
2) Установить зависимости

```
>> pip install -r requirements.txt
```

3) В файл sample.xlsx вписать все названия компаний и URL-адреса
4) Запустить программу

```
>> python3 main.py
```

### Возможности парсера xml

1) Напротив названия организации вписывается ссылка на ресурс

<table>
    <thead>
        <th>Организация</th>
        <th>Ссылка</th>
    </thead>
    <tbody>
        <tr>
            <td valign="middle"  align="center">Яндекс</td>
            <td valign="middle"  align="center">ya.ru</td>
        </tr>
    </tbody>
</table>

2) В ячейке со ссылками можно вписывать ссылки через запятую:

<table>
    <thead>
        <th>Организация</th>
        <th>Ссылка</th>
    </thead>
    <tbody>
        <tr>
            <td valign="middle"  align="center">Яндекс</td>
            <td valign="middle"  align="center">ya.ru, yandex.ru</td>
        </tr>
    </tbody>
</table>

3) Ссылки могут быть и с "https://", и с "http://" (http:// изменится на https://), и без них.

<table>
    <thead>
        <tr>
            <th>Организация</th>
            <th>Ссылка</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td valign="middle"  align="center">Яндекс</td>
            <td valign="middle"  align="center">https://ya.ru, yandex.ru</td>
        </tr>
        <tr>
            <td valign="middle"  align="center">Вконтакте</td>
            <td valign="middle"  align="center">https://vk.ru</td>
        </tr>
    </tbody>
</table>

4) Ячейку для названия компании можно представить в виде объединённой с несколькими строками

<table>
    <thead>
        <tr>
            <th>Организация</th>
            <th>Ссылка</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=2 valign="middle"  align="center">Яндекс</td>
            <td valign="middle"  align="center">https://ya.ru</td>
        </tr>
        <tr>
            <td valign="middle"  align="center">yandex.ru</td>
        </tr>
        <tr>
            <td valign="middle"  align="center">Вконтакте</td>
            <td valign="middle"  align="center">https://vk.ru</td>
        </tr>
    </tbody>
</table>