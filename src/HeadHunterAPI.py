##########################################################################################################
'''
Файл описывает класс доступа к API сайта hh.ru
'''
##########################################################################################################

import requests
from src.AbstractAPI import AbstractAPI
from config import hh_file_vacantions, hh_url


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
		
		response = requests.get(self.url, params=self.__params, timeout=10)
		response.raise_for_status()
		self.json_data = response.json()
		return self.json_data


##################################################################################################
