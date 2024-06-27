from django import forms # type: ignore
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'category', 'active']