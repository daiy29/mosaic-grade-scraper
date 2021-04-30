from bs4 import BeautifulSoup
import requests
import time
import sys
import smtplib
from email.mime.text import MIMEText

def get_grades(): 
    session = requests.Session()

    userid = sys.argv[1]
    pwd = sys.argv[2]

    data = {
        'userid': userid,
        'pwd': pwd
    }

    s = session.post("https://epprd.mcmaster.ca/psc/prepprd/EMPLOYEE/EMPL/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?&cmd=login&languageCd=ENG", data=data)
    s = session.get('https://csprd.mcmaster.ca/psc/prcsprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL?Page=SSR_SSENRL_GRADE&PortalActualURL=https%3a%2f%2fcsprd.mcmaster.ca%2fpsc%2fprcsprd%2fEMPLOYEE%2fSA%2fc%2fSA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL%3fPage%3dSSR_SSENRL_GRADE&PortalContentURL=https%3a%2f%2fcsprd.mcmaster.ca%2fpsc%2fprcsprd%2fEMPLOYEE%2fSA%2fc%2fSA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL%3fPage%3dSSR_SSENRL_GRADE&PortalContentProvider=SA&PortalCRefLabel=Grades&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fepprd.mcmaster.ca%2fpsp%2fprepprd%2f&PortalURI=https%3a%2f%2fepprd.mcmaster.ca%2fpsc%2fprepprd%2f&PortalHostNode=EMPL&NoCrumbs=yes&PortalKeyStruct=yes')

    soup = BeautifulSoup(s.text, 'html.parser')
    Grades = soup.find_all('span', {'class' : 'PSEDITBOX_DISPONLY'})
    return Grades

def send_mail():

    FROM = sys.argv[3]
    TO = sys.argv[3]
    SUBJECT = "Mosaic grade update"
    TEXT = "Your grade has been updated, log in to Mosaic to check updated grades. New grades have also been displayed on the command line." 
   
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sys.argv[3], sys.argv[4])
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


starttime = time.time()
Grades = get_grades()
print("Initial courses and grade info: ")
for grade in Grades:
    print(grade.get_text())
print("An e-mail will be sent if grades have been updated")

while True:
    Grades2 = get_grades()
    if (Grades == Grades2):
        pass
    else:
        send_mail()
        print("Grade update:")
        for grade in Grades2:
            print(grade.get_text())

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))





