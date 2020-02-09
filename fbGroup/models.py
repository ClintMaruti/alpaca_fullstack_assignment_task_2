from django.db import models


# Create your models here.
class User(models.Model):
    """User Model"""
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""
    group_name = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.group_name


class Posts(models.Model):
    """Posts Model"""
    post = models.CharField(max_length=150, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post']

    def __str__(self):
        return "%s %s" % (self.post, self.user)


class Comments(models.Model):
    """Comments Model"""
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "%s %s" % (self.name, self.body)


class Reply(models.Model):
    """ Replies to comments"""
    body = models.CharField(max_length=150, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "%s %s" % (self.name, self.body)
