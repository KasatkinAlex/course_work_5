import requests
import psycopg2


def get_vacancies(employer_id: str) -> list:
    """ """
    vacancies_list = []
    url = f'https://api.hh.ru/vacancies?employer_id={employer_id}'
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'page': 0, 'per_page': 100}

    while params.get('page') != 10:
        response = requests.get(url, headers=headers, params=params)
        if response.ok:
            vacancies = response.json()['items']
            vacancies_list.extend(vacancies)
            params['page'] += 1
        else:
            raise ValueError("НЕТ ПОДКЛЮЧЕНИЯ К САЙТУ")
    return vacancies_list


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о работодателях и вакансиях."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f"DROP DATABASE {database_name}")
    except psycopg2.errors.InvalidCatalogName:
        cur.execute(f"CREATE DATABASE {database_name}")
    else:
        cur.execute(f"CREATE DATABASE {database_name}")
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employs(
                employ_id INT PRIMARY KEY,
                employ_name VARCHAR(255) NOT NULL
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancy (
                vacancy_id SERIAL PRIMARY KEY,
                employ_id INT REFERENCES employs(employ_id),
                vacancy_name VARCHAR NOT NULL,
                publish_date DATE,
                salary INT,
                city VARCHAR(50),
                url VARCHAR(100),
                responsibility TEXT
            )
        """)

    conn.commit()
    conn.close()


def save_data_to_database(employers_id, employer_name: str, data_vacancy: list, database_name: str, params: dict):
    """ Сохранение данных работодателей и их вакансии"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO employs (employ_id, employ_name)
            VALUES (%s, %s)
            RETURNING employ_id
            """,
            (employers_id, employer_name)
        )
        employer_id = cur.fetchone()[0]

        for vacancy in data_vacancy:
            if vacancy['salary']:
                vacancy_salary = vacancy['salary']['from']
            else:
                vacancy_salary = 0
            cur.execute(
                """
                INSERT INTO vacancy (employ_id, vacancy_name, publish_date, salary, city, url, responsibility)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (employer_id, vacancy['name'], vacancy['published_at'], vacancy_salary,
                    vacancy['area']['name'], vacancy['alternate_url'], vacancy['snippet']['responsibility'])
            )
    conn.commit()
    conn.close()
