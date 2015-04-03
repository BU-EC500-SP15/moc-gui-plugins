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
    return render(request, 'projects.html', {'projects': projects})


def project_details(request, name):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    nodes = requests.get(settings.HAAS_URL + '/project/' + name + '/nodes')
    nodes = nodes.json()
    networks = requests.get(settings.HAAS_URL + '/project/' + name + '/networks')
    networks = networks.json()
    project = {'name':name, 'nodes':nodes, 'networks':networks}
    
    deleteForm = DeleteProjectForm()
    return render(request, 'projectDetails.html', {'project': project, 'deleteForm': deleteForm})


def project_create(request):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data["name"]
                r = requests.put(settings.HAAS_URL + '/project/' + name)
                if(r.status_code == 200):
                    return redirect('haasplugin.views.projects')
                else:
                    return render(request, 'error.html', {'status': r})
    project = ProjectForm()
    
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


def nodes(request):
    """
    List all nodes available to the user;
    """
    nodes = [{'name':'Node1'}, {'name':'Node2'}, {'name':'Node4'}, {'name':'Node6'}, {'name':'Node15'}, {'name':'Node17'}]
    context = {'nodes':nodes}
    return render(request, 'viewAllNodes.html', {'context': context})

def networks(request):
    """
    List all networks;
    """
    networks = [{'name':'Network1','accesslevel':'Shared'},{'name':'Network2','accesslevel':'Private'}, {'name':'Network5','accesslevel':'Shared'}, {'name':'Network12','accesslevel':'Public'}]
    project = {'networks':networks}
    return render(request, 'viewAllNetworks.html', {'project': project})

