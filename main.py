##############################################################################################################
'''
Основной запускающий файл.

Получаем от пользователя необходимые данные для поиска.
Выводим на экран полученную информацию
'''
##############################################################################################################

from src.SuperJobAPI import SuperJobAPI
from src.HeadHunterAPI import HeadHunterAPI
from src.service import user_interaction
from src.SuperJobVacancies import SuperJobVacancies
from src.HeadHunterVacancies import HeadHunterVacancies


def main():
	'''
	Главная функция.
	
	1. Запрашиваем у пользователя основные данные по вакансии (профессия или ключевое слово?)
	2. Создаем объекты для получения данных с сайтов.
	3. Запрос с сайта вакансий данных по пользовательскому вводу
	4. Сохранение полученных данных
	5. Создание объекта для работы с вакансиями
	6. Запрашиваем у пользователя данные по отображению вакансий
	'''
	
	# Описываем переменные
	list_dict = []
	
	# Основная работа с пользовательскими данными.
	# Возвращает кортеж с пользовательскими настройками:
	# в 0 - платформа: 1 - hh, 2 - sj, 3 - обе
	# в 1 - ключевое слово для поиска в интернете, или пустое
	# в	2 - количество вакансий	для	ТОП
	# в 3 - источник: интернет или файл
	# в 4 - слова для фильтрации запросов
	my_choice = user_interaction()
	if my_choice == 0:
		return

	# Создаем объекты.
	# Получаем вакансии по ключу.
	# Сохраняем вакансии.

	# Наличие выбора hh.ru
	if my_choice[0] in (1,3):
		if my_choice[3] == 1:
			hh_api = HeadHunterAPI(my_choice[1])
			hh_api.get_vacancies()
			hh_api.save_vacancies()

		hh_vacancies = HeadHunterVacancies(my_choice[4])
		hh_vacancies.read_files()
		list_dict += hh_vacancies.load_vacancies()

	# Наличие выбора superjob.ru
	if my_choice[0] in (2,3):
		if my_choice[3] == 1:
			sj_api = SuperJobAPI(my_choice[1])
			sj_api.get_vacancies()
			sj_api.save_vacancies()

		sj_vacancies = SuperJobVacancies(my_choice[4])
		sj_vacancies.read_files()
		list_dict += sj_vacancies.load_vacancies()

	# Вызвать функцию отображения данных о полученной информации
	list_dict.sort(reverse=True)
	count_vacancies = len(list_dict) if len(list_dict) < my_choice[2] else my_choice[2]
	print(f'По вашему запросу {my_choice[1]} {", ".join(my_choice[4])}')
	print(f'найдено {count_vacancies} вакансий')
	for i in range(count_vacancies):
		print(list_dict[i])


if __name__ == '__main__':
	main()

##############################################################################################################