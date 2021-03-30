from django import forms
from django.contrib.auth import get_user_model
from .models import Post, Comment


User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', ]

    # methods clean use for custom data validation
    # def clean_title(self):
    #     if 'Python' not in self.data['title']:
    #         raise forms.ValidationError("Can't create post without Python!")
    #     return self.data['title']
    #
    # def clean(self, **kwargs):
    #     return super(self).clean(**kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text', ]
