##########################################################################################################
'''
Файл описывает абстрактный класс работы с вакансиями.
'''
##########################################################################################################

# Подключаем необходимые модули
from abc import ABC


class AbstractVacancies(ABC):
	'''
	Абстрактный класс работы с вакансиями.
	
	Атрибуты:
	name: str - название вакансии
	link: str - ссылка (адрес?) вакансии
	salary: {} - из трех(?) элементов: минимум, максимум, средняя (?)
	description: str - краткое описание
	requirements: str - требования
	
	Возможно к атрибутам добавить что-то еще.
	
	Методы:
	сравнение по зарплате
	проверка данных (с какими значениями?)
	'''
	
	def __init__(self):
		'''
		Инициализатор вакансий
		'''
		
		self.__name = ''
		self.__link = ''
		self.__salary_min = 0
		self.__salary_max = 0
		self.__description = ''
		self.__requirements = ''
		
	@property
	def __str__(self) -> str:
		'''
		Магический метод.
		
		Возвращаем строку с данными по вакансии.
		Формируется "красивый" вывод
		:return -> str: строка с данными вакансии (конкретной или всех сразу?)
		'''
		my_str = f'Наименование вакансии: {self.__name} ссылка: {self.__link}\n'
		my_str += f'Диапазон зарплат: от {self.__salary_min} до {self.__salary_max}\n'
		my_str += f'Описание: {self.__description}\n'
		my_str += f'Требования: {self.__requirements}'

		return my_str


##########################################################################################################
