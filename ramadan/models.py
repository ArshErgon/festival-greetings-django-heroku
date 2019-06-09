from django.db import models


class Greeter_Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Festival_Info(models.Model):
     text2 = models.TextField()
     text1 = models.TextField()

     def __str__(self):
         return "%s -- %s" % (self.text1, self.text2)
