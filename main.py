from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time,os,sqlite3
def sign():
    pwd = os.getcwd()
    db_pwd = pwd + "/ultiverse.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * FROM ultiverse;')
    rows = c.fetchall()
    count=1
    for i in rows[27:40]:
        google_email=i[4]
        secret_key = i[3].split(" ")
        address=i[1]
        print("当前循环数量 "+str(count))
        print("当前钱包地址："+str(address))
        print("当前钱包助记词："+str(secret_key))
        print("当前email："+str(google_email))

        EXTENSION_PATH = "/Users/0x024/Desktop/trade/ultiverse/tool/matemask.crx"
        WEB_DRIVER_PATH = "/Users/0x024/Desktop/trade/ultiverse/tool/chromedriver"

        opt = webdriver.ChromeOptions()
        opt.add_extension(EXTENSION_PATH)
        driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH,options=opt)
        #driver.set_window_size(height=1000,width=400)
        #driver.set_window_position(x=800, y=0)
        driver.switch_to.window(driver.window_handles[0])
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(1)
        secret_key_1 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-0"]')
        secret_key_1.send_keys(secret_key[0])
        secret_key_2 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-1"]')
        secret_key_2.send_keys(secret_key[1])
        secret_key_3 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-2"]')
        secret_key_3.send_keys(secret_key[2])
        secret_key_4 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-3"]')
        secret_key_4.send_keys(secret_key[3])
        secret_key_5 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-4"]')
        secret_key_5.send_keys(secret_key[4])
        secret_key_6 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-5"]')
        secret_key_6.send_keys(secret_key[5])
        secret_key_7 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-6"]')
        secret_key_7.send_keys(secret_key[6])
        secret_key_8 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-7"]')
        secret_key_8.send_keys(secret_key[7])
        secret_key_9 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-8"]')
        secret_key_9.send_keys(secret_key[8])
        secret_key_10 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-9"]')
        secret_key_10.send_keys(secret_key[9])
        secret_key_11 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-10"]')
        secret_key_11.send_keys(secret_key[10])
        secret_key_12 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-11"]')
        secret_key_12.send_keys(secret_key[11])
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('abcd1234')
        password_confirmation = driver.find_element(By.XPATH, '//*[@id="confirm-password"]')
        password_confirmation.send_keys('abcd1234')
        driver.find_element(By.XPATH, '//*[@id="create-new-vault__terms-checkbox"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()
        driver.switch_to.window(driver.window_handles[1])


        driver.get("https://ultiball.ultiverse.io/")
        print("click connect")
        driver.find_element(By.XPATH, '//button[text()="Connect"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[text()="MetaMask"]').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        print("switch window 2")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
        print("matemask next step")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        print("matemask confirm")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
        print("matemask sign")

        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        print("switch window 2")
        driver.find_element(By.XPATH,"/html/body").send_keys(Keys.END)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div[2]/div/div[3]/label').click()
        time.sleep(2)
        send_email=driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[8]/div/div[2]/input')
        send_email.send_keys(google_email)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[8]/div/div[3]/div').click()
        c.execute("update ultiverse set status ='1' where address='%s';"%(address))
        conn.commit()
        count=count+1
        print ("&&&&&&&&&&&&&&&&&&&&&")
def vetrfy():
    pwd = os.getcwd()
    db_pwd = pwd + "/ultiverse.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * FROM ultiverse;')
    rows = c.fetchall()
    count=1
    for i in rows[16:40]:
        google_email=i[4]
        secret_key = i[3].split(" ")
        address=i[1]
        vetrfy_status=i[6]
        print("当前循环数量 "+str(count))
        print("当前钱包地址："+str(address))
        print("当前钱包助记词："+str(secret_key))
        print("当前email："+str(google_email))
        print("当前url："+str(vetrfy_status))

        EXTENSION_PATH = "/Users/0x024/Desktop/trade/ultiverse/tool/matemask.crx"
        WEB_DRIVER_PATH = "/Users/0x024/Desktop/trade/ultiverse/tool/chromedriver"

        opt = webdriver.ChromeOptions()
        opt.add_extension(EXTENSION_PATH)
        driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH,options=opt)
        #driver.set_window_size(height=1000,width=400)
        #driver.set_window_position(x=800, y=0)
        driver.switch_to.window(driver.window_handles[0])
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(1)
        secret_key_1 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-0"]')
        secret_key_1.send_keys(secret_key[0])
        secret_key_2 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-1"]')
        secret_key_2.send_keys(secret_key[1])
        secret_key_3 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-2"]')
        secret_key_3.send_keys(secret_key[2])
        secret_key_4 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-3"]')
        secret_key_4.send_keys(secret_key[3])
        secret_key_5 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-4"]')
        secret_key_5.send_keys(secret_key[4])
        secret_key_6 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-5"]')
        secret_key_6.send_keys(secret_key[5])
        secret_key_7 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-6"]')
        secret_key_7.send_keys(secret_key[6])
        secret_key_8 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-7"]')
        secret_key_8.send_keys(secret_key[7])
        secret_key_9 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-8"]')
        secret_key_9.send_keys(secret_key[8])
        secret_key_10 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-9"]')
        secret_key_10.send_keys(secret_key[9])
        secret_key_11 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-10"]')
        secret_key_11.send_keys(secret_key[10])
        secret_key_12 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-11"]')
        secret_key_12.send_keys(secret_key[11])
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('abcd1234')
        password_confirmation = driver.find_element(By.XPATH, '//*[@id="confirm-password"]')
        password_confirmation.send_keys('abcd1234')
        driver.find_element(By.XPATH, '//*[@id="create-new-vault__terms-checkbox"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()
        driver.switch_to.window(driver.window_handles[1])


        driver.get(vetrfy_status)
        print("click connect")
        driver.find_element(By.XPATH, '//button[text()="Connect"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[text()="MetaMask"]').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        print("switch window 2")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
        print("matemask next step")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        print("matemask confirm")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
        print("matemask sign")

        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        print("switch window 2")
        driver.find_element(By.XPATH,"/html/body").send_keys(Keys.END)
        time.sleep(2)
        c.execute("update ultiverse set vetrfy_status ='1' where address='%s';"%(address))
        conn.commit()
        count=count+1
        print ("&&&&&&&&&&&&&&&&&&&&&")
def play_go(sessions_date,sessions_count,sessions_result,sessions_goal):
    sessions_date = sessions_date
    # 12号对的26号
    sessions_count = sessions_count
    # 2第一场，3第二场 4第三场
    sessions_result = sessions_result
    # 2平局 3主场 4 客场
    sessions_goal = sessions_goal
    # 进球数量
    paly1 = "//div/div/div/main/div[2]/div[2]/div/div[%s]/div[%s]/section[2]/label" % (sessions_date, sessions_count)
    sessions_result = "//label[text()=%s]" % (sessions_result)
    print(paly1)
    print(sessions_result)
    pwd = os.getcwd()
    db_pwd = pwd + "/ultiverse.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * FROM ultiverse;')
    rows = c.fetchall()
    count=1

    for i in rows[30:40]:
        google_email=i[4]
        secret_key = i[3].split(" ")
        address=i[1]
        vetrfy_status=i[6]
        print("当前循环数量 "+str(count))
        print("当前钱包地址："+str(address))
        print("当前钱包助记词："+str(secret_key))
        print("当前email："+str(google_email))
        print("当前url："+str(vetrfy_status))
        EXTENSION_PATH=pwd + "/tool/matemask.crx"
        WEB_DRIVER_PATH=pwd+"/tool/chromedriver"
        opt = webdriver.ChromeOptions()
        opt.add_extension(EXTENSION_PATH)
        driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH,options=opt)
        #driver.set_window_size(height=1000,width=400)
        #driver.set_window_position(x=800, y=0)
        driver.switch_to.window(driver.window_handles[0])
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(1)
        secret_key_1 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-0"]')
        secret_key_1.send_keys(secret_key[0])
        secret_key_2 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-1"]')
        secret_key_2.send_keys(secret_key[1])
        secret_key_3 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-2"]')
        secret_key_3.send_keys(secret_key[2])
        secret_key_4 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-3"]')
        secret_key_4.send_keys(secret_key[3])
        secret_key_5 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-4"]')
        secret_key_5.send_keys(secret_key[4])
        secret_key_6 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-5"]')
        secret_key_6.send_keys(secret_key[5])
        secret_key_7 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-6"]')
        secret_key_7.send_keys(secret_key[6])
        secret_key_8 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-7"]')
        secret_key_8.send_keys(secret_key[7])
        secret_key_9 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-8"]')
        secret_key_9.send_keys(secret_key[8])
        secret_key_10 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-9"]')
        secret_key_10.send_keys(secret_key[9])
        secret_key_11 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-10"]')
        secret_key_11.send_keys(secret_key[10])
        secret_key_12 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-11"]')
        secret_key_12.send_keys(secret_key[11])
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('abcd1234')
        password_confirmation = driver.find_element(By.XPATH, '//*[@id="confirm-password"]')
        password_confirmation.send_keys('abcd1234')
        driver.find_element(By.XPATH, '//*[@id="create-new-vault__terms-checkbox"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()
        driver.switch_to.window(driver.window_handles[1])

        time.sleep(2)
        driver.get("https://ultiball.ultiverse.io/")
        print("click connect")
        driver.find_element(By.XPATH, '//button[text()="Connect"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[text()="MetaMask"]').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        print("switch window 2")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
        print("matemask next step")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        print("matemask confirm")
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
        print("matemask sign")

        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.execute_script("window.scrollBy(0,100000)")
        driver.find_element(By.XPATH, '//div[text()="Play"]').click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,100000)")

        time.sleep(3)


        driver.find_element(By.XPATH, paly1).click()
        print("goal")
        time.sleep(1)
        driver.find_element(By.XPATH, sessions_result).click()
        print("result")
        #time.sleep(2)
        #amount=driver.find_element(By.XPATH, '//div/div/div[5]/div/div[5]/div/div/input')
        #amount.send_keys(sessions_goal)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[5]/div/div[5]/div/div/span').click()
        print("amount")
        time.sleep(1)

        driver.find_element(By.XPATH, '//div/div/div[5]/div/button').click()
        print("confirm")
        count=count+1
        print ("&&&&&&&&&&&&&&&&&&&&&")

def update_count():
    pwd = os.getcwd()
    db_pwd = pwd + "/ultiverse.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * FROM ultiverse;')
    rows = c.fetchall()
    count=0
    for i in rows:
        address=i[1]
        print("当前循环数量 "+str(count))
        print("当前钱包地址："+str(address))
        c.execute("update ultiverse set id ='%s' where address='%s';"%(count,address))
        conn.commit()
        count=count+1

if __name__ == '__main__':
    #play_go(12,3,"\"Argentina\"",200)
    # 12号对的26号
    # 2第一场，3第二场 4第三场
    # 2平局 3主场 4 客场
    # 投注数量
    #update_count()

