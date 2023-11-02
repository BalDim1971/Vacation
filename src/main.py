##############################################################################################################
'''
Основной запускающий файл.

Получаем от пользователя необходимые данные для поиска.
Выводим на экран полученную информацию
'''
##############################################################################################################

from SuperJobAPI import SuperJobAPI
from HeadHunterAPI import HeadHunterAPI
from service import user_interaction
from Vacancy import Vacancy


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
	
	# Основная работа с пользовательскими данными
	my_choice = user_interaction()
	if my_choice == 0:
		return

	# Создаем объекты.
	# Получаем вакансии по ключу.
	# Сохраняем вакансии.

	# Наличие выбора hh.ru
	if my_choice[0] in (1,3):
		hh_api = HeadHunterAPI(my_choice[1])
		hh_api.get_vacancies()
		hh_api.save_vacancies()
		list_dict += hh_api.load_vacancies()

	# Наличие выбора superjob.ru
	if my_choice[0] in (2,3):
		sj_api = SuperJobAPI(my_choice[1])
		sj_api.get_vacancies()
		sj_api.save_vacancies()
		list_dict += sj_api.load_vacancies()

	# Вызвать функцию отображения данных о полученной информации
	list_dict.sort(reverse=True)
	for i in range(int(my_choice[2])):
		print(list_dict[i])


if __name__ == '__main__':
	main()

##############################################################################################################