from selenium import webdriver

def test_site_title():
    driver = webdriver.Chrome()

    try:
        driver.get('https://google.com')
        assert 'Example Domain' in driver.title
    finally:
        driver.quit()
