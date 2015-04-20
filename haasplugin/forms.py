from django import forms

class CreateProjectForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Project name')
    action = ''
    back_link = ''
    back_text = ''
    submit = ''
    


class DeleteProjectForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Delete Project')
    action = '/projects/delete'
    back_text = 'Cancel'
    submit = 'Delete'

class CreateNodeForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Node name')
    ipmi_host = forms.CharField(label='IPMI host')
    ipmi_user = forms.CharField(label='IPMI user')
    ipmi_pass = forms.CharField(label='IPMI pass')
    action = ''
    back_link = ''
    back_text = ''
    submit = ''

class AllocateNodeForm(forms.Form):
    node_name = forms.CharField(widget=forms.HiddenInput())
    action = ''
    submit = ''
    back_text = ''

class DetachNodeForm(forms.Form):
    node_name = forms.CharField(widget=forms.HiddenInput())
    submit = "Detach"

class HeadnodeForm(forms.Form):
    name = forms.CharField(label='Headnode Name')
    base_img = forms.CharField(label='Base Image')
    project = forms.CharField(label='Project')
    action = '/headnode/create/'
    back_link = '/projects/details/'
    back_text = 'Cancel'
    submit = 'Create'


