from utils import get_vacancies, create_database, save_data_to_database
from config import config
from class_DBManager import DBManager


def main():
    employers_id = {'Тинькоф': '78638',
                    'Ozon': '2180',
                    'МТС': '3776',
                    'СБЕР': '3529',
                    'Газпромбанк': '3388',
                    '2ГИС': '64174',
                    'VK': '15478',
                    'Ростелеком': '2748',
                    'Эр-Телеком': '44272',
                    'Калашников': '981'}

    params = config()

    create_database('hh_emploe', params)

    print("Поиск вакансий от работодателей 'Тинькоф', 'Ozon', 'МТС', 'СБЕР', "
          "'Газпромбанк', '2ГИС', 'VK', 'Ростелеком', 'Эр-Телеком', 'Калашников' ОЖИДАЙТЕ....")

    for employer_name, employers_id in employers_id.items():
        vacancies = get_vacancies(employers_id)
        save_data_to_database(employers_id, employer_name, vacancies, 'hh_emploe', params)

    class_db = DBManager('hh_emploe', params)

    word = input("Введите поисковое слово по вакансиям  ")
    vacancy_list = class_db.get_vacancies_with_keyword(word)
    for vacancy in vacancy_list:
        print(vacancy)
    print(f"Нашлось {len(vacancy_list)} вакансий")


if __name__ == '__main__':
    main()
