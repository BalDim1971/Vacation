#########################################################
'''
Модуль инициации констант.

Инициируем константы:
 - для адресов сайтов, с которых берем вакансии
 - для имен файлов для записи вакансий, формат json
'''
#########################################################

import os
from typing import Tuple

hh_url = 'https://api.hh.ru/vacancies'
sj_url = 'https://api.superjob.ru/2.0/vacancies'

hh_file_vacantions = os.path.join('data', 'hh_vacancy.json')
sj_file_vacantions = os.path.join('data', 'sj_vacancy.json')
my_files: tuple[str, str] = (hh_file_vacantions, sj_file_vacantions)

#########################################################