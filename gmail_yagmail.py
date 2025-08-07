import os
import dotenv
import yagmail

#load dotenv variables
dotenv.load_dotenv()

#get dotenv variables
password = os.getenv('gmail_test')

#create SMTP object with yagmail and provide sender info

yagmail_SMTP = yagmail.SMTP(user= 'youremail@gmail.com',password=password)


body ="""
My name is Neo.Call me Neo.
Don't call me Anderson. I am unplugged now.


Regards
Neo

"""
#receiver info

yagmail_SMTP.send(to='youremail@gmail.com',
                  subject='test',
                  contents=body,
                  attachments=['sample1.docx'])

print('Email sent succesfully!')