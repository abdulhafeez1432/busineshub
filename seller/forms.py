from django import forms
from .models import *
from multiupload.fields import MultiFileField


class SellerProfileForm(forms.ModelForm):

    class Meta:
        model = SellerProfile
        #fields = ("",)
        exclude = ('user', 'created_at', 'updated_at', )


class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('approval', 'user', 'created_at', 'updated_at',)


class AboutBusinessForm(forms.ModelForm):
    class Meta:
        model = AboutBusiness
        exclude = ('business', 'created_at', 'updated_at',)


class DocumentBusinessForm(forms.ModelForm):
    #document = MultiFileField(required=False)

    class Meta:
        model = BusinessDocument
        exclude = ('business', 'created_at', 'updated_at',)


class TargetBusinessForm(forms.ModelForm):
    class Meta:
        model = BusinessTarget
        exclude = ('business', 'created_at', 'updated_at',)


class StaffBusinessForm(forms.ModelForm):
    class Meta:
        model = BusinesStaff
        exclude = ('business', 'created_at', 'updated_at',)


class FinancialBusinessForm(forms.ModelForm):
    class Meta:
        model = BusinessFinancial
        exclude = ('business', 'created_at', 'updated_at',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_at', 'updated_at',)
