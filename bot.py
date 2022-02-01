from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
file = open('med.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
	rows.append(row)
print(rows)
file.close()

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
url = 'https://www.ebay.com'


def search(keyword):
	driver.get(url)
	searchBar = driver.find_element_by_name('_nkw')
	searchBar.send_keys(keyword)
	searchBar.send_keys('\n')
	pageInfo = []
	try:
		# wait for search results to be fetched
		WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "s-item__wrapper clearfix"))
		)
	except Exception as e:
		print(e)
		driver.quit()
	searchResults = driver.find_elements_by_class_name('s-item__wrapper clearfix')
	for result in searchResults:
		element = result.find_element_by_css_selector('a') 
		link = element.get_attribute('href')
		header = result.find_element_by_css_selector('h3').text
		price = result.find_element_by_class_name('s-item__price').text        
		pageInfo.append({
			'header' : header, 'link' : link, 'price': price
		})
	return pageInfo
	
#word = rows[1] + ' for sale'
#search(word)

search(rows[1][0] + ' ' + rows[1][1])
fields = ['header', 'link', 'price']
filename = "results.csv"
with open(filename, 'w') as csvfile:
	write = csv.DictWriter(csvfile, fieldnames = fields)
	writer.writeheader()
	writer.writerows(pageInfo)