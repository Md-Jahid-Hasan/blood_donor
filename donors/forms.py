from django import forms
from .models import DonorDetails
import datetime


class DonorDetailsForm(forms.ModelForm):
    class Meta:
        model = DonorDetails
        fields = '__all__'
        exclude = ('user', 'is_available')

        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-control form-control-chosen',
                                               'data-placeholder': 'Enter Your Blood Group'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Blood Group'}),
            'present_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Blood Group'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Blood Group'}),
            'specific_area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Blood Group'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Blood Group'}),
            'last_date_of_donation': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Enter your current organization'})
        }

        labels = {
            'blood_group': 'Enter Your Blood Group',
            'district': 'Enter Your District',
        }

        help_texts = {
            'organization': 'Please provide valid organization name. It will help you to find shortly. Take care '
                            'about spelling.',
        }

    def clean(self):
        d_date = self.cleaned_data['last_date_of_donation']
        if d_date > datetime.date.today():
            raise forms.ValidationError("This is not a valid date.")


class SearchDonorForm(forms.Form):
    blood_group = forms.ChoiceField(choices=DonorDetails.BLOOD_GROUP, help_text="This field is mandatory",
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    district = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    specific_area = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    organization = forms.CharField(required=False, help_text="Please enter Organisation name correctly. It help you to"
                                                             " find donor of your organisation.",
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))


