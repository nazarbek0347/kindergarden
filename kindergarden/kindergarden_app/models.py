from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=200,blank=False)
    teacher_age=models.IntegerField(blank=False)

    def __str__(self):
        return self.teacher_name

class Kid(models.Model):
    kid_name=models.CharField(max_length=200,blank=False)
    kid_age=models.IntegerField(blank=False)
    kid_parents=models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.kid_name