from django import forms
from learning_logs.models import Topic
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

# 这是一个 Git 测试改动
