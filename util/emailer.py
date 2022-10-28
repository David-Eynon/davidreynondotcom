# using yagmail for access to GMail
import os
import base64
import datetime
import sys
import json
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from configparser import ConfigParser
from lib.run_configs import RunConfigs
from xml_report_access import XMLReportAccess

class Emailer:
    
    REPORT_LOCATION = os.environ["CURRENT_REPORT_OUTPUT"];
    PROJECT_NAME = os.environ["PROJECT_NAME"];

    def __init__(self):
        return


    def to_emails(self):
        return RunConfigs()._email_report_to_addresses

    def from_email(self):
        return RunConfigs()._email_report_from_address;

    def today_date(self):
        date_s = str(datetime.datetime.now())
        return date_s

    def form_email_subject(self):
        singular_status = XMLReportAccess().get_singular_status()
        subject = "TEST RESULT - [{}] - {} - {}".format(self.PROJECT_NAME, singular_status, self.today_date())
        return subject

    def form_email_body(self):
        singular_status = XMLReportAccess().get_singular_status()
        rp = XMLReportAccess().get_report_results_data_object()
        body = 'TEST RESULT: {} \n'.format(singular_status)
        body += 'TEST RUN ON: {} \n'.format(self.today_date())
        for res in rp:
            body += "\t{} : {} \n".format(res.upper(), rp[res])
        return MIMEText(body, 'plain', 'utf-8')

    def get_attachments(self):
        attachments_MIME = MIMEBase('text', 'html')
        if os.path.exists(self.REPORT_LOCATION):
            fp = open(self.REPORT_LOCATION, 'rb')
            attachments_MIME.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachments_MIME)
            attachments_MIME.add_header('Content-Disposition','attachment', filename=os.path.basename(self.REPORT_LOCATION))
        return attachments_MIME


    def get_emailer_password(self):
        return os.environ.get('EMAILER_GMAIL_PASSWORD')

    def form_email(self):
        FROM_EMAIL = self.from_email()
        TO_EMAIL = self.to_emails()
        EMAIL_SUBJECT = self.form_email_subject()
        EMAIL_BODY = self.form_email_body()
        EMAIL_PW = self.get_emailer_password()
        ATTACHMENTS = self.get_attachments()

        outer = MIMEMultipart()

        outer['From'] = FROM_EMAIL
        outer['To'] = TO_EMAIL        
        outer['Subject'] = EMAIL_SUBJECT
        
        outer.attach(self.form_email_body())    
        outer.attach(self.get_attachments())

        return outer.as_string()

    def send_email(self):
        FROM_EMAIL = self.from_email()
        TO_EMAIL = self.to_emails()
        EMAIL_PW = self.get_emailer_password()

        formed_email = self.form_email()

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(FROM_EMAIL, EMAIL_PW)
                s.sendmail(FROM_EMAIL, TO_EMAIL, formed_email)
                s.close()
        except Exception as e:
            print("Unable to send the email. Error: ", sys.exec_info()[0])
            print(e)
        print('Sent mail', FROM_EMAIL, TO_EMAIL)

if __name__=="__main__":
    Emailer().send_email()
