from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.title
class Skill(models.Model):
    name = models.CharField(max_length=100)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    year = models.IntegerField()

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    link = models.URLField(blank=True)
