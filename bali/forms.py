from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
#    c = forms.IntegerField()


class ExtractForm(forms.Form)
    