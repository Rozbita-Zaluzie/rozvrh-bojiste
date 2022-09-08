from pydoc import classname
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

from day import days_to_json

className = "A2b"



browser = webdriver.Chrome()
url = ('https://aplikace.skolaonline.cz/SOL/PublicWeb/SOSaG/KWE009_RozvrhTridy.aspx')
browser.get(url)

select = Select(browser.find_element("id",'DDLTrida'))
select.select_by_visible_text(className)
browser.find_element("id", "btnZobrazit").click()
html_source = browser.page_source

soup = BeautifulSoup(html_source, 'html.parser')
table = soup.find(id="CCADynamicCalendarTable")

days = table.find_all('tr')
filterdays = []
for d in days:
    if d.get('class') != None:
        filterdays.append(d)

contin = False
for d in range(len(filterdays)):
    if contin:
        contin = False
        continue

    if d+1 < len(filterdays):
        next = filterdays[d+1]

        if next.find_all('td')[0].get('class') == ['DctCellBottom', 'DctCell']:
            days_to_json(className, filterdays[d].find_all('td'), next.find_all('td'))
            contin = True
        else:
            days_to_json(className ,filterdays[d].find_all('td')) 
    else:
        days_to_json(className, filterdays[d].find_all('td')) 
        
        
    
