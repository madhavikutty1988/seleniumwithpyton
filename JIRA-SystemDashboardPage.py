from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\Tools\Python\Driver\Chrome\chromedriver.exe")
driver.get("https://tejira.tataelxsi.co.in/login.jsp")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element_by_name("os_username").send_keys("madhavikutty.v")
driver.find_element_by_name("os_password").send_keys("Atlanta@1996")
driver.find_element_by_name("login").click()
#Tata Elxsi Logo
TEL_ele=driver.find_element_by_xpath("//*[@id='logo']/a/img")
print("Status of Tata Elxsi Logo displayed",TEL_ele.is_displayed())
print("Status of Tata Elxsi Logo enabled",TEL_ele.is_enabled())

#Dashboard Menu
DSHBRD_ele=driver.find_element_by_xpath("//*[@id='home_link']")
print("Status of Dashboard Menu displayed",DSHBRD_ele.is_displayed())
print("Status of Dashboard Menu enabled",DSHBRD_ele.is_enabled())
driver.find_element_by_xpath("//*[@id='home_link']").click()
#Projects Menu
PRJCT_ele=driver.find_element_by_xpath("//*[@id='browse_link']")
print("Status of Projects Menu displayed",PRJCT_ele.is_displayed())
print("Status of Dashboard Menu enabled",PRJCT_ele.is_enabled())
driver.find_element_by_xpath("//*[@id='browse_link']").click()
#Issues Menu
ISSUES_ele=driver.find_element_by_xpath("//*[@id='find_link']")
print("Status of Issues Menu displayed",PRJCT_ele.is_displayed())
print("Status of Issues Menu enabled",PRJCT_ele.is_enabled())
driver.find_element_by_xpath("//*[@id='browse_link']").click()
#Boards Menu
BOARDS_ele=driver.find_element_by_xpath("//*[@id='greenhopper_menu']")
print("Status of Board Menu displayed",BOARDS_ele.is_displayed())
print("Status of Board Menu enabled",BOARDS_ele.is_enabled())
driver.find_element_by_xpath("//*[@id='greenhopper_menu']").click()
#BigPicture Menu
BGPCTR_ele=driver.find_element_by_xpath("//*[@id='bigpicture-mainMenu']")
print("Status of BigPicture Menu displayed",BGPCTR_ele.is_displayed())
print("Status of BigPicture Menu enabled",BGPCTR_ele.is_enabled())
driver.find_element_by_xpath("//*[@id='bigpicture-mainMenu']").click()
#TestsMenu
TSTS_ele=driver.find_element_by_xpath("//*[@id='qaspace-board-webitem-link']")
print("Status of Tests Menu displayed",TSTS_ele.is_displayed())
print("Status of Tests Menu enabled",TSTS_ele.is_enabled())
driver.find_element_by_xpath("//*[@id='qaspace-board-webitem-link']").click()

