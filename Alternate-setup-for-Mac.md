# moc-gui-plugins
Plugin Architecture for the Mass Open Cloud GUI, Alternate Setup


##Install and Run a HaaS Server
<b>1. Open terminal (1) and clone the HaaS repo:</b>

    $git clone https://github.com/CCI-MOC/haas.git

<b>2. Create a HaaS configuration file:</b>

haas.cfg contains settings for both the CLI client and the server. Copy haas.cfg.dev-no-hardware file in examples/ into:
    
      a. haas main directory (the super directory of /examples/)

      b. rename the file to haas.cfg


<b>3. Create a new virtual environment using virtualenv</b>

This setup requires having the virtual environment directory inside of the haas directory.

<pre>
    $cd haas

    $virtualenv venv
</pre>

You may replace 'venv' with a name of your choice for [env-name], but remember to use the same virtual environment for the entire setup.

<b>3. Enter this virtual environment using:</b>
<pre>
    $source venv/bin/activate
</pre>
The path is different if you named the virtualenv differently.

<b>4. Install necessary files</b>
    
<pre>
    $pip install -e .
</pre>

<b>5. Intialize the HaaS Database:</b>
    
<pre>
    $haas init_db 
</pre>

Open a new terminal (2). Go back to the haas directory and reactivate the virtual environment.

<b>5. Run the HaaS Server</b>
<pre>
    $haas serve
</pre>

Open another new terminal (3). Go back to the haas directory and reactivate the virtual environment.

<b>6. Run the HaaS Server Networks</b>
<pre>
    $haas serve_networks
</pre>

The HaaS server should be up and running, and ready to interface with REST calls from the HaaS UI.

##Install and Run HaaS UI

<b>1. Open a new terminal (4).

<b>2. Clone Haas UI into the directory of your choice, but preferably in the same location as haas: </b>
<pre>
    $git clone https://github.com/BU-EC500-SP15/moc-gui-plugins.git
</pre>

<b>3. Reactivate the virtual environment in this terminal. Then go back to the moc-gui-plugins directory.

</b>

<b>4. Install Django </b>
<pre>
    $pip install django
</pre>

<b>5. Start the Haas Plugin server locally</b>
<pre>
    $python manage.py runserver 9000
</pre>
We recommend using python version 2.7. Technically, you can run this on any port except 5000, which is reserved for HaaS server, and 8000, which is reserved for the MOC UI Django project by default.

<b>6. Errors </b>

At this point, if you get errors it might be because there are additional functional HaaS APIs added for the HaaS UI but they're not currently implemented in HaaS. 

To fix this, go to the moc-gui-plugins directory. Go to "for new haas", and copy the two files: api.py, cli.py. Go to the haas directory. Go into the second haas directory. Copy these files into this directory. This operation updates the HaaS API and CLI.

These files are not actually updated while the HaaS server is running. Stop them, then deactivate the virtual environment (with $deactivate). Restart the virtual environment and get the server and server-networks running again.

## Setup and Run the MOC UI

<b>1. Clone the MOC UI repo </b>
    
    a. open a new terminal (5)

    b. git clone https://github.com/BU-EC500-SP15/ui.git

<b>2. Start a Django Project </b>

    a. activate the virtual environment again for this terminal

    b. go back to the ui/ directory
    
    c. install requirements using "$pip install -r requirements.txt"
    
    d. create database with "./syncdb.sh"

    e. create folder to hold session ids with "mkdir session"

    f. run server with "./runserver.sh"
    
<b> 3. Run the UI </b>

Note: These steps may not be necessary.

    a. open browser and point it to localhost:8000

    b. Register as a new user
    
<b> For more details, refer to the MOC UI page: https://github.com/CCI-MOC/ui</b>
