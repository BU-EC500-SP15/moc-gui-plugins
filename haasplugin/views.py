from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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
	images = [{'name':'Ubuntu'}, {'name':'Centos'}, {'name':'Windows'}]

	return render(request, 'createProject.html', {'baseimages', images})
