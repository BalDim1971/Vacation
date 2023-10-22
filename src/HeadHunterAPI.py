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
		
		r = requests.get(self.url)
		print(r.content.decode('utf-8'))


##########################################################################################################
