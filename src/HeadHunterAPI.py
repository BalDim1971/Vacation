##########################################################################################################
'''
Файл описывает класс доступа к API сайта hh.ru
'''
##########################################################################################################

import requests
from src.AbstractAPI import AbstractAPI
from data.config import hh_file_vacantions, hh_url
from src.Vacancy import Vacancy


class HeadHunterAPI(AbstractAPI):
	'''
	Класс реализует доступ через API к сайту с вакансиями hh.ru
	'''
	
	def __init__(self, keyword: str):
		'''
		Инициируем класс доступа к hh.ru
		'''
		
		self.__params = {
			"items_on_page": 200,
			"page": 0,
			"archive": False,
			"text": keyword
		}
		
		super().__init__(hh_url, hh_file_vacantions)
	
	def get_vacancies(self):
		'''
		Получает с сайта вакансии.

		:return: Список полученных с сайта вакансий в первоначальном виде
		'''
		
		self.json_data = requests.get(self.url, params=self.__params).json()
		return self.json_data

	def load_vacancies(self):
		'''
		Обрабатывает вакансии, полученные с сайта, м приводит их к стандартизованному виду.

		:return: Список вакансий в обработанном виде
		'''

		list_dict = []
		for item in self.json_data['items']:
			name = item['name']
			url_job = item['alternate_url']
			salary_from = 0
			salary_to = 0
			if not (item['salary'] is None):
				if not (item['salary']['from'] is None):
					salary_from = int(item['salary']['from'])
				if not (item['salary']['to'] is None):
					salary_to = int(item['salary']['to'])

			description = item['snippet']['responsibility']
			if not (description is None) and description.find('<highlighttext>'):
				for source in ('<highlighttext>', '</highlighttext>'):
					description = description.replace(source, '')

			requirement = item['snippet']['requirement']
			if not (requirement is None) and requirement.find('<highlighttext>'):
				for source in ('<highlighttext>', '</highlighttext>'):
					requirement = requirement.replace(source, '')

			vacancy = Vacancy(name, url_job, salary_from, salary_to, description, requirement)
			list_dict.append(vacancy)

		# for i in range(5):
		# 	print(f'{i} вакансия: \n{list_dict[i]}')
		return list_dict


##################################################################################################
