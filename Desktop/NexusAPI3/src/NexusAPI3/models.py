'''
Created on 2020/09/20

@author: shung
'''
from django.db import models

class User(models.Model):
    class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "User"
        db_table = "user"

    user_id = models.AutoField(verbose_name = "user_id", primary_key = True)
    user_name = models.CharField("user_name", max_length = 255)
    def __str__(self):
        return self.user_name