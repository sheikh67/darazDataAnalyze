from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep
import csv

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.daraz.pk/wow/i/pk/landingpage/flash-sale?spm=a2a0e.home.flashSale.1.6a274937mZuzR6&wh_weex=true&amp;wx_navbar_transparent=true&amp;scm=1003.4.icms-zebra-5029921-2824236.OTHER_5360388823_2475751&skuIds=3323260,137582873,180022323,178762280,1401794,183768401,142556048")

sleep(10)

saleTitle = WebDriverWait(driver, 10).until( lambda driver: driver.find_elements_by_class_name("sale-title"))
salePrice = WebDriverWait(driver, 10).until( lambda driver: driver.find_elements_by_class_name("sale-price"))
originPriceValue = WebDriverWait(driver, 10).until( lambda driver: driver.find_elements_by_class_name("origin-price-value"))
discount = WebDriverWait(driver, 10).until( lambda driver: driver.find_elements_by_class_name("discount"))
pgText = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_class_name("pg-text"))

# iterate through list and get text
with open("DarazFlashSalesData.csv", "w", newline="") as file_writer:
    fields = ['Sale_Title', 'Sale_Price', 'Orignal_Price', 'Discount', 'Item_Sold']
    wr = csv.DictWriter(file_writer, fieldnames=fields, delimiter=',')
    wr.writeheader()
    for (i, j, k, l, m) in zip(saleTitle, salePrice, originPriceValue, discount, pgText):
        data = {'Sale_Title': i.text, 'Sale_Price': j.text, 'Orignal_Price': k.text, 'Discount': l.text, 'Item_Sold':m.text}
        wr.writerow(data)
        print(data)

driver.quit()
