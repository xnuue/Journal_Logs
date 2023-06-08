# File creates a form with the required inputs we need from the user

from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """class adds a field which let users add a new topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """class allow users enter new entries to the new topics added"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
