# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:14:55 2019

@author: Admin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Bot():
    def __init__(self,il,ilce,min_price,max_price):
        self.il = il
        self.ilce  = ilce
        self.min_price = min_price
        self.max_price = max_price
        
    def main_process(self):
        driver_path = "C:\\Users\\Admin\\Desktop\\selenium\\chromedriver.exe"
        browser = webdriver.Chrome(driver_path)
        browser.get("https://www.sahibinden.com/kategori/otomobil")
        self.browser = browser
        time.sleep(2)
        browser.maximize_window()
        time.sleep(2)
        browser.find_element_by_css_selector("a[class = 'all-classifieds-link']").click()
        #element = browser.find_element_by_link_text("Cadillac")
        element = browser.find_element_by_xpath("//*[@id='searchCategoryContainer']/div/div[1]/ul/li[65]/a")
        browser.execute_script('arguments[0].scrollIntoView(true);', element)
        browser.find_element_by_xpath("//*[@id='searchCategoryContainer']/div/div[1]/ul/li[68]/a").click()
        browser.find_element_by_xpath("//*[@id='searchCategoryContainer']/div/div[1]/ul/li[68]/a").click()
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, 400)")
        browser.find_element_by_link_text("İl").click()
        time.sleep(1)
        browser.find_element_by_link_text(self.il).click()
        #Menu kapatma
        browser.find_element_by_xpath("//*[@id='searchResultLeft-address']/dl/dd/ul/li[1]/div/a").click()
        time.sleep(1)
        browser.find_element_by_link_text("İlçe").click()
        time.sleep(1)
        browser.find_element_by_link_text(self.ilce).click()
        browser.find_element_by_link_text("Bayraklı").click()
        browser.find_element_by_link_text("Buca").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='searchResultLeft-address']/dl/dd/ul/li[2]/div/a").click()
        time.sleep(1)
        browser.find_element_by_css_selector("input[name = 'price_min']").send_keys(self.min_price)
        browser.find_element_by_css_selector("input[name = 'price_max']").send_keys(self.max_price)
        browser.execute_script("window.scrollTo(0, 900)")
        browser.find_element_by_link_text("Dizel").click()
        
        #browser.find_element_by_xpath("//*[@id='_cllpsID_a6']").click()
        browser.find_element_by_link_text("Manuel").click()
        browser.find_element_by_link_text("Otomatik").click()
        browser.find_element_by_css_selector("button[class = 'btn btn-block search-submit']").click()
        time.sleep(2)
        
        #Value_list ve Price List oluşumu
        value_list_first = browser.find_elements_by_css_selector("td[class = 'searchResultsAttributeValue']")
        list1= []
        for i in value_list_first:
            list1.append(i.text)
        price_list_first = browser.find_elements_by_css_selector("td[class = 'searchResultsPriceValue']")
        price_list = []
        for i in price_list_first:
            price_list.append(i.text)
        
        id_list3 = browser.find_elements_by_class_name("searchResultsItem")
        id_list = []
        
        for i in id_list3:
            data_id = i.get_attribute("data-id")    
            if data_id == None:
                pass
            else:
                id_list.append(data_id)
                
        #1 den fazla sayfa için try-except
        while True :
            try:
                browser.execute_script("window.scrollTo(0, 2000)")
                browser.find_element_by_link_text("Sonraki").click()
                time.sleep(2)
                b = browser.find_elements_by_css_selector("td[class = 'searchResultsAttributeValue']")
                for i in b:
                    list1.append(i.text)
                c = browser.find_elements_by_css_selector("td[class = 'searchResultsPriceValue']")
                for i in c:
                    price_list.append(i.text)
                d = browser.find_elements_by_class_name("searchResultsItem")
                for i in d:
                    data_id = i.get_attribute("data-id")    
                    if data_id == None:
                        pass
                    else:
                        id_list.append(data_id)
                time.sleep(1)
                
            except (NoSuchElementException):
                break 
        return list1,price_list,id_list