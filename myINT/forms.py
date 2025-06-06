from django import forms

from myINT.models import LogMessage


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)
