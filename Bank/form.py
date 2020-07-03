from django import forms
from Bank.models import banks,Branch
class BankViewForm(forms.ModelForm):
    class Meta():
        model = Branch
        fields = '__all__'
