from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Post(models.Model):
    """ Base Post model. """

    # id - is automatic field
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', max_length=120, null=True, blank=True)
    # upload_to - folder name in folder media, will be created if not exist
    # max_length - length of file name, type varchar in DB
    # null - value for DB, can be empty
    # blank - value for django forms (admin or other pages), post can be without picture
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

        # if there are no realized Filter in core/admin.py
        # author = (
        #     f'{self.author.first_name} {self.author.last_name}'
        #     if self.author.first_name and self.author.last_name
        #     else self.author
        # )
        # return f'{author} | {self.title}'


class Comment(models.Model):
    """ Base Comment model. """

    # id - is automatic field
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
