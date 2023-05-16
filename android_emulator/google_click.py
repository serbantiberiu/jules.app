from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.google.android.googlequicksearchbox',
    'appActivity': 'com.google.android.launcher.GEL',
    'automationName': 'UiAutomator2'
}

# Specify the Appium server URL
appium_url = 'http://localhost:4723/wd/hub'

# Create the Appium driver with desired capabilities
driver = webdriver.Remote(appium_url, desired_caps)

# Wait for the Google application to launch
sleep(5)

# Perform a tap action on the search bar to click on it
search_bar = driver.find_element_by_id('com.google.android.googlequicksearchbox:id/search_box_input')
TouchAction(driver).tap(element=search_bar).perform()

# Wait for a while to observe the click on the search bar
sleep(5)

# Quit the driver and close the session
driver.quit()
