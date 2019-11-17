from django.db import models


class Student(models.Model):
    frist_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)



    def __str__(self):
        return self.frist_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message=models.TextField()



    def __str__(self):
        return self.email