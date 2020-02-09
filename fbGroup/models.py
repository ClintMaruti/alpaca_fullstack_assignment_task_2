from django.db import models


# Create your models here.
class User(models.Model):
    """User Model"""
    first_name = models.CharField('first Name', max_length=150, null=False)
    last_name = models.CharField('last Name', max_length=150, null=False)
    created_on = models.DateTimeField('date Created', auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""
    group_name = models.CharField('group Name', max_length=50, null=False)
    created_on = models.DateTimeField('created On', auto_now_add=True)
    user = models.ManyToManyField(User, related_name='groups')

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.group_name


class Post(models.Model):
    """Posts Model"""
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_on = models.DateTimeField('date created', auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return "%s %s" % (self.body, self.user)


class Comment(models.Model):
    """Comments Model"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return "%s %s" % (self.user, self.body)


class Reply(models.Model):
    """ Replies to comments"""
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'reply'
        verbose_name_plural = 'replies'

    def __str__(self):
        return "%s %s" % (self.user, self.body)
