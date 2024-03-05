from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
from threading import Thread
from time import sleep
number_of_requests= 100


def changeVPN(number , browser):
    extension_Protocol = "chrome-extension"
    extension_ID = "bihmplhobchoageeokmgbdihknkjbknd"
    indexPage = extension_Protocol + "://" + extension_ID + "/panel/index.html"
    browser.get(indexPage)
    time.sleep(5)
    browser.switch_to.window(window_name=browser.window_handles[0])
    time.sleep(2)
    browser.find_element(By.XPATH, "//*[contains(text(), 'Best Choice')]").click()
    time.sleep(2)
    flag_elements = browser.find_elements(By.CLASS_NAME, "flag")
    if flag_elements:
        flag_elements[number].click()
    browser.find_element(By.ID, "ConnectionButton").click()
    time.sleep(5)

def run(threadName=""):
    old = 10
    for i in range(0, number_of_requests):
        print("Thread is " + threadName + " with " + str(i))
        if i == 0:
            extension_path = "touchVPN.crx"
            options = webdriver.ChromeOptions()
            options.add_extension(extension_path)
        browser = webdriver.Chrome(options=options)
        # rand number is modulo 7
        num = 0
        while num == old:
            num = random.randint(0, 6)
        old = num
        changeVPN(num , browser)
        browser.get("https://ari.com.vn/")
        time.sleep(5)
        browser.quit()
    return

if __name__ == "__main__":
    try:

        thread1 = Thread(target=run , args=("1",))
        thread2 = Thread(target=run , args=("2",))
        thread3 = Thread(target=run , args=("3",))
        thread4 = Thread(target=run , args=("4",))
        thread5 = Thread(target=run , args=("5",))
        thread6 = Thread(target=run , args=("6",))  
        thread7 = Thread(target=run , args=("7",))  
        thread8 = Thread(target=run , args=("8",))  
        
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
    except Exception as e:
        print(e)
        print("An exception occurred")
    