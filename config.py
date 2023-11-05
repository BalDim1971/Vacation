#########################################################
'''
Модуль инициации констант.

Инициируем константы:
 - для адресов сайтов, с которых берем вакансии
 - для имен файлов для записи вакансий, формат json
'''
#########################################################

from typing import Tuple
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

hh_url = 'https://api.hh.ru/vacancies'
sj_url = 'https://api.superjob.ru/2.0/vacancies'

DATA_DIR = BASE_DIR.joinpath('data')
hh_file_vacantions = DATA_DIR.joinpath('hh_vacancy.json')
sj_file_vacantions = DATA_DIR.joinpath('sj_vacancy.json')

my_files: tuple[Path, ...] = (hh_file_vacantions, sj_file_vacantions)

#########################################################