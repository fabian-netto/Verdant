from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    img_main = models.ImageField()
    img_1 = models.ImageField()
    img_2 = models.ImageField()
    img_3 = models.ImageField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    course_id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    title_1 = models.CharField(max_length=100)
    brief = models.CharField(max_length=200)
    brief_1 = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    img_main = models.ImageField()
    img_1 = models.ImageField()
    img_2 = models.ImageField()
    img_3 = models.ImageField()

    def __str__(self):
        return self.title

class Registrationform(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name
