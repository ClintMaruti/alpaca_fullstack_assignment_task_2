from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    group = models.models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Posts(models.Model):
    post = models.CharField(_("Post"), max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    created_on = models.DateField(_("Created On"), auto_now=True, auto_now_add=True)
    class Meta:
        ordering = ['post']

    def __str__(self):
        return "%s %s" % (self.post, self.user)

class Group(models.Model):
    group_name = models.CharField( max_length=50)
    group_founder = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.group_name
    

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "%s %s" % (self.name, self.body)
    