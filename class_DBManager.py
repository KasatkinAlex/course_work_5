import psycopg2


class DBManager:

    def __init__(self, database_name, params):
        self.conn = psycopg2.connect(dbname=database_name, **params)

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""

        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT employs.employ_name, COUNT(*) as total_vacancy
                FROM vacancy
                INNER JOIN employs USING (employ_id)
                GROUP BY employs.employ_name
                ORDER BY employs.employ_name
                """)
            employs = cur.fetchall()
            return employs

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""

        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT employs.employ_name, vacancy_name, salary, url
                FROM vacancy
                INNER JOIN employs USING (employ_id)
                ORDER BY salary DESC
                """
            )
            vacancy = cur.fetchall()
            return vacancy

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT employs.employ_name, round(AVG(salary)) as salary_avg
                FROM vacancy
                INNER JOIN employs USING (employ_id)
                WHERE salary > 0
                GROUP BY employs.employ_name
                """
            )
            vacancy = cur.fetchall()
            return vacancy

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""

        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT *   
                FROM vacancy
                WHERE salary > (SELECT AVG(salary) FROM vacancy WHERE salary > 0)
                ORDER BY salary DESC
                """
            )
            vacancy = cur.fetchall()
            return vacancy

    def get_vacancies_with_keyword(self, word):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова"""

        with self.conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT employs.employ_name, vacancy_name, salary, url, responsibility
                FROM vacancy
                INNER JOIN employs USING (employ_id)
                WHERE vacancy_name ILIKE '%{word}%'
                ORDER BY salary DESC
                """
            )
            vacancy = cur.fetchall()
            return vacancy
