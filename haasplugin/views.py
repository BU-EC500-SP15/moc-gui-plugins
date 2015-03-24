from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from haasplugin.forms import *
from django.conf import settings
import requests

def projects(request):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    projects = [{'name':'Project 1', 'status':'ON'}, {'name':'Project 2', 'status':'OFF'}, {'name':'Project 3', 'status':'ON'}, {'name':'Project 4', 'status':'OFF'}]

    return render(request, 'projects.html', {'projects': projects})


def projectDetails(request, name):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    project = {'name':name, 'nodes':[{'name':'Node 1'}, {'name':'Node 2'},{'name':'Node 3'}], 'networks':[{'name':'Network 1', 'accesslevel':'Shared'}]}
    deleteForm = DeleteProjectForm()
    return render(request, 'projectdetails.html', {'project': project, 'deleteForm': deleteForm})


def createProject(request):
    """
    List keystone projects available to the user;
    attempt to login with credentials
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data["name"]
                r = requests.put(settings.HAAS_URL + '/project/' + name)
                #return render(request, 'error.html', {'status': r})
                if(r.status_code == 200):
                    return redirect('haasplugin.views.projects')
                else:
                    return render(request, 'error.html', {'status': r})
    project = ProjectForm()
    
    return render(request, 'createProject.html', {'project': project})

def deleteProject(request):
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




def allocNodes(request, name):
    """
    List keystone projects available to the user;
    attempt to login with credentials

    """
    project = {'name':name}
    nodes = [{'name':'Node1'}, {'name':'Node2'}, {'name':'Node4'}, {'name':'Node6'}, {'name':'Node15'}, {'name':'Node17'}]
    context = {'project' : project, 'nodes':nodes}
    return render(request, 'allocateNode.html', {'context': context})


def allNodes(request):
    """
    List all nodes available to the user;
    """
    nodes = [{'name':'Node1'}, {'name':'Node2'}, {'name':'Node4'}, {'name':'Node6'}, {'name':'Node15'}, {'name':'Node17'}]
    context = {'nodes':nodes}
    return render(request, 'viewAllNodes.html', {'context': context})

