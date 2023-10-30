##########################################################################################################
'''
Файл описывает класс доступа к API сайта hh.ru
'''
##########################################################################################################

from AbstractAPI import AbstractAPI
from data.config import hh_file_vacantions, hh_url


class HeadHunterAPI(AbstractAPI):
	'''
	Класс реализует доступ через API к сайту с вакансиями hh.ru
	'''
	
	def __init__(self):
		'''
		Инициируем класс доступа к hh.ru
		'''
		
		super().__init__(hh_url, hh_file_vacantions)
		self.params = ['text', 'python']

	def get_vacancies(self, name_work: str):
		'''
		Возвращает список вакансий.

		:return: Список полученных с сайта вакансий
		'''

		self.params = ['text', name_work]
		super().get_vacancies()

##########################################################################################################
