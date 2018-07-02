from django import forms


class ResidentCheckForm(forms.Form):
    cottage_number = forms.CharField(help_text="Enter a cottage number.",max_length="5")
    cottage_key = forms.CharField(help_text="Enter cottage passkey.",max_length="50")