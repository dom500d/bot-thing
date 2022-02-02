from selenium import webdriver
import csv
import time
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
del rows[0]

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
url = 'https://www.ebay.com'


def search(keyword):
	driver.get(url)
	searchBar = driver.find_element(By.NAME, '_nkw')
	searchBar.send_keys(keyword)
	searchBar.send_keys('\n')
	pageInfo = []
	# try:
		# # wait for search results to be fetched
		# WebDriverWait(driver, 10).until(
		# EC.presence_of_element_located((By.CLASS_NAME, "s_item"))
		# )
	# except Exception as e:
		# print(e)
		# driver.quit()
		# exit()
	time.sleep(2)
	#amount = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[2]/div[1]/div[1]/h1')
	#print(amount)
	searchResults = driver.find_elements(By.CLASS_NAME, 's-item--watch-at-corner')
	#count = 0
	
	for result in searchResults:
		# if(amount[0] > 0 and (count-1) == amount[0]):
			# break
		element = result.find_element_by_css_selector('a') 
		link = element.get_attribute('href')
		header = result.find_element_by_css_selector('h3').text
		price = result.find_element(By.CLASS_NAME, 's-item__price').text
		pageInfo.append({
			'Name' : header, 'Link' : link, 'Price': price
		})
		#count += 1
	del pageInfo[0]
	return pageInfo
fields = ['Name', 'Link', 'Price']	
for row in rows:
	pageInfo = search(row[1])
	filename = row[1] + '.csv'
	with open(filename, 'w') as csvfile:
		try:
			write = csv.DictWriter(csvfile, fieldnames = fields)
			write.writeheader()
			write.writerows(pageInfo)
		except Exception as e:
			print(e)

