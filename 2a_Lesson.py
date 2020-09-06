from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

#url = 'https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=Data+scientist&from=suggest_post'

main_link = 'https://hh.ru'
headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10/0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

response = requests.get(main_link + '/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=Data+scientist&from=suggest_post',headers=headers)

soup = bs(response.text,'html.parser')

#vacancy_block = soup.find('div',{'class':'vacancy-serp'})
#vacancy_list = vacancy_block.findChildren(recursive=False)

vacancy_list = soup.find_all('div',{'class':'bloko-gap bloko-gap_s-top bloko-gap_m-top bloko-gap_l-top'})
vacancies = []
for vacancy in vacancy_list:
    vacancy_data ={}
    vacancy_link = main_link + vacancy.find('a', class_='bloko-link HH-LinkModifier').get('href')
    vacancy_name = vacancy.find('_blank').getText()
    vacancy_salary = vacancy.find('div',{'class':'bloko-section-header-3 bloko-section-header-3_lite'})

pprint(vacancy_link)
vacancy_data['name'] = vacancy_name
vacancy_data['link'] = vacancy_link
vacancy_data['salary'] = vacancy_salary
vacancies.append(vacancy_data)
pprint(vacancies)

