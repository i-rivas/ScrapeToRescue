from bs4 import BeautifulSoup
import requests
import smtplib
import time

html_text = requests.get('https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals2.aspx?species=Dog&sex=A&agegroup=All&onhold=N&orderby=ID&colnum=3&AuthKey=1w2169r3m576xy6505c6z57e3g07tkl0vwgcx29kkels9bo086&css=https://ws.petango.com/WebServices/adoptablesearch/css/styles.css').text
soup = BeautifulSoup(html_text, 'lxml')
dogs = soup.find_all('div', class_ = 'list-animal-info-block' )

def sending_email(line):
    try:
        #Create your SMTP session
        smtp = smtplib.SMTP('smtp.gmail.com', 587)

    #Use TLS to add security
        smtp.starttls()

        #User Authentication
        smtp.login("email","password")

        #Defining The Message
        fromaddr = "from email goes here"
        toaddrs = "to email goes here"

        message = ("From: %s\r\nTo: %s\r\n\r\n" % (fromaddr, ", ".join(toaddrs)))

        message = message + line

        #Sending the Email
        smtp.sendmail("from email goes here", "to email goes here", message)

        #Terminating the session
        smtp.quit()
        print ("Email sent successfully!")

    except Exception as ex:
        print("Something went wrong....",ex)

while True:
    time.sleep(32400)

    for dog in dogs:

        dogs_type = dog.find('div', class_ = 'list-animal-breed').text

        if 'Chihuahua, Short Coat/Mix' in dogs_type:
            print (dogs_type)
            more_info = dog.a['href']
            all = dogs_type + "\nhttps://ws.petango.com/webservices/adoptablesearch/" + more_info
            print(f"https://ws.petango.com/webservices/adoptablesearch/" + more_info)
            sending_email(str(all))

        elif 'Chihuahua' in dogs_type:
            print (dogs_type)
            more_info = dog.a['href']
            exact = dogs_type + "\nhttps://ws.petango.com/webservices/adoptablesearch/" + more_info
            print(f"https://ws.petango.com/webservices/adoptablesearch/" + more_info)
            sending_email(str(exact))
