from django.core import mail
from django.template import loader
from django.db import models

from blog.models import Blog
from home.models import Subscribe
from datetime import datetime


# Create your models here.
class Mailers(models.Model):
    primaryBlog = Blog.objects.all().order_by('-id')[0]
    secondaryBlog = Blog.objects.all().order_by('-id')[1]
    tertiaryBlog = Blog.objects.all().order_by('-id')[2]

    def __str__(self):
        return str(self.id) + ", B1: " + str(self.primaryBlog.id) + \
               ", B2: " + str(self.secondaryBlog.id) + \
               ", B3: " + str(self.tertiaryBlog.id)


class SendMails(models.Model):
    mailer_to_send = models.ForeignKey(Mailers, on_delete=models.CASCADE)
    process_start_time = models.DateTimeField(default=datetime.now(), editable=False)
    process_finish_time = models.DateTimeField(default=datetime.now(), editable=False)
    exceptions = models.IntegerField(default=0, editable=False)
    mails_sent = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        super(SendMails, self).save(*args, **kwargs)

        email_list = Subscribe.objects.all()
        mail_subject = self.mailer_to_send.primaryBlog.title

        html_message = loader.render_to_string(
            'mailers/mailer_mail_update_template.html',
            {
                'blog_data': self.mailer_to_send,
            }
        )

        # Manual opening of connection to avoid connection instances
        connection = mail.get_connection()
        SendMails.process_start_time = datetime.now()
        connection.open()

        count = 0
        exceptions = 0
        while count < len(email_list):
            try:
                msg = mail.EmailMessage(mail_subject, html_message, 'news@adurcup.com', [email_list[count]],
                                        connection=connection)
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
                count += 1
            except:
                exceptions += 1
                pass

        connection.close()
        SendMails.process_finish_time = datetime.now()
        SendMails.mails_sent = count
        SendMails.exceptions = exceptions
