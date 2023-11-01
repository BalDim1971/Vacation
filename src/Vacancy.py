##########################################################################################################
'''
Файл описывает класс работы с одной вакансией.
'''
##########################################################################################################


class Vacancy:
	'''
	Класс работы с одной вакансией.
	
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
	
	def __init__(self, name, link, salary_min, salary_max, description, requirements):
		'''
		Инициализатор вакансий
		
		:param name: наименование вакансии
		:param link: ссылка на вакансию
		:param salary_min: минимальная зарплата
		:param salary_max: максимальная зарплата
		:param description: описание вакансии
		:param requirements: требования.
		
		Добавить id вакансии ???
		'''
		
		self.__name = name
		self.__link = link
		self.__salary_min = salary_min
		self.__salary_max = salary_max
		self.__description = description
		self.__requirements = requirements
	
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
	
	def __lt__(self, other):
		'''
		Магический метод сравнения < по минимальной зарплате
		:param other: объект это го же класса
		:return: bool
		'''
		
		return self.__salary_min < other.__salary_min
	
	def __le__(self, other):
		'''
		Магический метод сравнения <= по минимальной зарплате
		:param other: объект это го же класса
		:return: bool
		'''
		
		return self.__salary_min <= other.__salary_min
	
	def __gt__(self, other):
		'''
		Магический метод сравнения > по минимальной зарплате
		:param other: объект это го же класса
		:return: bool
		'''
		
		return self.__salary_min > other.__salary_min
	
	def __ge__(self, other):
		'''
		Магический метод сравнения >= по минимальной зарплате
		:param other: объект это го же класса
		:return: bool
		'''
		
		return self.__salary_min >= other.__salary_min
	
	def __eq__(self, other):
		'''
		Магический метод сравнения == по минимальной зарплате
		:param other: объект это го же класса
		:return: bool
		'''
		
		return self.__salary_min == other.__salary_min

##########################################################################################################
