import requests
from bs4 import BeautifulSoup
from noti import send

BASE_URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="

res = requests.get(BASE_URL)
soup = BeautifulSoup(res.content, 'html.parser')

last_updated = soup.select('div.timetable > p > span')[0].text
last_updated_month = last_updated.split('.')[0][1:]
last_updated_date = last_updated.split('.')[1]

national_data = soup.select(
    'div.regional_patient_status_A > div.rpsa_detail > div > div.open > div.mapview > ul.cityinfo > li')

national_total_cases = national_data[0].select('div > span')
national_daily_change = national_data[1].select('div > span')
national_active_cases = national_data[2].select('div > span')
national_total_recovered = national_data[3].select('div > span')
national_total_deaths = national_data[4].select('div > span')

seoul_data = soup.select('div.rpsam_graph > div > button > span')
seoul_total_cases = seoul_data[1]
seoul_daily_change = seoul_data[2]

result = f'🇰🇷COVID-19 Update🇰🇷\n' + \
    f'📆{last_updated_date}/{last_updated_month}/2020\n\n' + \
    '😷National stats\n' + \
    f'Daily change: {national_daily_change[1].text[1:-1]}\n' + \
    f'Total cases: {national_total_cases[1].text}\n' + \
    f'Total deaths: {national_total_deaths[1].text}\n\n' + \
    '😷Seoul stats\n' + \
    f'Daily change: {seoul_daily_change.text[1:-1]}\n' + \
    f'Total cases: {seoul_total_cases.text}\n'

print(result)
send(result)
