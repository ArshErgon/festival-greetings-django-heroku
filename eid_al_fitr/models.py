from django.db import models

class Eid_Greeter_Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Add_Eid_Info(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()

    def __str__(self):
        return "%s %s" % (self.text1, self.text2)

    
