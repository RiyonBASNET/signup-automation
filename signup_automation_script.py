from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firstname = "Ram"
lastname="Bahadur"
email="ram.bahadur@email.com"
phoneNumber = 9818181818
password="R@M1bahadur"
confirmPassword="R@M1bahadur"

options = Options()
options.add_argument("--start-maximized")
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


try:

    driver.get("https://authorized-partner.vercel.app/")

    WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
    )
    register_button = driver.find_element(By.XPATH,"//a[@href='/register']")
    register_button.click()

    agree_id = "remember"
    WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.ID,agree_id))
    )
    agree_button=driver.find_element(By.ID, agree_id)
    agree_button.click()

    continue_button = driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]")
    continue_button.click()

    form_fields={
        "firstName":firstname,
        "lastName":lastname,
        "email":email,
        "phoneNumber":phoneNumber,
        "password":password,
        "confirmPassword":confirmPassword
    }

    for name,value in form_fields.items():
        input_field = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.NAME,name))
        )
        input_field.clear()
        input_field.send_keys(value)

    submit_button= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH,"//button[@type='submit']"))
    )
    submit_button.click()

    otp_input = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Verify Code')]"))
    )
    print("Verify OTP from email.")

except Exception as e:
    print(e)
    
finally:
    driver.quit()