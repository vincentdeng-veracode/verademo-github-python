from django.forms import ModelForm, inlineformset_factory, CharField, TextInput
from .models import Question, Choice


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': TextInput(attrs={'class': 'form-control'}),
        }


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': TextInput(attrs={'class': 'form-control'}),
        }


ChoicesFormSet = inlineformset_factory(Question, Choice, fields=('choice_text',), form=ChoiceForm, extra=3, can_delete=False)
