import smtplib,argparse,sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

def work():
    
    server=smtplib.SMTP(host="smtp.gmail.com",port="587")
    server.starttls()
    semail=input("Email:")
    password=input("Password:")
    print("..trying login to your account..")
    try:
        server.login(semail,password)
    except smtplib.SMTPAuthenticationError as err:
        print("<*>Error..Cant login..<*>\nplease check your credentials..{}".format(err))
        sys.exit(1)
    i=input("To....eg->xyz@gmail.com,was@gmail.com  :")
    ls=i.split(",")
    print(ls)
    subject=input("Subject:")
    body=input("Body:")
    ans=int(input("Attach something:1 if yes:"))
    if ans==1:
        filename=input("path_to_file:")
        name=filename.split(os.path.sep)[-1]
        attachment=open(filename,"rb")

        part=MIMEBase("application","octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition","attachment;filename= "+name)


    for remail in ls:  
        msg=MIMEMultipart()
        msg["From"]=semail
        msg["To"]=remail
        msg["Subject"]=subject
        msg.attach(MIMEText(body,"plain"))
        if part:msg.attach(part)
        message=msg.as_string()
        try:
            server.sendmail(semail,remail,message)
        except:
            print("...ERROR WHILE SENDING...\n... CAN'T SEND YOUR EMAIL...")
        else:
            print(">>successfully send")
        server.quit()

if __name__=="__main__":
    work()
