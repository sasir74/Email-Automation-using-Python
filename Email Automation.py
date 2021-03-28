'''
Created by Sasi Ravipati 
Email Automation using Python
'''


import pandas as pd
import smtplib

my_name = "Sasi Kumar" 
my_email = "email@gmail.com"
my_pwd = "Password"  #enter email & pwd here


server=smtplib.SMTP("smtp.gmail.com",587) #port & server details
server.starttls()
server.login(my_email,my_pwd)  

email_list = pd.read_csv("emaillist.csv") #will read file

all_names = email_list['Names']
all_emails = email_list['Email']
all_subjects = email_list['Subject']
all_messages = email_list['Message']


for idx in range(len(all_emails)):     # Loop for emails

    # Get each records name, email, subject and message
    name = all_names[idx]
    email = all_emails[idx]
    subject = all_subjects[idx]
    message = all_messages[idx]

    # Create email to send
    full_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}"
                  .format(my_name, my_email, name, email, subject, message))

    # In the email field, you can add multiple other emails if you want
    # all of them to receive the same text
    try:
        server.sendmail(my_email, [email], full_email)
        print('Email to {} successfully sent!\n\n'.format(email))
    except Exception as e:
        print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))


server.close()  
