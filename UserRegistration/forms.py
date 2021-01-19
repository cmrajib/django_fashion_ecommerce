from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms, TextInput

from UserRegistration.models import  User



# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user',)
#
#
# # Appling css class to the field and button
#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'single-input'
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('submit', 'Save', css_class='genric-btn success circle'))



class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('full_name', 'email','password1', 'password2',)
        labels = {
            'full_name': (''),
            'email': (''),
            'password1': (''),
            'password2': (''),
        }
    # Appling css class to the field and button
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['full_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password again'

        # self.fields['full_name'].label = False
        # self.fields['email'].label = False
        # self.fields['password1'].label = False
        # self.fields['password2'].label = False

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['full_name'].widget = TextInput(attrs={
    #         'class': 'form-block',
    #         'placeholder': 'Name'})

# 'single-input'
        # self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Create Account', css_class='genric-btn success circle'))



