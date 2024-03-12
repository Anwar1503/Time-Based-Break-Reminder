import smtplib
from plyer import notification
import time
from notifyproject import name_,time_value

EMAIL_ADDRESS='Email@email.com'
#give email with creating an app password from account settings in goole accounts in security section.
EMAIL_PASSWORD='******************'
##the password which you set should be there
RECEIVER_MAIL =name_


def notifyme(title,message):
    notification.notify(
        title = title,
        message =message,
        app_icon ="icon path",
        timeout =10,
    )


if __name__ == '__main__' :
    notifyme("alert!!!!","your pc is in parental control")
    while True:
      time.sleep(int(time_value))
      hours = (int(time_value)) // 3600
      minutes = ((int(time_value)) % 3600) // 60
      seconds = (int(time_value)) % 60
      message = f"It's been {hours} hours, {minutes} minutes, and {seconds} seconds. You should take a break!"
      notifyme("alert!!!!", message)
      server = smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
      subject ="PC USAGE OF YOUR SON"
      body = "your child has been using laptop continously ask him to take break "

      message = f'Subject: {subject}\n\n{body}'

      server.sendmail(EMAIL_ADDRESS,RECEIVER_MAIL, message)
      server.quit()