##########################################################################################################
'''
Файл описывает класс получения данных для hh.ru из файла и
приведения списка вакансий к нормализованному виду
'''
##########################################################################################################

from VacanciesWorkABC import VacanciesWorkABC
from data.config import hh_file_vacantions
from Vacancy import Vacancy


class HeadHunterVacancies(VacanciesWorkABC):
    '''
    Класс реализует получение данных для hh.ru из файла и
    приведения списка вакансий к нормализованному виду
    '''

    def __init__(self, params):
        '''
        Инициируем класс доступа к hh.ru
        '''

        super().__init__(hh_file_vacantions, params)

