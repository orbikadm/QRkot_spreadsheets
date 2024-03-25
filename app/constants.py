from datetime import datetime


LIFETIME_JWT = 3600
PASS_MIN_LEN = 3
TIME_EXAMPLE = '2024-02-19T11:51:11.389Z'
TIME_FORMAT_SHEET = "%Y/%m/%d %H:%M:%S"


def create_table_head():
    return ([
        ['Отчёт от', datetime.now().strftime(TIME_FORMAT_SHEET)],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ])


def create_table_body():
    return {
        'properties': {
            'title': f'Отчёт на {datetime.now().strftime(TIME_FORMAT_SHEET)}',
            'locale': 'ru_RU'
        },
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Лист1',
                'gridProperties': {
                    'rowCount': 100,
                    'columnCount': 11
                }
            }
        }]
    }
