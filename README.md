# moc-gui-plugins
Plugin architecture for The Mass Open Cloud GUI

##Install and Run a HaaS Server
<b>1. Clone the HaaS repo:</b>

    $git clone https://github.com/CCI-MOC/haas

<b>2. Install HaaS:</b>

     $cd haas
    
     $sudo python setup.py install

<b>3. Create a system user called "haas_user": </b>

    $sudo useradd haas_user -d /var/lib/haas -m -r

<b>4. Create a HaaS configuration file:</b>

    haas.cfgcontains settings for both the CLI client and the server. Copy one of the haas.cfg* files in examples/ into:
    
      a. haas main directory
      
      b. /etc

<b>5. Create a symlink to the haas cfg in the HaaS user's home directory:</b>

    $sudo ln -s /etc/haas.cfg /var/lib/haas/

<b>6. Intialize the HaaS Database:</b>
    
    $haas init_db 

<b>7. Run the HaaS server by following the instructions [here]:</b>

    https://github.com/CCI-MOC/haas/blob/master/HACKING.rst


## Setup and Run the MOC UI

<b>1. Clone the MOC UI repo </b>
    
    git clone https://github.com/BU-EC500-SP15/ui.git

<b>2. Start a Django Project </b>

    a. create python virtual enviornment using "virtualenv [env-name]"
    
    b. source environment using "source [env-name]/bin/activate"
    
    c.install requirements using "pip install -r requirements.txt"
    
    d. create database with "./syncdb.sh"

    e. create folder to hold session ids with "mkdir session"

    f. run server with "./runserver.sh"
    
<b> 3. Run the UI </b>

    a. open browser and point it to localhost:8000

    b. Register as a new user
