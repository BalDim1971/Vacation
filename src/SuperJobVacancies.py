##########################################################################################################
'''
Файл описывает класс получения данных для superjob.ru из файла и
приведения списка вакансий к нормализованному виду
'''
##########################################################################################################

from src.VacanciesWorkABC import VacanciesWorkABC
from config import sj_file_vacantions
from src.Vacancy import Vacancy
import datetime
from src.service import save_one_file
from dataclasses import asdict


class SuperJobVacancies(VacanciesWorkABC):
    '''
    Класс реализует получение данных для hh.ru из файла и
    приведения списка вакансий к нормализованному виду
    '''

    def __init__(self, params):
        '''
        Инициируем класс доступа к hh.ru
        '''

        super().__init__(sj_file_vacantions, params)

    def load_vacancies(self):
        '''
        Обрабатывает вакансии, полученные с сайта, м приводит их к стандартизованному виду.

        :return: Список вакансий в обработанном виде
        '''

        for item in self.json_data['objects']:
            str_item = str(item)
            count_contains = 0
            for param in self.params:
                if param in str_item:
                    count_contains += 1
            if count_contains == 0:
                continue

            name = item['profession']
            url_job = item['link']
            salary_from = item['payment_from']
            salary_to = item['payment_to']
            currency = item['currency']
            description = item['candidat']
            requirement = ''
            vacancy = Vacancy(name, url_job, salary_from, salary_to, currency, description, requirement)
            self.append(vacancy)

        return self.vacancies
    
    def save_processed_vacancies_json(self):
        '''
        Записать в файл данные в обработанном виде в формате json.
        
        В файл добавить строки, по которым был сделан запрос(?).
        '''
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        name_file = 'sj_' + '_'.join(self.params) + '_' + str_current_datetime + '.json'
        
        vacancies_json = []
        for vacan in self.vacancies:
            vacancies_json.append(asdict(vacan))
        
        save_one_file(name_file, vacancies_json)

##########################################################################################################
