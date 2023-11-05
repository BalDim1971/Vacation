##############################################################################################################
'''
Файл с сервисными функциями.

1. Функция записи файла с проверкой пути: save_one_file
2. Тестирование наличия файлов предыдущих запросов: test_files
3. Выбор источника получения данных, интернет или из файла: internet_or_file
4. Определить, с какой платформой, hh или sj, работать: get_platforms
5. Функция получения данных от пользователя user_interaction
'''
##############################################################################################################

from config import my_files
import os
import json


def test_data_in_name_file(name_file_par: str, name_dir: str = 'data') -> str:
	'''
	Функция проверки имени файла на содержание в нем строки name_dir.

	Функция принимает на вход имя файла и имя нужного каталога, по умолчанию 'data'.
	Если имя файла не содержит в пути 'data', добавляем.
	Если имя пустое, возвращаем ''.
	Параметры:
	:param name_file_par: имя файла, будет располагаться в каталоге name_dir, относительно текущего каталога
	:param name_dir: имя подкаталога

	:return: новое или старое имя файла, или '', если имя файла пустое?
	'''
	
	pass


def save_one_file(name_file_par: str, json_data):
	'''
	Функция для записи файла с проверкой наличия пути.
	
	Функция принимает на вход имя файла и данные для записи, json-формат
	Если имя файла не содержит в пути 'data', добавляем.
	Если имя пустое, возвращаем -1.
	Параметры:
	:param name_file_par: имя файла, будет располагаться в каталоге data, относительно текущего каталога
	:param json_data: данные для записи
	
	:return: -1, если передали пустое значение
	'''
	
	if name_file_par is None or len(name_file_par) == 0:
		return -1
	
	name_file = name_file_par
	path_list = name_file.split(os.sep)
	if len(path_list) == 0:
		return -1
	
	if not ('data' in path_list):
		name_file = os.path.join('data', name_file_par)
	
	if not os.path.exists('data'):
		name_file = os.path.join('..', name_file)
	
	with open(name_file, "w", encoding='utf-8') as f:
		json.dump(json_data, f, indent=4, ensure_ascii=False)


def load_one_file(name_file_par: str) -> str:
	'''
	Функция для чтения файла в json формате с проверкой пути.
	
	Функция принимает на вход имя файла.
	Если имя файла не содержит в пути 'data', добавляем.
	Если имя пустое, возвращаем ''.
	Параметры:
	:param name_file_par: имя файла, будет располагаться в каталоге data, относительно текущего каталога
	:return: прочитанные из файла данные строка, или пусто
	'''
	
	if name_file_par is None or len(name_file_par) == 0:
		return ''
	
	name_file = name_file_par
	path_list = name_file.split(os.sep)
	if len(path_list) == 0:
		return ''
	
	if not ('data' in path_list):
		name_file = os.path.join('data', name_file_par)
	
	if not os.path.exists('data'):
		name_file = os.path.join('..', name_file)
	name_file = os.path.join('data', name_file_par)
	if not os.path.exists('data'):
		name_file = os.path.join('..', name_file)
	
	with open(name_file, "r", encoding='utf-8') as f:
		json_data = json.load(f)
	
	return json_data


def test_files():
	'''
	Проверка наличия файлов с необработанным списком вакансий с сайта.

	Функция проверяет наличие файла с ранее запрошенными данными вакансий с сайта.
	В случае наличия хотя бы одного файла, функция возвращает соответствующий ответ.
	
	:return: 1 - наличие файла hh_file_vacantions, 2 - sj_file_vacantions, 3 - оба файла есть
	0 - нет файлов
	'''
	
	count_files = 0
	for i in range(2):
		name_file = my_files[i]
		
		# Нет каталога, пробуем подняться на уровень выше
		if not os.path.exists('data'):
			name_file = os.path.join('..', name_file)
		
		# Проверяем наличие файла по списку
		if not os.path.exists(name_file) or not os.path.isfile(name_file):
			continue
		
		count_files += (i + 1)
	
	return count_files


def internet_or_file(count_files):
	'''
	Функция запрашивает у пользователя, откуда берем данные.
	На выбор: интернет, файлы (при наличии) или оба варианта/
	
	На входе:
	count_files - количество файлов: 1 - hh, 2 - sj, 3 - оба варианта
	:return: 1 - интернет, 2 - файл, 0 - завершение работы
	'''
	
	# Есть хотя бы один файл
	if count_files > 0:
		print(f'В наличии есть файлы:')
		if count_files in (1, 3):
			print(f'с данными с сайта hh.ru {my_files[0]}')
		if count_files in (2, 3):
			print(f'с данными с сайта superjob.ru {my_files[1]}')
		
		# Запросить, откуда берем данные: из интернета или из файла ранее загруженного
		print('\nЗапрашиваем данные из интернета или обрабатываем файлы?')
		print('1 - работаем с интернетом')
		print('2 - работаем с файлами')
		print('0 - прекращение работы скрипта')
		my_work = int(input('Введите 1, 2 или 0 и нажмите Enter: '))
		return my_work
	
	return 1


def get_platforms(count_files, my_work):
	'''
	Запрашиваем платформы для получения данных
	
	На входе:
	:param count_files: наличие файлов, 1(hh), 2(sj), 3(оба файла)
	:param my_work: откуда берем данные: 1 - интернет, 2 - файл
	:return: условный номер платформ: 1(hh), 2(sj), 3(обе вместе)
	'''
	
	# Запросить платформы hh, superjob или обе
	if my_work == 1:
		print('\nВыберите платформы для получения вакансий:')
		print('1 - HeadHunter (hh.ru)')
		print('2 - SuperJob (superjob.ru)')
		print('3 - обе платформы')
		print('0 - прекращение работы скрипта')
		my_choice = int(input('Введите 1,2,3 или 0 и нажмите Enter: '))
	else:
		if count_files in (1, 2):
			print(f'\nВ наличии только {my_files[count_files - 1]}')
			input('Для продолжения нажмите Enter')
			return count_files
		
		print('\nВыберите источники информации:')
		print(f'1 - HeadHunter {my_files[0]}')
		print(f'2 - SuperJob {my_files[1]}')
		print('3 - оба файла')
		print('0 - прекращение работы скрипта')
		my_choice = int(input('Введите 1,2,3 или 0 и нажмите Enter: '))
	
	return my_choice


def user_interaction():
	'''
	Функция взаимодействия с пользователем.
	Получаем данные для запросов.

	1. Проверяем наличие файлов с предыдущего запроса
	2. Работаем с файлами или интернетом
	3. Запрос: с каких платформ получать данные.
	4. Ключевое слово для поиска в интернете.
	3. Количество профессий для вывода в топ по зарплате.
	4. Отсортированные вакансии, по какому ключу? и сколько?
	5. Получить вакансии по ключевым словам?
	6. Дать возможность удалить определенные вакансии

	:return: Введенные для поиска и отображения данные в виде кортежа(?)
	'''
	
	# Инициируем переменные
	my_keyword = ''
	
	# Проверяем наличие файлов с предыдущим запросом
	count_files = test_files()
	
	# Получаем откуда берем данные
	# Должно вернуть 1(интернет), 2(файлы) или 0
	my_work = internet_or_file(count_files)
	if my_work == 0:
		return 0
	
	# Пытаемся получить платформу с которой работаем
	# Должно вернуть 1(hh), 2(sj), 3(hh+sj) или 0
	my_choice = get_platforms(count_files, my_work)
	if my_choice == 0:
		return 0
	
	# Если работаем с интернетом, запрашиваем ключевое слово для поиска
	if my_work == 1:
		my_keyword = input('Введите ключевое слово для поиска: ')
	
	# Количество вывода в топ по зарплате
	my_top = int(input('Введите количество вакансий для вывода в топ по зарплате N: '))
	
	# Ключевые слова для фильтрации вакансий
	print('\nВведите ключевые слова для фильтрации вакансий, через пробел')
	filter_words = input("Ключевые слова: ").split()
	
	print('\n')
	
	# Вернуть введенные данные
	return my_choice, my_keyword, my_top, my_work, filter_words

##############################################################################################################
