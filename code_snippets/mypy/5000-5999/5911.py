INSTALLED_APPS = ('app1', 'app2')

from django.db import models

class User(models.Model):
    member = models.ForeignKey(to='app1.Model1')

