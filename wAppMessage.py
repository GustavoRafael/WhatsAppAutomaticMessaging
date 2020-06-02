from selenium import webdriver
import html
import xml.dom

# it is necessary to have the chromedriver accordingly your browser version. 
# the one here is for chrome v83.
# for other versions check: https://chromedriver.chromium.org/downloads
# download the zip file and substitute the one the root
web_driver_path = "./chromedriver"
driver = webdriver.Chrome(web_driver_path)
driver.get('https://web.whatsapp.com/')


def getContact():
    try:
        contactName = input("Please type contact name:")
        # select the contact name in whatsapp page.
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contactName))
        user.click()
    except Exception as e:
        print("getcontact Error {}".format(e))
    

def getMessage():
    # input message
    return input("Please type your message: ")    

def sendMessage(msg):    
    try:
        # filling in the message to be sent.
        msg_box = driver.find_element_by_class_name('_1Plpp')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
    except Exception as e:
        print("sendMessage Error code {}".format(e))
    

def whatsAppMsg():
    try:
        sendMessage(myMsg)
    except Exception as e_id:
        print("whatsAppMsg Error code {}".format(e_id))
    else:
        print("message sent!!!")


# hold the application to avoid start looking for elements that are not loaded yet
input("Please, read the Qr code and Press Enter!!!")
getContact()
myMsg = getMessage()