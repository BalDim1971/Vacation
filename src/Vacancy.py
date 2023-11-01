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
		self.__description = description if not (description is None ) else 'Не указано'
		self.__requirements = requirements.replace('<highlighttext>','')
		self.__requirements = self.__requirements.replace('</highlighttext>','')

	# @property
	def __str__(self) -> str:
		'''
		Магический метод.
		
		Возвращаем строку с данными по вакансии.
		Формируется "красивый" вывод
		:return -> str: строка с данными вакансии.
		Требуется доработать для корректного вывода зарплат
		'''
		my_str = f'Наименование вакансии: {self.__name}\n'
		my_str += f'Ссылка на вакансию: {self.__link}\n'
		my_str += f'Зарплата: '
		if self.__salary_min == 0 and self.__salary_max == 0:
			my_str += f'по договоренности'
		if self.__salary_min != 0:
			my_str += f'от {self.__salary_min} '
		if self.__salary_max != 0:
			my_str += f'до {self.__salary_max}'
		my_str += '\n'
		my_str += f'Описание: {self.__description}\n'
		my_str += f'Требования: {self.__requirements}\n'
		
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
