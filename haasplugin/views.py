from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from haasplugin.forms import *



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
	return render(request, 'projectdetails.html', {'project': project})


def createProject(request):
	"""
	List keystone projects available to the user; 
	attempt to login with credentials
	"""
	if request.method == "POST":
                form = ProjectForm(request.POST)
                if form.is_valid():
                        projectname = form.cleaned_data["projectname"]
                        project = {'name':projectname, 'status':'OFF'}
                        projects = [{'name':'Project 1', 'status':'ON'}, {'name':'Project 2', 'status':'OFF'}, {'name':'Project 3', 'status':'ON'}, {'name':'Project 4', 'status':'OFF'}]       
                        projects.append(project)
                        return render(request, 'projects.html', {'projects': projects})
    
	return render(request, "createProject.html")


def allocNodes(request, name):
	"""
	List keystone projects available to the user; 
	attempt to login with credentials

	"""
	project = {'name':name}
	nodes = [{'name':'Node1'}, {'name':'Node2'}, {'name':'Node4'}, {'name':'Node6'}, {'name':'Node15'}, {'name':'Node17'}]
	context = {'project' : project, 'nodes':nodes}
	return render(request, 'allocateNode.html', {'context': context})
