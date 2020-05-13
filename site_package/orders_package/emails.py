from site_package import mail
from flask import current_app
from flask_mail import Message
from site_package.orders_package.forms import RegistrationForm


class email_form(RegistrationForm):
    def send_emails(self):
        msg = Message('So this our shopping List', sender = 'test@gmail.com',
        recipients=['hello@gmail.com'] )
        #TODO
        # get data from database
        
        msg.body = f''' 
        Hello

                      '''
       
        mail.send(msg)

    
    
    








    
