from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text", "group")
        help_texts = {
            "text": "Текст нового поста",
            "group": "Группа, к которой будет относиться пост",
            }
        group = forms.ModelChoiceField(
            queryset=Post.objects.all(),
            required=False, to_field_name="group"
            )
        widgets = {
            'text': forms.Textarea(),
            }
        labels = {
            "text": "Текст поста",
            "group": "Группа",
        }
