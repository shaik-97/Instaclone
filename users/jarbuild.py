from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def build():
    # Chrome Options to avoid issues
    options = Options()
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")  # Uncomment this line to run in headless mode

    # Instantiate a ChromeDriver class with options
    driver = webdriver.Chrome(options=options)

    try:
        # Open Website
        driver.get("https://rbtqa.onmobile.com/JenkinsPaymentGateway/")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/section/ul/li/a/span[1]")))
        # //*[@id="main-panel"]/div[2]/div/section/ul/li/a/span[1]
        element.click()

        # Maximize the browser
        driver.maximize_window()

        # Log in
        username = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/div[1]/input")))
        username.send_keys("admin")
        password = driver.find_element(By.XPATH, "/html/body/div/div/form/div[2]/input")
        password.send_keys("P@$$w0rd")
        login_button = driver.find_element(By.XPATH, "/html/body/div/div/form/div[4]/button")
        # /html/body/div/div/form/div[4]/button
        time.sleep(5)
        login_button.click()
        time.sleep(5)
        prism_build = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[13]/a")
        prism_build.click()
        time.sleep(5)
        prism_build_for_Saleem = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/table/tbody/tr[4]/td[3]/a")
        prism_build_for_Saleem.click()
        time.sleep(5)

        build_with_params = driver.find_element(By.XPATH,
                                                     "/html/body/div[3]/div[1]/div[1]/div[5]/span/a")
        build_with_params.click()
        time.sleep(5)

        #dev = 'dev'
        dev = '62.sp1'
        if dev != "dev":
            filter = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/div[1]/input[2]")))
            filter.send_keys(dev)
            time.sleep(5)
            #build = driver.find_element(By.XPATH,
             #                           "/html/body/div[3]/div[2]/form/div[1]/div[2]/div/span/span/button")
            #build.click()
            time.sleep(5)

        #build = driver.find_element(By.XPATH,
              #                                  "/html/body/div[3]/div[2]/form/div[1]/div[2]/div/span/span/button")
        #build.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        return False
    finally:
        # Always close the driver
        driver.quit()
    return True
#
# if __name__ == "__main__":
#     main()