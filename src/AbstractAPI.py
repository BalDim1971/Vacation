##########################################################################################################
'''
Файл описывает абстрактный класс доступа к API сайтов с вакансиями
'''
##########################################################################################################

from abc import ABC


class AbstractAPI(ABC):
	'''
	Абстрактный класс, предоставляющий шаблон класса для создания классов доступа к сайтам с вакансиями
	'''
	
	def __init__(self, url: str):
		'''
		Инициируем базовый класс.
		
		Параметры:
		url: str - адрес сайта вакансий
		'''
		self.__url = url
		self.headers = {}
		self.params = {}
		self.json_data = {}
		self.name_file = ''
		
	@property
	def url(self):
		'''
		Возвращает значение приватной переменной - адреса сайта
		:return: адрес сайта
		'''
		
		return self.__url
	
	@url.setter
	def url(self, url: str):
		'''
		Устанавливаем новое значение адреса сайта.
		
		Параметр:
		url: str - новый адрес
		'''
		
		self.__url = url
	
	def get_vacancies(self):
		return self.json_data
	
	def save_vacancies(self):
		pass

##########################################################################################################
