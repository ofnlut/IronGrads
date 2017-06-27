from django import forms

from .models import Graduate
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Graduate
        fields = ('first_name','last_name','job_title','Email','Github','Linkedin')
