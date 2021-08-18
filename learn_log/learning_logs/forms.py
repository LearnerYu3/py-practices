from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    # Meta 和 model 拼写一定不能出错
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
