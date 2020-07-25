from django import forms
from .models import MonthlyTotalDonate


class MonthlyDonationChart(forms.Form):

    y = MonthlyTotalDonate.objects.all().order_by().values_list('year', flat=True).distinct('year')
    print(y)
    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    month = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    test = forms.CharField()