from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

from app.day import days_to_json


chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)


def get_schedule(className):

    # driver setup
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH

    browser = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    url = ('https://aplikace.skolaonline.cz/SOL/PublicWeb/SOSaG/KWE009_RozvrhTridy.aspx')
    browser.get(url)


    # select class
    select = Select(browser.find_element("id",'DDLTrida'))
    select.select_by_visible_text(className)
    browser.find_element("id", "btnZobrazit").click()
    html_source = browser.page_source


    # get html
    soup = BeautifulSoup(html_source, 'html.parser')
    table = soup.find(id="CCADynamicCalendarTable")


    # get days in table
    days = table.find_all('tr')
    filterdays = []
    for d in days:
        if d.get('class') != None:
            filterdays.append(d)


    # parse days into json - finnishedDays
    fullweek = []
    contin = False
    for d in range(len(filterdays)):
        if contin:
            contin = False
            continue

        if d+1 < len(filterdays):
            next = filterdays[d+1]

            if next.find_all('td')[0].get('class') == ['DctCellBottom', 'DctCell']:
                parsedDay = days_to_json(className, filterdays[d].find_all('td'), next.find_all('td'))
                contin = True
            else:
                parsedDay = days_to_json(className ,filterdays[d].find_all('td')) 
        else:
            parsedDay = days_to_json(className, filterdays[d].find_all('td')) 
            
        fullweek.append(parsedDay)    

    return fullweek

