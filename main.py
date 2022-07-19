from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "/Users/haelmj/variables/chromedriver"

print('Starting test')

driver = webdriver.Chrome(PATH)

def submit_form():
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div/div[1]/div/div[10]/div[1]/div/div[11]/div/div/button').click()

def find_text_elements(xpath:str, message:str):
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(message)

def find_checkboxes(xpath:str):
    driver.find_element(By.XPATH, xpath).click()

def get_page():
    if (driver.window_handles[0]):
        driver.execute_script(f"window.open('redactedurl')")
        driver.switch_to.window(driver.window_handles[-1])
    else:
        driver.get("redactedurl")
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div/div[1]/div/div[10]/div[1]/div/div[1]/div/div[1]/div/textarea')))
    element.send_keys("We are ensuring that this appplication is not easily compromised")
    find_text_elements('//*[@id="root"]/div[1]/div[1]/div/div/div/section/div/div[1]/div/div[10]/div[1]/div/div[2]/div/div[1]/div/textarea', 'Every where that thinks security')
    find_text_elements('//*[@id="root"]/div[1]/div[1]/div/div/div/section/div/div[1]/div/div[10]/div[1]/div/div[3]/div/div[1]/div/input', 'test@test.com')
    find_checkboxes('//*[@id="root"]/div[1]/div[1]/div/div/div/section/div/div[1]/div/div[10]/div[1]/div/div[5]/div/label/span')
    find_checkboxes('//*[@id="root"]/div[1]/div[1]/div/div/div/section/div/div[1]/div/div[10]/div[1]/div/div[6]/div/label/span')
    find_checkboxes('//*[@id="root"]/div[1]/div[1]/div/div/div/section/div/div[1]/div/div[10]/div[1]/div/div[7]/div/label/span')



if __name__ == '__main__':
    for i in range(20):
        get_page()
    for handle in driver.window_handles[1:]:
        driver.switch_to.window(handle)
        submit_form()