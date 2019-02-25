from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Post, LeaveApplication, ExpenseApplication, Announcement


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {'text': forms.Textarea(attrs={'rows':   5, 'cols': 100, 'style': 'resize:none;'})}


class LeaveForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ('reasons', 'subject', 'text', 'from_date', 'to_date')
        widgets = {'text': forms.Textarea(attrs={'rows': 5, 'cols': 100, 'style': 'resize:none;'}),
                   'from_date': DatePickerInput(),
                   'to_date': DatePickerInput()
                   }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseApplication
        fields = ('subject', 'text', 'date','amount' ,'file')
        widgets = {'text': forms.Textarea(attrs={'rows': 5, 'cols': 100, 'style': 'resize:none;'}),
                   'date': DatePickerInput(),
                   }

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'text')
        widgets = {'text': forms.Textarea(attrs={'rows': 5, 'cols': 100, 'style': 'resize:none;'}),

                   }