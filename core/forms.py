from django.contrib.auth.models import User
from django import forms
from .models import Whishlist,Applied,Interview,Offer,Rejected
from django.core.exceptions import ValidationError


class WhishlistForm(forms.ModelForm):
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Role"}), required=True)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Company Name"}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Location"}), required=True)
    basic_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Basic Salary"}), required=True)
    closing_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control',"placeholder": "Closing Date"}), required=True)
    move_to_applied = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input',"placeholder": "Move To Applied"}),required=False)

    def __init__(self, *args, **kwargs):
        super(WhishlistForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            del self.fields['move_to_applied']

    class Meta:
        model = Whishlist
        fields = ['role', 'company_name', 'location', 'basic_salary', 'closing_date','move_to_applied']

class AppliedForm(forms.ModelForm):
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Role"}), required=True)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Company Name"}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Location"}), required=True)
    basic_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Basic Salary"}), required=True)
    closing_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control',"placeholder": "Closing Date"}), required=True)
    # radio button for move to rejected or move to interview

    move_to_rejected = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input',"placeholder": "Move To Rejected"}),required=False)
    move_to_interview = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input',"placeholder": "Move To Interview"}),required=False)

    

    def __init__(self, *args, **kwargs):
        super(AppliedForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            del self.fields['move_to_rejected']
            del self.fields['move_to_interview']
    def clean(self):
        cleaned_data = super().clean()
        move_to_rejected = cleaned_data.get('move_to_rejected')
        move_to_interview = cleaned_data.get('move_to_interview')

        if move_to_rejected and move_to_interview:
            self.add_error('move_to_interview', "You can only select either 'Move To Rejected' or 'Move To Interview', not both.")

    class Meta:
        model = Applied
        order_by = ['-created_at']
        fields = '__all__'
        exclude = ['created_by','created_at','updated_at']
       

class InterviewForm(forms.ModelForm):
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Role"}), required=True)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Company Name"}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Location"}), required=True)
    basic_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Basic Salary"}), required=True)
    interview_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control',"placeholder": "Closing Date"}), required=True)
    move_to_offer = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input',"placeholder": "Move To Offer"}),required=False)
    move_to_rejected = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input',"placeholder": "Move To Rejected"}),required=False)

    def __init__(self, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            del self.fields['move_to_offer']
            del self.fields['move_to_rejected']
    def clean(self):
        cleaned_data = super().clean()
        move_to_offer = cleaned_data.get('move_to_offer')
        move_to_rejected = cleaned_data.get('move_to_rejected')

        if move_to_offer and move_to_rejected:
            self.add_error('move_to_rejected', "You can only select either 'Move To Rejected' or 'Move To Offer', not both.")
    
    class Meta:
        model = Interview
        fields = ['role', 'company_name', 'location', 'basic_salary', 'interview_date', 'move_to_offer','move_to_rejected']

class OfferForm(forms.ModelForm):
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Role"}), required=True)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Company Name"}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Location"}), required=True)
    basic_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Basic Salary"}), required=True)
    joining_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class': 'form-control',"placeholder": "Joining Date"}), required=True)

    class Meta:
        model = Offer
        fields = ['role', 'company_name', 'location', 'basic_salary', 'joining_date']
        
class RejectedForm(forms.ModelForm):
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Role"}), required=True)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Company Name"}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Location"}), required=True)
    basic_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Basic Salary"}), required=True)

    class Meta:
        model = Rejected
        fields = ['role', 'company_name', 'location', 'basic_salary']