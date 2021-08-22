from django import forms

class EmailForm(forms.Form):
  first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
  last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
  email = forms.EmailField(max_length=120, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
  body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
