import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pathlib
import logging 
import webGlobal



def send_mail(m,sbj,f_addr,f_pswd,f_smtp,t_addr):

    msg = MIMEText(str(m) +  "\n--------------------\n" + webGlobal.mail["bottom_text"] ,'plain','utf-8')
    msg['Subject'] = sbj
    msg['From'] = f_addr
    msg['To'] = ",".join(t_addr)  if isinstance(t_addr,list)  else t_addr  
    server = smtplib.SMTP_SSL(f_smtp,465)
    server.set_debuglevel(0)
    server.login(f_addr,f_pswd)
    server.sendmail(f_addr,t_addr,msg.as_string())
    server.quit()
    logging.info("mailing... From:{0} ; To:{1}".format(f_addr,msg['To']))

def auto_mail(this_message,this_subject,t_addr):
    """
    send emails using zhengxc_auto@163.com 
    m  = message
    sbj = subject
    t_addr = to_address  str or list
    """
    f_addr=webGlobal.mail['f_addr']
    f_pswd=webGlobal.mail['f_pswd']
    f_smtp=webGlobal.mail['f_smtp']
    msg = MIMEText(str(this_message)+ "\n--------------------\n" + webGlobal.mail["bottom_text"],'plain','utf-8')
    msg['Subject'] = this_subject
    msg['From'] = f_addr 
    msg['To'] =  ",".join(t_addr)  if isinstance(t_addr,list)  else t_addr  
    server = smtplib.SMTP_SSL(f_smtp,465)
    server.set_debuglevel(0)
    server.login(f_addr,f_pswd)
    server.sendmail(f_addr,t_addr,msg.as_string())
    server.quit()
    logging.info("auto mailing... From:{0} ; To:{1}".format(f_addr,msg['To']))

def auto_mail_attach(this_message,this_subject,t_addr,file=None):
    f_addr=webGlobal.mail['f_addr']
    f_pswd=webGlobal.mail['f_pswd']
    f_smtp=webGlobal.mail['f_smtp']

    if file:
        msg = MIMEMultipart()
        part_text = MIMEText(this_message+ "\n--------------------\n"  + webGlobal.mail["bottom_text"])
        msg.attach(part_text)
        part_attach = MIMEApplication(open(file,'rb').read())
        part_attach.add_header('Content-Disposition', 'attachment', filename =pathlib.Path(file).name)
        msg.attach(part_attach) 
    else:
        msg = MIMEText(this_message+ "\n--------------------\n"  + webGlobal.mail["bottom_text"])
    msg['Subject'] = this_subject
    msg['From'] = f_addr 
    msg['To'] = ",".join(t_addr)  if isinstance(t_addr,list)  else t_addr
    server = smtplib.SMTP_SSL(f_smtp,465)
    server.set_debuglevel(0)
    server.login(f_addr,f_pswd)
    server.sendmail(f_addr,t_addr,msg.as_string())
    server.quit()
    logging.info("auto mailing... From:{0} ; To:{1}".format(f_addr,msg['To']))

if __name__=="__main__":

    
    auto_mail("hello","CCAS test","zhengxinchang@big.ac.cn")