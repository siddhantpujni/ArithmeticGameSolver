from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setting up web drive
driver = webdriver.Chrome(executable_path="C:\Users\pujni\Downloads\chrome-win64\chrome-win64")

# Open webpage
driver.get('https://arithmetic.zetamac.com/')

# Loading the page
time.sleep(2)

# Starting the game
start_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="Start"]')
start_button.click()

# Loading the page
time.sleep(2)

# Interacting with test elements
question_element = driver.find_element(By.CLASS_NAME, "problem")
answer_input = driver.find_element(By.CLASS_NAME, "answer")

# Loop to solve multiple questions

while True:    
    question = question_element.text
    
    answer = eval(question)
    
    answer_input.clear()
    answer_input.send_keys(str(answer))
    
    time.sleep(0.5)
