from django.db import models

class User(models.Model):
    member = models.ForeignKey(to='app1.Model1')
