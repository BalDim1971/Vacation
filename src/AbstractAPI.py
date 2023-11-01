##########################################################################################################
'''
Файл описывает абстрактный класс доступа к API сайтов с вакансиями
'''
##########################################################################################################

# Подключаем необходимые модули

from abc import ABC, abstractmethod
import json
import os


class AbstractAPI(ABC):
	'''
	Абстрактный класс, предоставляющий шаблон класса для создания классов доступа к сайтам с вакансиями.
	
	Содержит параметры:
	__url: str - адрес сайта вакансий
	headers - заголовок запроса для доступа к данным сайта
	params - параметры запроса
	json_data - данные, полученные с сайта, преобразованные в формат json
	__name_file: str - имя файла для сохранения данных
	'''
	
	def __init__(self, url: str, name_file: str):
		'''
		Инициируем базовый класс.
		
		Параметры:
		url: str - адрес сайта вакансий
		'''
		self.__url = url
		self.json_data = {}
		self.__name_file = name_file
		
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

	@property
	def name_file(self):
		'''
		Возвращает значение приватной переменной - имени файла
		:return: имя файла
		'''
		
		return self.__name_file
	
	@name_file.setter
	def name_file(self, name_file: str):
		'''
		Устанавливаем новое значение имени файла для сохранения данных.

		Параметр:
		name_file: str - новое имя файла
		'''
		
		self.__name_file = name_file
	
	@abstractmethod
	def get_vacancies(self):
		'''
		Абстрактный метод.
		Возвращает список вакансий.
		Должен быть переопределен в наследниках
		
		:return: Список полученных с сайта вакансий
		'''
		pass
	
	def save_vacancies(self):
		'''
		Сохранение в файл списка вакансий.

		Проверяем наличие нужного каталога, если нет, переходим на уровень выше.
		'''
		
		name_file = self.__name_file
		if not os.path.exists('data'):
			name_file = os.path.join('..', name_file)
		
		with open(name_file, "w", encoding='utf-8') as f:
			json.dump(self.json_data, f, indent=4, ensure_ascii=False)
		
	
	
##########################################################################################################
