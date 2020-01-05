# -*- coding: utf-8 -*-
import information_process
import bot


if __name__ == "__main__":
    bot1 = bot.Bot("İzmir","Bornova","1500","9000000")
    value_list_first, price_list_first,id_list = bot1.main_process()
    information = information_process.information_process()
    final_list = information.final_process(value_list_first,price_list_first,id_list)
    #information.send_mongo(final_list)


# =============================================================================
# records.insert_many(araclar)
# records.count_documents({})
# records.delete_many({})
# =============================================================================
