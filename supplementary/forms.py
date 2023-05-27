from django import forms
from .models import Supplementary

class monitoringWorkshopForm(forms.ModelForm):
    class Meta:
        model = Supplementary
        fields = ["monitoring","workshop"]