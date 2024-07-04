from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# print(doc.select('.heading-50-black')[0].contents)
# print(doc.select('.heading-50-black.color-black'))

courses = doc.select('.heading-50-black.color-black')
for course in courses:
    print(course.contents[0].strip())
