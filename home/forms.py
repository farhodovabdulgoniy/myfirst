from django import forms 
from home.models import ContactMessage
from django.forms import TextInput,Textarea,EmailInput


# class SearchForm(forms.Form):

#     query = forms.CharField(max_length=255)
#     catid = forms.IntegerField()


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage
        fields = ('name','email','subject','message')
        widgets = {
            'name':TextInput(attrs={'class':'input','placeholder':'Name'}),
            'subject':TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'email':EmailInput(attrs={'class':'input','placeholder':'Email Address'}),
            'message':Textarea(attrs={'class':'input','placeholder':'Your Message','rows':'5'})
        }
    