from django import forms

class ProjectForm(forms.Form):
    """description of class"""
    projectname = forms.CharField()


