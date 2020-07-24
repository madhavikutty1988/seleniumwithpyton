from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\Tools\Python\Driver\Chrome\chromedriver.exe")
driver.get("https://tejira.tataelxsi.co.in/login.jsp")
driver.implicitly_wait(15)
#Login
driver.find_element_by_name("os_username").send_keys("madhavikutty.v")
driver.find_element_by_name("os_password").send_keys("Atlanta@1996")
driver.find_element_by_name("login").click()


driver.find_element_by_xpath("//*[@id='header-details-user-fullname']/span/span/img").click()

driver.find_element_by_xpath("//*[@id='log_out']").click()

driver.close()