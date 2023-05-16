from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for the emulator
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '5.1',
    'appPackage': 'com.google.android.googlequicksearchbox',
    'appActivity': 'com.google.android.launcher.GEL',
    'automationName': 'UiAutomator2'
}

# Appium server connection details
appium_server = 'http://localhost:4723/wd/hub'

# Initialize the Appium driver
driver = webdriver.Remote(appium_server, desired_caps)

# Wait for the Chrome app to launch
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.android.chrome:id/terms_accept')))

# Accept terms and conditions
terms_accept_btn = driver.find_element(MobileBy.ID, 'com.android.chrome:id/terms_accept')
terms_accept_btn.click()

# Wait for the sign-in page to load
wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.android.chrome:id/signin_promo')))
sign_in_btn = driver.find_element(MobileBy.ID, 'com.android.chrome:id/signin_promo')
sign_in_btn.click()

# Wait for the sign-in form to load
wait.until(EC.presence_of_element_located((MobileBy.ID, 'identifierId')))
email_field = driver.find_element(MobileBy.ID, 'identifierId')
email_field.send_keys('your_email@gmail.com')

# Proceed to the next step
next_btn = driver.find_element(MobileBy.ID, 'identifierNext')
next_btn.click()

# Wait for the password field to load
wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//input[@type="password"]')))
password_field = driver.find_element(MobileBy.XPATH, '//input[@type="password"]')
password_field.send_keys('your_password')

# Sign in
sign_in_btn = driver.find_element(MobileBy.ID, 'passwordNext')
sign_in_btn.click()

# Wait for the account to be signed in
wait.until(EC.presence_of_element_located((MobileBy.ID, 'gb')))
print('Successfully logged into Google account')

# Perform any additional actions or operations as needed

# Quit the driver and close the session
driver.quit()
