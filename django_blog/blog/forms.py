from django.forms import ModelForm
from django import forms
from taggit.forms import TagWidget
from taggit.models import Tag
from .models import Post, Comment

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
