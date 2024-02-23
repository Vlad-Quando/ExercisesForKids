from .models import Texts
from django.forms import ModelForm, TextInput, Textarea, Form, ModelChoiceField
from .models import Texts, Modes


class TextsForm(ModelForm):
    class Meta:
        model = Texts
        fields = ['title', 'text']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название"
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст"
            })}


class SetRunTextParameters(Form):
    modes = ["Перемешать слова", "Слова с конца", "Предложения с конца", "Убрать гласные", "Случайные пробелы"]

    text = ModelChoiceField(queryset=Texts.objects.all())
    mode = ModelChoiceField(queryset=Modes.objects.all())
