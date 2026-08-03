import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1280,1000')

driver = webdriver.Edge(options=options)
driver.get('http://localhost:8080')
time.sleep(1)

# Scroll into showcase section
print("Scrolling to 1400px...")
driver.execute_script("window.scrollTo(0, 1400);")
time.sleep(0.5)

# Check active tab
active_tab_1 = driver.execute_script("return document.querySelector('.tab-btn.active').innerText;")
print("Active tab at 1400px:", active_tab_1)

print("Scrolling to 2000px...")
driver.execute_script("window.scrollTo(0, 2000);")
time.sleep(0.5)

active_tab_2 = driver.execute_script("return document.querySelector('.tab-btn.active').innerText;")
print("Active tab at 2000px:", active_tab_2)

print("Scrolling to 2600px...")
driver.execute_script("window.scrollTo(0, 2600);")
time.sleep(0.5)

active_tab_3 = driver.execute_script("return document.querySelector('.tab-btn.active').innerText;")
print("Active tab at 2600px:", active_tab_3)

driver.quit()
