# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 10:29:41 2019

@author: Admin
"""
from selenium import webdriver
import re
from pymongo import MongoClient



class information_process():

    
    def final_process(self,list1,price_list1):
        list2 = []
        list3 = []
        for i in range(len(list1)):
            if len(list3) < 3:
                list3.append(list1[i])
            elif len(list3) == 3:
                list2.append(list3)
                list3 = []
                list3.append(list1[i])
        if len(list3) == 0:
            pass
        else:
            list2.append(list3)
        #Regex for TL 
        price_list_2 = []
        for i in price_list1:
             a = re.findall(r"(\d+[\.\,\ ]\d+)",i)
             price_list_2.append(a)
        for i in range(len(price_list_2)):
            list2[i].append(price_list_2[i][0])
        return list2
    
    def send_mongo(self, final_list):
        araclar =[]
        arac_ = {}
        for i in range(len(final_list)):
            arac_[i] = {
                    "Yıl" : final_list[i][0],
                    "Km" : final_list[i][1],
                    "Renk" : final_list[i][2],
                    "Fiyat" : final_list[i][3]
                    }
            araclar.append(arac_[i])
        client = MongoClient("mongodb+srv://admin:admin@cluster0-azjtd.mongodb.net/test?retryWrites=true&w=majority")
        db = client.get_database("admin_db")
        records = db.test
        records.insert_many(araclar)
        
        
        
        
        