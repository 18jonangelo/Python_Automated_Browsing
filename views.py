from selenium import webdriver #chromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep #time
from tkinter import *  #form
from tkinter.ttk import *  #progressbar
import sys #exitbtn
import random #randomNumbers
import sqlite3


# import  eel
#
# eel.start('index.html')
#
# eel.init*('venv')

root = Tk()
root.title("View Bot Generator")
#root.geometry('120x50')
#root.maxsize(90, 50)
#root.resizable(50, 50)
root.geometry("300x100+350+250")

#=== DB====

#===selenium==

def btnFunction():
    driver1 = webdriver.Chrome(executable_path="D:\Views Bot\chromedriver.exe")
    # driver2 = webdriver.Chrome(executable_path="D:\Views Bot\chromedriver.exe")
    # driver3 = webdriver.Chrome(executable_path="D:\Views Bot\chromedriver.exe")




    #
    # driver1.get(name)
    # driver1.get(item)
    # driver1.get("https://www.lazada.com.ph/products/neutron-ex-treme-g2-computer-case-blue-i178763686-s225808324.html?spm=a2o4l.searchlist.list.1.73791730XpySyl&search=1")
    # driver2.get("https://www.facebook.com/JonAngelo18/videos/10215541722449874")
    # driver3.get("https://www.facebook.com/JonAngelo18/videos/10215541722449874")



    t1 = ("https://www.lazada.com.ph/products/ecolum-hand-held-rechargeable-flashlight-yellow-eel546y-i1030856354-s3467600619.html?spm=a2o4l.home.flashSale.2.239e359djfFby3&search=1&mp=1&c=fs&clickTrackInfo=%7B%22rs%22%3A%220.0012698412698412698%22%2C%22prior_score%22%3A%220%22%2C%22submission_discount%22%3A%2210%25%22%2C%22iss%22%3A%220.0012698412698412698%22%2C%22type%22%3A%22entrance%22%2C%22prior_type%22%3A%22leaf%22%2C%22userid%22%3A%22%22%2C%22sca%22%3A%224%22%2C%22hourtonow%22%3A%222%22%2C%22abid%22%3A%22178638%22%2C%22itemid%22%3A%221030856354_0_leaf_0.0012698412698412698_0.0012698412698412698%22%2C%22pvid%22%3A%2280b8f31a-2d96-4e55-8646-7c5ccbf97636%22%2C%22pos%22%3A%220%22%2C%22rms%22%3A%220.0%22%2C%22c2i%22%3A%220.3765007280087767%22%2C%22scm%22%3A%221007.17760.178638.%22%2C%22ss%22%3A%220.0012698412698412698%22%2C%22i2i%22%3A%220.0%22%2C%22ms%22%3A%220.0012698412698412698%22%2C%22itr%22%3A%220.0%22%2C%22mt%22%3A%22leaf%22%2C%22its%22%3A%2240%22%2C%22promotion_price%22%3A%22117.00%22%2C%22anonid%22%3A%223ec85d7c-8b5d-4ab7-dfa2-227359dd9623%22%2C%22FinalScore%22%3A%220.09483599662780762%22%2C%22isc%22%3A%220%22%2C%22iss2%22%3A%220.0%22%2C%22data_type%22%3A%22flashsale%22%2C%22iss1%22%3A%220.0%22%2C%22config%22%3A%22%22%2C%22HP_score%22%3A%220.09483599662780762%22%2C%22channel_id%22%3A%220000%22%7D&scm=1007.17760.178638.0",
      "https://www.lazada.com.ph/products/asus-zenbook-14-ux425ja-bm066ts-lilac-14-inch-fhd-intel-core-i5-1035g18gb512gb-ssdintel-uhd-graphicswindows-10-laptop-i1235536638-s4420026913.html?spm=a2o4l.searchlist.list.3.715c3005OyEXEx&search=1",
      "https://www.lazada.com.ph/products/brand-new-asus-x409j-i1309652925-s4774346256.html?spm=a2o4l.searchlist.list.17.715c300528G3YD&search=1",
      "https://www.lazada.com.ph/products/seiko-watch-golden-automatic-dial-steel-original-analog-round-ladies-stainless-symg44j1-i1193510578-s4216114599.html?spm=a2o4l.home.just4u.3.45d8359daqSvV3&scm=1007.17519.162103.0&pvid=b5540073-5acd-4f40-b1ed-4c9bcb72d3a5&search=0&clickTrackInfo=tcExpIds%3A248%3Btcsceneid%3AHPJFY%3Bbuyernid%3A3ec85d7c-8b5d-4ab7-dfa2-227359dd9623%3Btcbid%3A4%3Btcboost%3A0%3Bpvid%3Ab5540073-5acd-4f40-b1ed-4c9bcb72d3a5%3Bchannel_id%3A0000%3Bmt%3Ai2i%3Bitem_id%3A1193510578%3Bself_ab_id%3A162103%3Bself_app_id%3A7519%3Blayer_buckets%3A955.3631%3B",
      "https://www.lazada.com.ph/products/aula-s2016f2068-mechanical-gaming-keyboard-104-keys-anti-ghosting-marco-programming-led-backlit-keyboard-for-pc-laptop-computer-i6730236-s8603727.html?spm=a2o4l.home.flashSale.6.7a9c359dMEtrHC&search=1&mp=1&c=fs&clickTrackInfo=%7B%22rs%22%3A%220.022510344827586206%22%2C%22prior_score%22%3A%220%22%2C%22submission_discount%22%3A%2258%25%22%2C%22iss%22%3A%220.022510344827586206%22%2C%22type%22%3A%22entrance%22%2C%22prior_type%22%3A%22racing%22%2C%22userid%22%3A%22%22%2C%22sca%22%3A%220%22%2C%22hourtonow%22%3A%222%22%2C%22abid%22%3A%22178638%22%2C%22itemid%22%3A%226730236_4_racing_0.022510344827586206_0.022510344827586206%22%2C%22pvid%22%3A%22d3b98a44-5730-40ea-8afb-b67afa79afdd%22%2C%22pos%22%3A%224%22%2C%22rms%22%3A%220.0%22%2C%22c2i%22%3A%220.0%22%2C%22scm%22%3A%221007.17760.178638.%22%2C%22ss%22%3A%220.022510344827586206%22%2C%22i2i%22%3A%220.0%22%2C%22ms%22%3A%220.022510344827586206%22%2C%22itr%22%3A%220.04%22%2C%22mt%22%3A%22racing%22%2C%22its%22%3A%2250%22%2C%22promotion_price%22%3A%221399.00%22%2C%22anonid%22%3A%223ec85d7c-8b5d-4ab7-dfa2-227359dd9623%22%2C%22DiversifyApplied%22%3A%223%22%2C%22FinalScore%22%3A%220.05831829831004143%22%2C%22isc%22%3A%222%22%2C%22iss2%22%3A%220.19352826050499727%22%2C%22data_type%22%3A%22flashsale%22%2C%22iss1%22%3A%220.006896551724137931%22%2C%22config%22%3A%22%22%2C%22HP_score%22%3A%220.05831829831004143%22%2C%22channel_id%22%3A%220000%22%7D&scm=1007.17760.178638.0",
      "https://www.lazada.com.ph/products/360-degree-full-cover-3in1-combo-phone-case-for-oppo-a3s-i252346397-s345587735.html?spm=a2o4l.searchlist.list.1.12b2218c7Yzkkw&search=1"
    )

    # sleep(min)
    while True:
        randNum = random.randint(10, 20)
        item = random.choice(t1)
        driver1.get(item)

        try:
            link = driver1.find_element_by_class_name("add-to-cart-buy-now-btn")
            link.click()
            # link2 = driver1.find_element_by_class_name("checkout-order-total-button")
            # link2.click()
            # element = WebDriverWait(driver1,10).until(
            #     EC.presence_of_all_elements_located((By.__class__,"add-to-cart-buy-now-btn"))
            # )
            # element.click()
        except:
            sleep(randNum)
            driver1.refresh()
        else:
            sleep(randNum)
            driver1.refresh()
        # sleep(randNum)
        # driver1.refresh()

        conn.commit()
        conn.close()
    # driver2.refresh()
    # driver3.refresh()


def addFunction():

    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    # DB Table
    # c.execute("""CREATE TABLE addresses(
    #         description text,
    #         url text)""")



    def submitFunc():
        conn = sqlite3.connect('address_book.db')

        c = conn.cursor()

        c.execute("INSERT INTO addresses VALUES (:descEntry, :urlEntry)",
                  {
                      'descEntry': descEntry.get(),
                        'urlEntry': urlEntry.get()
                  }

                  )


        descEntry.delete(0, END)
        urlEntry.delete(0, END)

        conn.commit()
        conn.close()

    #======Query Function

    def query():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        c.execute("SELECT description, oid FROM addresses")
        records = c.fetchall()
        print(records)


        print_records = ''
        #for record in records[0]:
        for record in records:
            print_records += str(record) + "\n"

        query_label = Label(addMaster, text=print_records)
        query_label.grid(row=9, column =0, columnspan=2)


        conn.commit()
        conn.close()

        # descript = descEntry.get()
        # urlAdd = urlEntry.get()



#========FORM=====


    addMaster= Tk()
    addMaster.title("Add New URL")
    addMaster.geometry("300x400+350+250")

    # desc1Label = Label(addMaster, text="")
    # desc1Label.grid(row=1, column=0)

    descEntry = Entry(addMaster, width=30)
    descEntry.grid(row=0, column=1)

    urlEntry = Entry(addMaster, width=30)
    urlEntry.grid(row=1, column=1)

    descLabel = Label(addMaster, text="Description:")
    descLabel.grid(row = 0, column = 0)

    urlLabel = Label(addMaster, text="URL:")
    urlLabel.grid(row = 1, column = 0)



    submitBtn = Button(addMaster, text="Submit", command=submitFunc)
    submitBtn.grid(row=6,column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    conn.commit()
    conn.close()

    #====Query Button
    query_btn = Button(addMaster, text ="Show Records", command=query)
    query_btn.grid(row=7, column =0, columnspan=2, pady=10, padx=10, ipadx=100)

def exitBtn():
    sys. exit("Error message")



b = Button(root, text="Execute", command=btnFunction)
# b.pack(side=tkinter.LEFT)
b.grid(row=1,column=1)

addBtn = Button(root, text="Add New URL", command=addFunction)
addBtn.grid(row=1,column=2)

bExit = Button(root, text="   Exit   ", command=exitBtn)
bExit.grid(row=1,column=3)





root.mainloop()
