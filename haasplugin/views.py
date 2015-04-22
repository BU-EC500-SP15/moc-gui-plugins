from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from haasplugin.forms import *
from django.conf import settings
import requests
import json

def projects(request):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    r = requests.get(settings.HAAS_URL + '/projects')
    projects = r.json()
    createProject = CreateProjectForm()
    #createProject.submit = "Create"
    createProject.action = "/project_create"
    #createProject.back_text = "Cancel"
    return render(request, 'projects.html', {'projects': projects, 'createProject':createProject})


def project_details(request, name):
    """
    Get Project details
    """
    project_nodes = requests.get(settings.HAAS_URL + '/project/' + name + '/nodes')
    project_nodes = project_nodes.json()
    nodes = []
    for proj_node in project_nodes:
       node = requests.get(settings.HAAS_URL + '/node/' +proj_node)
       node = node.json()
       nodes.append(node)

    networks = requests.get(settings.HAAS_URL + '/project/' + name + '/networks')
    networks = networks.json()
    headnodes = requests.get(settings.HAAS_URL + '/project/' + name + '/headnodes')
    headnodes = headnodes.json()

    project = {'name':name, 'project_nodes':project_nodes, 'networks':networks, 'headnodes':headnodes}
    
    deleteForm = DeleteProjectForm()
    deleteForm.action = '/project_delete'
    return render(request, 'projectDetails.html', {'project': project, 'nodes': nodes, 'deleteForm': deleteForm})


def project_create(request):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data["name"]
                r = requests.put(settings.HAAS_URL + '/project/' + name)
                if(r.status_code == 200):
                    return redirect('haasplugin.views.projects')
                else:
                    return render(request, 'error.html', {'status': r})
    project = CreateProjectForm()
    project.submit = "Create"
    project.action = "/projects/create"
    project.back_text = "Cancel"
    project.back_link = "/projects"
    
    return render(request, 'createProject.html', {'project': project})

def project_delete(request):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    if request.method == "POST":
        form = DeleteProjectForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data["name"]
                
                r = requests.delete(settings.HAAS_URL + '/project/' + name)
                if(r.status_code == 200):
                    return redirect('haasplugin.views.projects')
                else:
                    return render(request, 'error.html', {'status': r.status_code })

   
    return render(request, 'error.html', {'status': ''})

def headnode(request):
    """
    Show the headnode of a project
    """
    headnode = [{'name':'headNode1'}]
    return render(request, headnode)


def headnode_create(request):
    """
    Create the headnode of a project
    """
    name = ""
    base_img = ""
    project = ""
    if request.method == "POST":
        form = HeadnodeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            base_img = form.cleaned_data['base_img']
            project = form.cleaned_data['project']
            context = {'project':project, 'base_img':base_img}
            r = requests.put(settings.HAAS_URL + '/headnode/' + name, data = json.dumps(context))
            if(r.status_code == 200):
                return redirect('haasplugin.views.project_details', project)
            else:
                return render(request, 'error.html', {'status': r})
    headnode = HeadnodeForm()
    given = {'form':headnode, 'project':project}
    return render(request, 'createHeadnode.html', {'headnode':headnode})


def allocate_node(request, name):
    """
    List keystone projects available to the user;
    attempt to login with credentials

    """
    node_name = ""
    if request.method == 'POST':
        form = AllocateNodeForm(request.POST)
        if form.is_valid():
            node_name = form.cleaned_data['node_name']
            payload = {'node':node_name}
            r = requests.post(settings.HAAS_URL + '/project/' + name + '/connect_node', data = json.dumps(payload))
            if r.status_code == 200:
                return redirect('haasplugin.views.project_details', name)
        else:
           return render(request, 'error.html', {'status': 'form is not valid' })

    project = {'name':name}
    nodes = requests.get(settings.HAAS_URL + '/free_nodes')
    nodes = nodes.json()
    context = {'project' : project, 'nodes':nodes}
    return render(request, 'allocateNode.html', {'context': context, 'nnode': node_name})

def detach_node(request, name):
    """
    Detaches the node from the specified project

    """
    if request.method == 'POST':
        form = DetachNodeForm(request.POST)
        if form.is_valid():
            node_name = form.cleaned_data['node_name']
            #return render(request, 'error.html', {'status': node_name })
            payload = {'node':node_name}
            r = requests.post(settings.HAAS_URL + '/project/' + name + '/detach_node', data = json.dumps(payload))
            if r.status_code == 200:
                return redirect('haasplugin.views.project_details', name)
            else:
                return render(request, 'error.html', {'status': r.status_code})
        else:
            return render(request, 'error.html', {'status': 'form is not valid' })
    return redirect('haasplugin.views.project_details', name)


def node_details(request, name):
    """
    Show node details: Name, Availabiltiy, Associated NICs
    """
    node = requests.get(settings.HAAS_URL + '/node/' + name)
    node = node.json()
    return render(request, 'nodeDetails.html', {'node': node})


def nodes(request):
    """
    List all nodes available to the user;
    """

    r = requests.get(settings.HAAS_URL + '/nodes')
    nodes = r.json()

    createNode = CreateNodeForm()
    createNode.action = '/node_create'

    context = {'nodes':nodes, 'createNode':createNode}

    return render(request, 'nodes.html', {'context': context})

def node_create(request):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    if request.method == "POST":
        form = CreateNodeForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data["name"]
                ipmi_host = form.cleaned_data["ipmi_host"]
                ipmi_user = form.cleaned_data["ipmi_user"]
                ipmi_pass = form.cleaned_data["ipmi_pass"]
                payload = {'ipmi_host' : ipmi_host, 'ipmi_user' : ipmi_user, 'ipmi_pass' : ipmi_pass}
                r = requests.put(settings.HAAS_URL + '/node/' + name, data = json.dumps(payload))
                if(r.status_code == 200):
                    return redirect('haasplugin.views.nodes')
                else:
                    return render(request, 'error.html', {'status': "node_create"})

    createNode = CreateNodeForm()
    createNode.action = "/node_create"
    return render(request, 'createNode.html', {'createNode': createNode})


def networks(request):
    """
    List all networks;
    """
    r = requests.get(settings.HAAS_URL + '/networks')
    networks = r.json()
    project = {'networks':networks}
    return render(request, 'viewAllNetworks.html', {'project': project})


