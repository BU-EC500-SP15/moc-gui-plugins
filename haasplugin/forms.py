from django import forms

class ProjectForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Project name')
    action = '/projects/create'
    back_link = '/projects'
    back_text = 'Cancel'
    submit = 'Create'


