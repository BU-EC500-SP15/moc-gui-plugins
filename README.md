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

    haas.cfgcontains settings for both the CLI client and the server. 
    Copy one of the haas.cfg* files in examples/ into:
    
      a. haas main directory
      
      b. /etc

<b>5. Create a symlink to the haas cfg in the HaaS user's home directory:</b>

    $sudo ln -s /etc/haas.cfg /var/lib/haas/

<b>6. Intialize the HaaS Database:</b>
    
    $haas init_db 

<b>7. Run the HaaS server by following the instructions [here]:</b>

    https://github.com/CCI-MOC/haas/blob/master/HACKING.rst

##Install and Run HaaS UI

<b>1. Clone Haas UI into the folder of your choice: </b>

    $git clone https://github.com/BU-EC500-SP15/moc-gui-plugins

<b>2. Create a new virtual environment using virtualenv</b>

    $virtualenv venv

You may replace 'venv' with a name of your choice, but remember to do so for the entire tutorial.

<b>3. Enter this virtual environment using</b>

        $source venv/bin/activate

The path is different if you named the virtualenv differently.

<b>4. While the venv is active and in the .git directory for moc-gui-plugins, install necessary libraries</b>

        $pip install -r requirements.txt

<b>5. Start the Haas Plugin server locally</b>

    $python manage.py runserver 9000
    
We recommend using python version 2.7. You run this on any port except 5000 (HaaS server port) or 8000 (MOC UI port). 

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
    
<b> For more details, refer to the MOC UI page: https://github.com/CCI-MOC/ui.git </b>
