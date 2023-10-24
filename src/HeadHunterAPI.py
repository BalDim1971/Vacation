##########################################################################################################
'''
Файл описывает класс доступа к API сайта hh.ru
'''
##########################################################################################################

from AbstractAPI import AbstractAPI
import requests
import os


class HeadHunterAPI(AbstractAPI):
	'''
	Класс реализует доступ через API к сайту с вакансиями hh.ru
	'''
	
	def __init__(self):
		'''
		Инициируем класс доступа к hh.ru
		'''
		
		super().__init__('https://api.hh.ru/vacancies')
		
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
		# r = requests.get(self.url, params=self.params)
		#r_data = json.load(r.text)
		return r
	
	def save_vacancies(self):
		'''
		Сохраняем в файл вакансии
		:return:
		'''
		pass
		
##########################################################################################################
