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

    while True:
        print("1 -- Получить список всех компаний и количество вакансий у каждой компании.\n"
              "2 -- Получить список всех вакансий с указанием названия компании,"
              "названия вакансии и зарплаты и ссылки на вакансию.\n"
              "3 -- Получить среднюю зарплату по вакансиям.\n"
              "4 -- Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n"
              "5 -- Получить список всех вакансий, в названии которых содержатся переданные Вами слово\n"
              "6 -- ВЫХОД\n")
        user_action = input("Введите значение действия ")
        if user_action == "1":
            vacancy_list = class_db.get_companies_and_vacancies_count()
            for vacancy in vacancy_list:
                print(vacancy)
        elif user_action == "2":
            vacancy_list = class_db.get_all_vacancies()
            for vacancy in vacancy_list:
                print(vacancy)
            print(f"Нашлось {len(vacancy_list)} вакансий")
        elif user_action == "3":
            vacancy_list = class_db.get_avg_salary()
            print("Средняя зарплата по вакансиям")
            for vacancy in vacancy_list:
                print(f"{vacancy[0]}, {str(vacancy[1])}")
        elif user_action == "4":
            vacancy_list = class_db.get_vacancies_with_higher_salary()
            for vacancy in vacancy_list:
                print(vacancy)
            print(f"Нашлось {len(vacancy_list)} вакансий")
        elif user_action == "5":
            word = input("Введите поисковое слово по вакансиям  ")
            vacancy_list = class_db.get_vacancies_with_keyword(word)
            for vacancy in vacancy_list:
                print(vacancy)
            print(f"Нашлось {len(vacancy_list)} вакансий")
        elif user_action == 6:
            break
        else:
            print("Вы ввели неправильное значение")

        user_action_while = input("\nЖелаете продолжить -- 1\n"
                                  "Выход -- любая клавиша \n"
                                  "Ваши действия --- ")
        if user_action_while != "1":
            print("Всего доброго")
            break


if __name__ == '__main__':
    main()
