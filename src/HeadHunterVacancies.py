##########################################################################################################
'''
Файл описывает класс получения данных для hh.ru из файла и
приведения списка вакансий к нормализованному виду
'''
##########################################################################################################

from src.VacanciesWorkABC import VacanciesWorkABC
from data.config import hh_file_vacantions
from src.Vacancy import Vacancy


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

    def load_vacancies(self):
        '''
        Обрабатывает вакансии, полученные с сайта, м приводит их к стандартизованному виду.
        Использовать параметр отбора?

        :return: Список вакансий в обработанном виде
        '''

        # Обрабатываем прочитанные данные
        for item in self.json_data['items']:
            str_item = str(item)
            count_contains = 0
            for param in self.params:
                if param.lower() in str_item.lower():
                    count_contains += 1
            if count_contains == 0:
                continue

            name = item['name']
            url_job = item['alternate_url']
            salary_from = 0
            salary_to = 0
            currency = ' RUR'
            if not (item['salary'] is None):
                if not (item['salary']['from'] is None):
                    salary_from = int(item['salary']['from'])
                if not (item['salary']['to'] is None):
                    salary_to = int(item['salary']['to'])
                if not (item['salary']['currency'] is None):
                    currency = ' ' + item['salary']['currency']

            description = item['snippet']['responsibility']
            if not (description is None) and item['snippet']['responsibility'].find('highlighttext'):
                for source in ('<highlighttext>', '</highlighttext>'):
                    description = description.replace(source, '')

            requirement = item['snippet']['requirement']
            if not (requirement is None) and item['snippet']['requirement'].find('highlighttext'):
                for source in ('<highlighttext>', '</highlighttext>'):
                    requirement = requirement.replace(source, '')

            vacancy = Vacancy(name, url_job, salary_from, salary_to, currency, description, requirement)
            self.append(vacancy)

        return self.vacancies


##########################################################################################################
