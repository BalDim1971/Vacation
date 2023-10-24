##########################################################################################################
'''
Файл описывает класс доступа к API сайта superjob.ru
'''
##########################################################################################################

from AbstractAPI import AbstractAPI
import requests
import os

class SuperJobAPI(AbstractAPI):
	'''
	Класс реализует доступ через API к сайту с вакансиями superjob.ru
	'''
	
	def __init__(self):
		'''
		Инициируем класс доступа к superjob.ru
		'''
		
		super().__init__('https://api.superjob.ru/2.0/vacancies')
		
		# API_KEY скопирован из гугла и вставлен в переменные окружения
		self.app_id: str = os.getenv('APP_ID_SUPERJOB')
		self.secret_key: str = os.getenv('API_KEY_SUPERJOB')
		
		self.headers = {
			"X-Api-App-Id": self.secret_key,
		}
		
		self.params = {
			"count": 100,
			"page": 0,
			"keyword": "python",
			"archive": False,
		}
		
	def get_vacancies(self):
		'''
		Получение списка вакансий с сайта
		:return:
		'''
		
		r = requests.get(self.url, headers=self.headers, params=self.params).json()
		return r
		

##########################################################################################################
