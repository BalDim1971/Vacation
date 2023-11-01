##########################################################################################################
'''
Описываем абстрактный класс работы со списком вакансий.
'''
##########################################################################################################

# Подключаем необходимые модули

from abc import ABC
from typing import List, Any

from Vacancy import Vacancy


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
