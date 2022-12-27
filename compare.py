import os
import typing


def is_report_in_directory() -> bool:
    if os.listdir('reports').remove('.gitkeep'):
        return True
    else:
        return False


def get_last_report_name() -> str:
    os_files = os.listdir('reports')
    files = []
    for file in os_files:
        files.append(f'reports/{file}')
    return max(files, key=os.path.getctime)


def compare(old_report: typing.Dict[str, typing.Dict[int, str]],
            new_report: typing.Dict[str, typing.Dict[int, str]]) -> typing.Dict[str, typing.Dict[int, str]]:
    new_report['Изменения'] = {}

    for i in range(len(new_report['Ссылка'])):
        if new_report['Ссылка'][i] in old_report['Ссылка'].values():
            index = list(old_report['Ссылка'].keys())[
                list(old_report['Ссылка'].values()).index(new_report['Ссылка'][i])
            ]
            if new_report['Статус'][i] == old_report['Статус'][index]:
                new_report['Изменения'][i] = ''
            else:
                new_report['Изменения'][i] = new_report['Статус'][i]
        else:
            new_report['Изменения'][i] = 'Новый ресурс'

    return new_report
