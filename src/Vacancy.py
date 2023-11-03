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
	
	def __init__(self, name, link, salary_min, salary_max, currency, description, requirements: str):
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
		self.__currency = currency
		if not (description is None) and description.find('highlighttext'):
			for source in ('<highlighttext>', '</highlighttext>'):
				description = description.replace(source, '')
		self.__description = description if not (description is None ) else 'Не указано'

		if not (requirements is None) and requirements.find('highlighttext'):
			for source in ('<highlighttext>', '</highlighttext>'):
				requirements = requirements.replace(source, '')
		self.__requirements = requirements

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
			my_str += f'по договоренности, в '
		if self.__salary_min != 0:
			my_str += f'от {self.__salary_min} '
		if self.__salary_max != 0:
			my_str += f'до {self.__salary_max} '
		if 'RUR' in self.__currency or 'rub' in self.__currency:
			my_str += 'руб.'
		else:
			my_str += self.__currency.lstrip()
		my_str += '\n'
		my_str += f'Описание: {self.__description}\n'
		if self.__requirements != '' and not (self.__requirements is None):
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
