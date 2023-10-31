##########################################################################################################
'''
Файл описывает класс доступа к API сайта hh.ru
'''
##########################################################################################################

from AbstractAPI import AbstractAPI
from data.config import hh_file_vacantions, hh_url


class HeadHunterAPI(AbstractAPI):
    '''
	Класс реализует доступ через API к сайту с вакансиями hh.ru
	'''

    def __init__(self, keyword: str):
        '''
		Инициируем класс доступа к hh.ru
		'''

        params = {
            "items_on_page": 200,
            "page": 0,
            "archive": False,
            "text": keyword
        }

        super().__init__(hh_url, hh_file_vacantions, params)


##########################################################################################################
