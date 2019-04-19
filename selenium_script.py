import re
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import ui




TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 20)
    return driver


def lookup(driver, query):
    driver.get("https://www.zillow.com/homes/for_rent/")
    try:
        search_input = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "citystatezip")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "zsg-icon-searchglass")))
        search_input.send_keys(query[0])
        button.click()

        dropdown = driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//legend[@data-za-label="Listing Type"]')))
        dropdown.click()

        checkbox = driver.find_element_by_css_selector(".filter-pane").find_element_by_id("category-entries").find_element_by_xpath('//ul/li[@id="fr-listings"]/div/label[@for="fr-listings-input"]')
        # print(checkbox.is_selected())
        if checkbox.is_selected():
            checkbox.click()
        dropdown = driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//legend[@data-za-label="Price"]')))
        dropdown.click()
        driver.find_element_by_css_selector(".filter-price").find_element_by_xpath('//*[@id="rental-payment-min-options"]/ul/li[@data-value=""]').click()
        driver.find_element_by_css_selector(".filter-price").find_element_by_xpath('//*[@id="rental-payment-max-options"]/ul/li[@data-value=""]').click()

        dropdown = driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//fieldset[@data-dropdown-id="beds-select"]')))
        dropdown.click()

        # driver.implicitly_wait(10)

        driver.find_element_by_css_selector(".filter-pane .search-entry > ul").find_element_by_xpath('//li[@data-value="0,"]').click()

        dropdown = driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//legend[@data-za-label="Home Type"]')))
        dropdown.click()
        houses_check = driver.find_element_by_xpath('//ul/li[@id="hometype-sf-top-filters"]/label[@for="hometype-sf-top-filters-input"]')
        if houses_check.is_selected():
            houses_check.click()

        apartment_check = driver.find_element_by_xpath(
            '//ul/li[@id="hometype-mf-top-filters"]/label[@for="hometype-mf-top-filters-input"]')

        if not apartment_check.is_selected():
            apartment_check.click()

        condo_check = driver.find_element_by_xpath(
            '//ul/li[@id="hometype-condo-top-filters"]/label[@for="hometype-condo-top-filters-input"]')
        if condo_check.is_selected():
            condo_check.click()

        town_check = driver.find_element_by_xpath(
            '//ul/li[@id="hometype-townhome-top-filters"]/label[@for="hometype-townhome-top-filters-input"]')
        if town_check.is_selected():
            town_check.click()

        get_results(driver)
    except TimeoutException as ex:
        print("Box or Button not found in google.com")
        print(ex)


def get_results(driver):
    driver.wait.until(EC.invisibility_of_element((By.CLASS_NAME, "list-loading-message-cover")))
    results = driver.find_elements_by_xpath('//div[@id="search-results"]/ul/li')
    print(len(results)-1)
    xsl_results = list()
    for index, result in enumerate(results):
        try:
            # driver.wait.until(EC.invisibility_of_element((By.XPATH, '//div[@id="search-results"]/ul/li')))
            if index == 2:
                continue
            single_result = dict()
            # print(result.get_attribute('article'))
            # print(result.get_attribute('class'))


            # result.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'article')))

            result.click()

            driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ds-price")))
            price = driver.find_element_by_xpath('.//h3[@class="ds-price"]/span/span[@class="ds-value"]').text

            months = driver.find_element_by_xpath('.//h3[@class="ds-price"]/span/span[@class="ds-label-small"]').text

            single_result["price"] = price + months

            # driver.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h1.ds-address-container")))

            addressess = driver.find_elements_by_xpath('.//h1[@class="ds-address-container"]/span')

            prime_address = addressess[0].text
            sec_address = addressess[1].text
            single_result["address"] = prime_address
            sec_address = sec_address.split(',')
            single_result['zip'] = sec_address[1].split(" ")[1]
            single_result['city'] = sec_address[0]

            # driver.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "header.ds-bed-bath-living-area-header")))

            facilitites = driver.find_elements_by_xpath('.//h3[@class="ds-bed-bath-living-area-container"]/span')
            bd = facilitites[0].find_elements_by_xpath('.//span')

            bd = bd[0].text + ' ' + bd[1].text
            single_result['bed'] = bd
            ba = facilitites[1].find_elements_by_xpath('.//span')

            ba = ba[0].text + ' ' + ba[1].text
            single_result['baths'] = ba
            area = facilitites[2].find_elements_by_xpath('.//span')

            area = area[0].text + ' ' + area[1].text
            single_result['area'] = area
            buildings = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'span.ds-body.ds-home-fact-value')))

            buildings = buildings.text
            single_result['type_of_home'] = buildings
            phone = driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "RCFAgentPhoneDesktopText__phoneNumber")))

            phone = phone.text
            single_result['phone_number'] = phone
            xsl_results.append(single_result)
            close_button = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button.ds-close-lightbox-icon.hc-back-to-list')))
            close_button.click()
            driver.implicitly_wait(300)
            print(xsl_results)
        except StaleElementReferenceException:
            print ('exception==============>')
            pass
        except TimeoutException:
            pass


if __name__ == "__main__":
    driver = init_driver()
    query = "Hennepin County MN", "abcd", "test", "ABI00L"
    lookup(driver, query)
    time.sleep(5)
    driver.quit()

# table_trs = driver.find_elements_by_xpath('//table[@id="dlData"]/tbody/tr/td/table/tbody/tr')
# # print (table_trs)
# for tr in table_trs:
#     # print (tr.get_attribute("innerHTML").encode("UTF-8"))
#
#     td = tr.find_elements_by_xpath(".//td")
#     # print (td)
#     if len(td) == 2:
#         key = td[0].get_attribute("innerHTML").encode("UTF-8")
#         value = td[1].get_attribute("innerHTML").encode("UTF-8")
#         print(key, value)
#         print(remove_tags(key.decode("UTF-8")), remove_tags(value.decode("UTF-8")))