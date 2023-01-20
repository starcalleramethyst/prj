from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://careers.onepeloton.com/en/all-jobs/?search=&remote=true&pagesize=100#results"
page= requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="card-job")

with open('remote-jobs.csv', 'w', encoding='utf8', newline='') as f: 
    thewriter = writer(f)
    header = ['Title', 'Department']
    thewriter.writerow(header)

    for list in lists: 
        department = list.find('span', class_="card-category").text
        title = list.find('a', class_="js-view-job").text
        info = [title, department]
        thewriter.writerow(info)