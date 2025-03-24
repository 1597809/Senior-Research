from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time

driver = webdriver.Chrome()

base_url = 'https://www.floodsmart.gov/historical-nfip-claims-information-and-trends'
driver.get(base_url)

os.makedirs('downloads', exist_ok=True)

data = []

year_range = range(1980, 2024)

state_select = Select(driver.find_element(By.ID, 'stateselect'))

for state_option in state_select.options:
    state_name = state_option.text

    if state_name == 'United States':
        continue

    state_select.select_by_visible_text(state_name)

    submit_button = driver.find_element(By.ID, 'submitFilters')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'submitFilters'))
    )
    submit_button.click()
        
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_element(By.ID, 'yearselectmin').find_elements(By.TAG_NAME, 'option')) > 1
    )

    year_select_min = Select(driver.find_element(By.ID, 'yearselectmin'))
    year_select_max = Select(driver.find_element(By.ID, 'yearselectmax'))

    for year_option in year_select_min.options[::-1]:
        year = year_option.text
        
        if year == 'All':
            continue

        year_select_min.select_by_visible_text(year)
        year_select_max.select_by_visible_text(year)

        time.sleep(0.1)
        
        submit_button = driver.find_element(By.ID, 'submitFilters')
        driver.execute_script("arguments[0].click();", submit_button)
        
        print(state_name, year)
        
        time.sleep(0.75)
        
        download_button = driver.find_element(By.ID, 'download_csv')
        driver.execute_script("arguments[0].click();", download_button)

driver.quit()