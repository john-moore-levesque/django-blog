from django import forms
from blog.models import Comment
from antispam.honeypot.forms import HoneypotField


class CommentForm(forms.ModelForm):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!"
            }
        )
    )
    honeypot = HoneypotField()

    class Meta:
        model = Comment
        fields = ('author', 'body', 'honeypot')
