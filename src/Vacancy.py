##########################################################################################################
'''
Файл описывает класс работы с одной вакансией.
'''
##########################################################################################################

from dataclasses import dataclass, field


@dataclass(order=True)
class Vacancy:
	'''
	Класс работы с одной вакансией.
	
	Атрибуты:
	name: str - название вакансии
	link: str - ссылка (адрес?) вакансии
	salary_min: int -минимальная зарплата
	salary_max: int - максимальная зарплата
	Доделать (возможно):
	переделать на: salary: {} - из трех(?) элементов: минимум, максимум, средняя (?)
	Добавить id вакансии ???
	
	currency: str - валюта
	description: str - краткое описание
	requirements: str - требования
	
	Возможно к атрибутам добавить что-то еще.
	
	Методы:
	сравнение по зарплате
	проверка данных (с какими значениями?)
	'''
	
	name: str = field(compare=False)
	link: str = field(compare=False)
	salary_min: int
	salary_max: int = field(compare=False)
	currency: str = field(compare=False)
	description: str = field(compare=False)
	requirements: str = field(compare=False)
	
	def __post_init__(self):
		'''
		Обработка после инициализации.
		
		На всякий случай проверяем строки на highlighttext и убираем при наличии
		'''
		
		if not (self.description is None) and self.description.find('highlighttext'):
			for source in ('<highlighttext>', '</highlighttext>'):
				self.description = self.description.replace(source, '')
		self.description = self.description if not (self.description is None) else 'Не указано'
		
		if not (self.requirements is None) and self.requirements.find('highlighttext'):
			for source in ('<highlighttext>', '</highlighttext>'):
				self.requirements = self.requirements.replace(source, '')
	
	def __str__(self) -> str:
		'''
		Магический метод.

		Возвращаем строку с данными по вакансии.
		Формируется "красивый" вывод
		:return -> str: строка с данными вакансии.
		Требуется доработать для корректного вывода зарплат
		'''
		
		my_str = f'Наименование вакансии: {self.name}\n'
		my_str += f'Ссылка на вакансию: {self.link}\n'
		my_str += f'Зарплата: '
		if self.salary_min == 0 and self.salary_max == 0:
			my_str += f'по договоренности, в '
		if self.salary_min != 0:
			my_str += f'от {self.salary_min} '
		if self.salary_max != 0:
			my_str += f'до {self.salary_max} '
		if 'RUR' in self.currency or 'rub' in self.currency:
			my_str += 'руб.'
		else:
			my_str += self.currency.lstrip()
		my_str += '\n'
		my_str += f'Описание: {self.description}\n'
		if self.requirements != '' and not (self.requirements is None):
			my_str += f'Требования: {self.requirements}\n'
		
		return my_str

##########################################################################################################
