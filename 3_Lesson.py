from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1',27017)
db = client['vacancies_db_new']

vacancies = db.vacancies
#users = db.users

vacancies.insert_many([{'vacancy_name': 'Математик-аналитик (data scientist / data analyst)',
                    'salary_max': None,
                    'salary_min': 85000,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/38349035?query=data%20analyst'},

                    {'vacancy_name': 'Инженер-аналитик (data science)',
                    'salary_max': None,
                    'salary_min': None,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/39066212?query=data%20analyst'},

                    {'vacancy_name': 'Data Analyst',
                    'salary_max': None,
                    'salary_min': None,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/38674359?query=data%20analyst'},

                    {'vacancy_name': 'Data аналитик',
                    'salary_max': None,
                    'salary_min': None,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/38768830?query=data%20analyst'},

                    {'vacancy_name': 'Data Analyst',
                    'salary_max': None,
                    'salary_min': None,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/38720713?query=data%20analyst'}])


vacancies.insert_many([{'vacancy_name': 'Аналитик данных (Data Analyst)',
                    'salary_max': 140000,
                    'salary_min': 140000,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/38740056?query=data%20analyst'},

                    {'vacancy_name': 'Аналитик/Data scientist',
                    'salary_max': None,
                    'salary_min': 70000,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/38598935?query=data%20analyst'},

                    {'vacancy_name': 'Data analyst',
                    'salary_max': None,
                    'salary_min': 130000,
                    'site': 'hh.ru',
                    'vacancy_link': 'https://spb.hh.ru/vacancy/38642159?query=data%20analyst'}])


for vacancy in vacancies.find({}, {'salary_max':0}):
    pprint(vacancy)

for vacancy in vacancies.find({}).sort('salary_min',-1).limit(3):
    pprint(vacancy)

print(vacancies.count_documents({'salary_max':None}))