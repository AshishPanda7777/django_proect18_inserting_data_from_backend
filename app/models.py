from django.db import models

# Create your models here.
class COURSE(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=50)
    def __str__(self):
        return self.cname
class STUDENT(models.Model):
    cid=models.ForeignKey(COURSE,on_delete=models.CASCADE)
    sname=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.sname

   