##########################################################################################################
'''
Файл описывает класс доступа к API сайта superjob.ru
'''
##########################################################################################################

from AbstractAPI import AbstractAPI
import requests
import os
from data.config import sj_file_vacantions, sj_url


class SuperJobAPI(AbstractAPI):
	'''
	Класс реализует доступ через API к сайту с вакансиями superjob.ru
	'''
	
	def __init__(self, keyword: str):
		'''
		Инициируем класс доступа к superjob.ru
		'''
		
		self.__params = {
			"count": 200,
			"page": '',
			"archive": False,
			"keyword": keyword
		}
		
		super().__init__(sj_url, sj_file_vacantions)
		
		# API_KEY скопирован из гугла и вставлен в переменные окружения
		self.app_id: str = os.getenv('APP_ID_SUPERJOB')
		self.secret_key: str = os.getenv('API_KEY_SUPERJOB')
		
		self.__headers = {
			"X-Api-App-Id": self.secret_key,
		}
	
	def get_vacancies(self):
		'''
		Получает с сайта вакансии.

		Возвращает необработанный список вакансий.

		:return: Список полученных с сайта вакансий
		'''
		
		self.json_data = requests.get(self.url, headers=self.__headers, params=self.__params).json()
		return self.json_data

##########################################################################################################
