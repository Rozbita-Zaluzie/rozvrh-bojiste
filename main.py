from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = ('https://aplikace.skolaonline.cz/SOL/PublicWeb/SOSaG/KWE009_RozvrhTridy.aspx')
browser.get(url)

select = Select(browser.find_element("id",'DDLTrida'))
select.select_by_visible_text('E3a')
browser.find_element("id", "btnZobrazit").click()
html_source = browser.page_source

soup = BeautifulSoup(html_source, 'html.parser')
table = soup.find(id="CCADynamicCalendarTable")

days = table.find_all('tr')
filterdays = []
for d in days:
    if d.get('class') != None:
        filterdays.append(d)

for d in filterdays:
    for r in d.find_all('td'):
        print(r.get("class"))
        if r.get('class') == ['DctInnerTableType10DataTD']:
            pass
            #print(r.text)
    print("=====================================")
