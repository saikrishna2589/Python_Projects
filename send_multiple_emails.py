import os
import yagmail
import dotenv

#load dotenv variables
dotenv.load_dotenv()

#access variables in dotenv
password = os.getenv('gmail_app')


#read email text file

email_info = 'emails'

with open(email_info, 'r') as file:
    #email_receivers = file.readlines() #readlines is a risk as it reads empty lines too
    email_list = [line.strip() for line in file if line.strip()]

#email_list =[]
#email_list.extend(email_receivers)  #copying email_receivers list to official list

#SMTP and sender info

try:
    sender_info_yagmail = yagmail.SMTP(user='youremailaddress',
                                   password=password)
except Exception as e:
    print("Failed to connect to SMTP: ",e)
    exit()

#receiver info

body = """
Hi, i just want to say hi!

cheers
Mr.Anderson
"""

#sending email to
for each_email in email_list:
    try:
        sender_info_yagmail.send(to=each_email,
                                 contents=body)
        print("Emails sent successfully!")

    except Exception as e:
        print(f"Failed to send email to {each_email} : {e}")
