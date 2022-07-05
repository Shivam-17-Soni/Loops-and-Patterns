# Schedule your program to wish your fried at exact 12am at night as here we have not scheduled the program.
# Turn on your "Less secure app access" through gmail or google so that this program can send messages.
# You can send message using SMS APIs from the program.

import pandas as pd                                         # install panda first using pip
import datetime
import smtplib
import os
os.chdir(r"D:\Python Programs\Projects")                    # Providing directory path to check program is working on schedule or not.
#os.mkdir("Testing")                                        # Making directory to check program is working on schedule or not.

GMAIL_ID = ""                                               # Enter yur E-Mail Id from which you want to send E-Mail.
GMAIL_PSWD = ""                                             # Here, give you E-Mail Id Password.


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject : {sub} and message {msg}.")
    s=smtplib.SMTP("smtp.gamil.com",587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)

    s.sendmail(GMAIL_ID,to,f"Subject : {sub}\n\n{msg}")
    s.quit()

if __name__ == "__main__":
    #endEmail(GMAIL_ID,"subject","test message")
    #exit()

    df = pd.read_excel("data.xlsx")                         #dataframe # install xlrd using pip
    #print(df)
    today=datetime.datetime.now().strftime("%d-%m")         # "strftime()" fuction is used to take out or slice the date, time from the datetime function and made its type to string.
    #print(today)kk
    #print(type(today))
    yearNow=datetime.datetime.now().strftime("%Y")
    writeInd=[]
    for index, item in df.iterrows():                       # "iterrows()" function is used to take index and item from a dataframe or dataframe file like excel file.
        #print(index,item["Birthday"])
        bday = item['Birthday'].strftime("%d-%m")
        print(bday)
        #msg = "I don't send birthday emails to people but you are such an awesome person in my life that I am bound to send you an email onthis ocassion of your birthday. You are the best person and friend."
        if (today == bday) and yearNow not in str(item['Year']):    ## To avoid itteration.
            sendEmail(item['Email'], "Happy Birthday",item['Dialogue'])
            writeInd.append(index)
    
    if writeInd!=[]:
        for i in writeInd:
            yr = df.loc[i,"Year"]
            df.loc[i,"Year"] = str(yr) + "," + str(yearNow)     # To add current year to avoid itteration.
        
        df.to_excel("data.xlsx", index=False)                                # To append or update the excel sheet. and To open Excel file first install "openpyxl" through pip. So you are able to open the excel file.
