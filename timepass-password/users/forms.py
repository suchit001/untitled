import datetime
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        now = datetime.datetime.now()
        fields = ('username', 'email', 'gender', 'security_question', 'answer', 'contact_number' ,'birth_date', 'emergency_contact_name', 'emergency_contact_number',
                  'blood_group','resume','address',
                  )
        widgets={
            'birth_date' :DatePickerInput(
                options={
                    'maxDate':str(datetime.datetime.now()),
                }
            ),
            'address': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'style': 'resize:none;'}),
        }
        help_texts={
            'email':'Enter valid email address',
            'resume' : 'You can add resume later',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['resume'].required = False

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
