from django import forms

class CreateProjectForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Project name', widget=forms.TextInput(attrs={'required':'required'}))
    action = ''
    back_link = ''
    back_text = ''
    submit = ''
    


class DeleteProjectForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Delete Project')
    action = '/projects/delete'
    back_text = ''
    submit = ''

class CreateNodeForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Node name',  widget=forms.TextInput(attrs={'required':'required'}))
    ipmi_host = forms.CharField(label='IPMI host', widget=forms.TextInput(attrs={'required':'required'}))
    ipmi_user = forms.CharField(label='IPMI user', widget=forms.TextInput(attrs={'required':'required'}))
    ipmi_pass = forms.CharField(label='IPMI pass', widget=forms.TextInput(attrs={'required':'required'}))
    action = ''
    back_link = ''
    back_text = ''
    submit = ''

class DeleteNodeForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Delete Node', widget=forms.TextInput(attrs={'required':'required'}))
    action = ''
    back_text = ''
    submit = ''

class RegisterNodeNicForm(forms.Form):
    """description of class"""
    nic = forms.CharField(label='NIC name', widget=forms.TextInput(attrs={'required':'required'}))
    macaddr = forms.CharField(label='Mac Address', widget=forms.TextInput(attrs={'required':'required'}))
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
    name = forms.CharField(label='Headnode Name',  widget=forms.TextInput(attrs={'required':'required'}))
    base_img = forms.CharField(label='Base Image',  widget=forms.TextInput(attrs={'required':'required'}))
    project = forms.CharField(label='Project', widget=forms.TextInput(attrs={'required':'required'}))
    action = '/headnode/create/'
    back_link = '/projects/details/'
    back_text = ''
    submit = ''

class AddHNICForm(forms.Form):

    """description of class"""

    hnic = forms.CharField(label='HNIC Name',  widget=forms.TextInput(attrs={'required':'required'}))

    action = ''

    back_link = ''

    back_text = ''

    submit = ''

class CreateNetworkForm(forms.Form):
    """description of class"""
    network = forms.CharField(label='Network name', widget=forms.TextInput(attrs={'required':'required'}))    
    action = ''
    back_link = ''
    back_text = ''
    submit = ''

class DeleteHeadnodeForm(forms.Form):
    headnode = forms.CharField(label='Headnode', widget=forms.TextInput(attrs={'required':'required'}))
    project = forms.CharField(label='Project', widget=forms.TextInput(attrs={'required':'required'}))
    action = ''
    back_link = ''
    back_text = ''
    submit = ''

class DeleteNetworkForm(forms.Form):
    name = forms.CharField(label='Delete Network')
    action = '/networks/delete'
    back_text = ''
    submit = ''
