from django.db import models

# Create your models here.

class Listjobs(models.Model):
    title_job = models.TextField(unique=True)
    urls_job = models.TextField(unique=True)
    date_job = models.DateField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return self.title_job

class Listblog(models.Model):
    title_blog = models.TextField(primary_key=True)
    
    def __str__(self):
        return self.title_blog

class Content(models.Model):
    name_content = models.TextField()
    title_content = models.ForeignKey(Listblog, default=None, on_delete=models.CASCADE)
    urls_content = models.URLField()

    def __str__(self):
        return '{}'.format(self.title_content)
