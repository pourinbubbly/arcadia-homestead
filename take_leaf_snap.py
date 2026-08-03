import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1280,1000')

driver = webdriver.Edge(options=options)
driver.get('http://localhost:8080')
time.sleep(1)

# Scroll to sticky showcase section to trigger leaf wipe transition
driver.execute_script("window.scrollTo(0, 1500);")
time.sleep(0.1) # capture mid-leaf wipe!
driver.save_screenshot('C:\\Users\\user\\.gemini\\antigravity\\scratch\\arc-pixel-farm\\screenshot_leaf_sweep_mid.png')
driver.quit()
print("Saved screenshot_leaf_sweep_mid.png!")
