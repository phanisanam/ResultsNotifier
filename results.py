from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

 
driver = webdriver.Chrome('D:\work\python\selenium\webdriver\chromedriver.exe') 
driver.maximize_window()

def getResults (roll_no):
 driver.get("http://www.khitguntur.com/jntuk-results/") 
 wait = WebDriverWait(driver, 600) 
 x_arg = '//a[@href="results/jntuk-bt-1-2-r16-results-may-2018.html"]'
 R16_12_Results = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
 R16_12_Results.click()

 inp_xpath = '//input[@id="ht"]'
 input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
 input_box.send_keys(roll_no+ Keys.ENTER) 

 results = wait.until(EC.presence_of_element_located(( 
	By.XPATH, "//div[@id='rs']/table/tbody/tr[2]/td[2]")))
	
 results2= wait.until(EC.presence_of_element_located(( 
	By.XPATH, "//table[@class='ui table segment']"))) 

 resultstext = driver.find_element_by_xpath("//div[@id='rs']/table").text
 #ALternate xapth:  //table[@class="ui table segment"]

 return resultstext
