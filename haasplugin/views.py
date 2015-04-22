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
    project_headnodes = requests.get(settings.HAAS_URL + '/project/' + name + '/headnodes')
    project_headnodes = project_headnodes.json()
    headnodes = []
    for proj_hnode in project_headnodes:
       hnode_details = requests.get(settings.HAAS_URL + '/headnode/' + proj_hnode)
       hnode_details = hnode_details.json()
       headnodes.append(hnode_details)
    #hnode = json.dumps(headnodes)
    #hnode_details = requests.get(settings.HAAS_URL + '/headnode/' + hnode)
    #hnode_details = hnode_details.json()
    project = {'name':name, 'project_nodes':project_nodes, 'networks':networks, 'headnodes':project_headnodes}
    
    addHNICForm = AddHNICForm()
    addHNICForm.action = '/projects/'+name+'/hnic_add'

    deleteForm = DeleteProjectForm()
    deleteForm.action = '/project_delete'
    return render(request, 'projectDetails.html', {'project': project, 'nodes': nodes, 'hnodes': headnodes, 'deleteForm': deleteForm, 'addHNICForm': addHNICForm})



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
    node = requests.get(settings.HAAS_URL + '/node_detailed/' + name)
    node = node.json()
    return render(request, 'nodeDetails.html', {'node': node})


def node_powercycle(request, name):
    """
    Power cycles the node
    """
    if request.method == 'POST':
        requests.post(settings.HAAS_URL + '/node/' + name + '/power_cycle')
        return redirect('haasplugin.views.node_details', name)

    payload = {'node':name}
    r = requests.post(settings.HAAS_URL + '/node/' + name + '/power_cycle')
    return redirect('haasplugin.views.node_details', name)

def node_register_nic(request, name):
    """
    List keystone projects available to the user;
    attempt to login with credentials

    """
    if request.method == 'POST':
        form = RegisterNodeNicForm(request.POST)
        if form.is_valid():
            nic = form.cleaned_data['nic']
            macaddr = form.cleaned_data['macaddr']
            payload = {'macaddr':macaddr}
            r = requests.put(settings.HAAS_URL + '/node/' + name + '/nic/' + nic, data = json.dumps(payload))
            if r.status_code == 200:
                return redirect('haasplugin.views.node_details', name)
            else:
                return render(request, 'error.html', {'status': r.status_code })
        else:
           return render(request, 'error.html', {'status': 'form is not valid' })

def node_delete_nic(request, name, nic):
    """
    List keystone projects available to the user;
    attempt to login with credentials

    """
    r = requests.delete(settings.HAAS_URL + '/node/' + name + '/nic/' + nic)
    if r.status_code == 200:
        return redirect('haasplugin.views.node_details', name)
    else:
        return render(request, 'error.html', {'status': r.status_code })

def nodes(request):
    """
    List all nodes available to the user;
    """

    r = requests.get(settings.HAAS_URL + '/nodes')
    all_nodes = r.json()
    nodes = []
    for proj_node in all_nodes:
       node = requests.get(settings.HAAS_URL + '/node/' +proj_node)
       node = node.json()
       nodes.append(node)
    createNode = CreateNodeForm()
    createNode.action = '/node_create'

    context = {'all_nodes':all_nodes,'nodes':nodes, 'createNode':createNode}

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


def network_create(request):
    """

    List keystone projects available to the user;

    attempt to login with credentials

    """
    if request.method == "POST":
        form = CreateNetworkForm(request.POST)
        if form.is_valid():
                network = form.cleaned_data["network"]
                creator = "admin"
                access = "proj"
                net_id = "123"
                payload = {'creator' : creator, 'access' : access, 'net_id' : net_id}
                r = requests.put(settings.HAAS_URL + '/network/' + network, data = json.dumps(payload))
                if(r.status_code == 200):
                    return redirect('haasplugin.views.networks')
                else:
                    return render(request, 'error.html', {'status': r.status_code})

    #createNetwork = CreateNetworkForm()
    #createNetwork.action = "/network_create"
    return render(request, 'createNetwork.html')

def networks(request):
    """
    List all networks;
    """
    r = requests.get(settings.HAAS_URL + '/networks')
    networks = r.json()
    
    createNetwork = CreateNetworkForm()
    createNetwork.action = "/network_create"
    project = {'networks':networks, 'createNetwork': createNetwork }
    
    return render(request, 'networks.html', {'project': project})

def hnic_add(request, name):
    """
    adds a haednic to a headnode
    """
    if request.method == "POST":
        form = AddHNICForm(request.POST)
        if form.is_valid():
                hnode = form.cleaned_data["hnode"]
                hnic = form.cleaned_data["hnic"]
                r = requests.put(settings.HAAS_URL + '/headnode/'+ hnode +'/hnic/' + hnic)
                if(r.status_code == 200):
                    #return
                    return redirect('haasplugin.views.project_details', name)
                else:
                    return render(request, 'error.html', {'status': r})

    #hnic = AddHNICForm()
    #hnic.submit = "Create"
    #hnic.action = "/projects"
    #hnic.back_text = "Cancel"
    #hnic.back_link = "/projects"    

    return render(request, 'error.html', {'status': "page not found. Should not reach here"})




