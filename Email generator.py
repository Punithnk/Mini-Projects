import smtplib
import random

def read_data_send_mail():
    try:
        f=open("student_mails.txt","r")
        student_mails=f.read()

        student_mails=student_mails.split(",")
        print(student_mails)
    except:
        print("file not availble")
     

    sender_email="******@gmail.com"        
     
    for i in student_mails:
      otp_number=random.randint(0000,9999)
      print(otp_number)
      s = smtplib.SMTP("smtp.gmail.com",587)
      s.starttls()
      s.login(sender_email, "**********")
      message = f"Hi your OTP number is,{otp_number}, OTP is valid for 1 mins. Do not share this OTP with any one "
      
    try:
        s.sendmail(sender_email, i, message)
        print("mail sent successfully")
        s.quit()
    except:
        print("mail not sent")
read_data_send_mail    