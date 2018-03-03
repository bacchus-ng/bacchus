from django.core.mail import send_mail
from settings.models import Settings

class MailTools:
    @staticmethod
    def sendMail(mail_to,message):
        return send_mail("Open Bacchus Notification",message,'',mail_to,fail_silently=False,)
    
    @staticmethod
    def testMail():
        mails = Settings.objects.get(parameter="mail_to")
        mail_to = mails.value.split(',')        
        return MailTools.sendMail(mail_to,"This is an auto-generated message to test Open Bacchus e-mail settings.")

    @staticmethod
    def notifyUsers(message):
        mails = Settings.objects.get(parameter="mail_to")
        mail_to = mails.value.split(',')        
        return MailTools.sendMail(mail_to,message)
