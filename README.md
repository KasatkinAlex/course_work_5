
Программа собирает информацию о вакансиях по 10 работодателям ('Тинькоф', 'Ozon', 'МТС', 'СБЕР','Газпромбанк', '2ГИС', 
'VK', 'Ростелеком', 'Эр-Телеком', 'Калашников') и сохраняет их базу данных.

База данных имеет 2 таблицы:
employs - работодатели
vacancy - вакансии

Программы выгружает информацию из БД по действию пользователя следующую информвцию:
1 -- Получить список всех компаний и количество вакансий у каждой компании.
2 -- Получить список всех вакансий с указанием названия компании,названия вакансии и зарплаты и ссылки на вакансию.
3 -- Получить среднюю зарплату по вакансиям.
4 -- Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.
5 -- Получить список всех вакансий, в названии которых содержатся переданные Вами слово
6 -- ВЫХОД

Как использовать данный проект?
Склонировать репозиторий в IDE.
В терминале ввести команду:
git clone https://github.com/KasatkinAlex/course_work_5.git

Установить зависимости.
В терминале ввести команду:
pip install -r requirements.txt

Создать Файл database.ini с данными:
[postgresql]
host=**localhost** - хостинг вашей базы данных
user=**postgres** - имя пользователя, используемого в СУБД
password=**12345** - Ввести пароль пользователя
port=**5432** - Ввести свой порт, по умолчанию 5432

