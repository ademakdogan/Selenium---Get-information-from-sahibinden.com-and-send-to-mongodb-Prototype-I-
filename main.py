# -*- coding: utf-8 -*-
import information_process
import bot


if __name__ == "__main__":
    bot1 = bot.Bot("İzmir","Bornova","1500","9000000")
    value_list_first, price_list_first = bot1.main_process()
    information = information_process.information_process()
    final_list = information.final_process(value_list_first,price_list_first)
    information.send_mongo(final_list)


# =============================================================================
# araclar =[]
# arac_ = {}
# for i in range(len(final_list)):
#     arac_[i] = {
#             "Yıl" : final_list[i][0],
#             "Km" : final_list[i][1],
#             "Renk" : final_list[i][2],
#             "Fiyat" : final_list[i][3]
#             }
#     araclar.append(arac_[i])
# from pymongo import MongoClient
# 
# client = MongoClient("mongodb+srv://admin:admin@cluster0-azjtd.mongodb.net/test?retryWrites=true&w=majority")
# db = client.get_database("admin_db")
# records = db.test
# records.insert_many(araclar)
# records.count_documents({})
# len(araclar)
# records.delete_many({})
# =============================================================================
