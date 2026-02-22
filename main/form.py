from django import forms
from main import models as m1
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = m1.ContactModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'contact-input',
                'placeholder':'Enter Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class':'contact-input',
                'placeholder': 'Enter Your Email',
            }),
            'message': forms.Textarea(attrs={
                'class' : 'contact-input',
                'placeholder' : 'Enter Your Message',
            })
        }