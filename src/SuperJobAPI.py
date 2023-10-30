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
	
	def __init__(self):
		'''
		Инициируем класс доступа к superjob.ru
		'''
		
		super().__init__(sj_url, sj_file_vacantions)
		self.params = ['keyword', 'python']

		# API_KEY скопирован из гугла и вставлен в переменные окружения
		self.app_id: str = os.getenv('APP_ID_SUPERJOB')
		self.secret_key: str = os.getenv('API_KEY_SUPERJOB')
		
		self.headers = {
			"X-Api-App-Id": self.secret_key,
		}

	def get_vacancies(self, name_work: str):
		'''
		Возвращает список вакансий.

		:return: Список полученных с сайта вакансий
		'''

		self.params = ['keyword', name_work]
		super().get_vacancies()


##########################################################################################################
