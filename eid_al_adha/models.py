from django.db import models

# Create your models here.
class Bakra_Name_Model(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Add_Bakra_Info(models.Model):
    text1 = models.TextField
    text2 = models.TextField()

    def __str__(self):
        return "%s === %s" % (self.text1, self.text2)
