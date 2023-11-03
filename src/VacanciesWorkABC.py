##########################################################################################################
'''
Описываем абстрактный класс работы со списком вакансий.
'''
##########################################################################################################

# Подключаем необходимые модули

from abc import ABC, abstractmethod
from typing import List, Any
import json
from src.Vacancy import Vacancy


class VacanciesWorkABC(ABC):
	'''
	Абстрактный класс работы со списком вакансий.
	
	Атрибуты:
	список вакансий;
	параметры для отображения на экран(?);
	параметры для записи в файл(?);
	файл для записи выборки(?).
	
	Методы:
	добавление вакансий в файл;
	получение данных из файла по указанным критериям:
	удаление информации о вакансиях (по каким параметрам).
	
	Дополнительно (по желанию):
	заложить возможность расширения класса для работы с другими форматами, например с CSV-, Excel- или TXT-файлом
	'''
	__vacancies: list[Vacancy]
	
	def __init__(self, name_file, params):
		'''
		Конструктор класса.
		
		:param name_file: Файл для записи отобранных вакансий
		:param params: Параметры выборки, они же отображение на экране(?)
		'''
		
		self.__vacancies = []
		self.__name_file = name_file
		self.__params = params
		self.json_data = []

	def append(self, vacancy):
		'''
		Добавляем в список одну новую вакансию
		
		:param vacancy: Новая вакансия
		:return: Себя? Или список?
		'''
		
		self.__vacancies.append(vacancy)
		
	def remove(self, vacancy):
		'''
		Удаляем из списка одну вакансию
		
		:param vacancy: Удаляемая вакансия
		:return: Себя? Или список?
		'''
		
		self.__vacancies.remove(vacancy)
		
	def add_vacancies(self, vacancies):
		'''
		Добавляем список вакансий
		
		:param vacancies: Список вакансий
		:return: Себя? Или список?
		'''
		
		self.__vacancies += vacancies
	
	def del_vacancies(self, vacancies):
		'''
		Удаляем вакансии по списку
		
		:param vacancies: Список удаляемых вакансий
		:return: Себя? Или список?
		'''
		
		for vacancy in vacancies:
			self.__vacancies.remove(vacancy)
		
	@property
	def vacancies(self):
		'''
		Возвращаем список вакансий
		
		:return: Список вакансий
		'''
		
		return self.__vacancies

	@property
	def params(self):
		'''
		Возвращаем параметры поиска

		:return: Список слов для поиска
		'''

		return self.__params

	def read_files(self):
		'''
		Прочитать файл с исходными данными вакансий в json-формате

		:return: Вернуть массив информации в json-формате
		'''

		with open(self.__name_file, "r", encoding='utf-8') as f:
			self.json_data = json.load(f)

		return self.json_data

	@abstractmethod
	def load_vacancies(self):
		'''
		Абстрактный метод.
		Читает из файла данные и возвращает список вакансий в обработанном виде.
		Должен быть переопределен в наследниках

		:return: Список вакансий в обработанном виде
		'''
		pass

##########################################################################################################
