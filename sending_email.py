import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

MY_ADDRESS = 'mithunchitradurga@gmail.com'
PASSWORD = 'xxxxxxx'

def main():
    name, email = "mithun","mithunchitradurga@gmail.com" #get_contacts('mycontacts.txt')  # read contacts
    message_template = "welcome {0} demo message" #read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)


    msg = MIMEMultipart()  # create a message

    # add in the actual person name to the message template
    message = message_template.format(name)

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))


    #attach file
    # open the file to be sent
    filename = "demo.txt"
    attachment = open(filename, "rb")#read in bytes

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)





    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()

#if smtp doesnt allow you to login : go to below link
#https://www.google.com/settings/security/lesssecureapps
