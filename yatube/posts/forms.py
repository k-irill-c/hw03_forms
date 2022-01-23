from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(label='Текст поста', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('group', 'text')
