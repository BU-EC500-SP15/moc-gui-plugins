# moc-gui-plugins
##Plugin architecture for The Mass Open Cloud GUI

###Install and Run HaaS UI

1. Clone Haas UI into the folder of your choice: 
<pre>
    $git clone https://github.com/BU-EC500-SP15/moc-gui-plugins
</pre>
2. Create a new virtual environment using virtualenv
<pre>
    $virtualenv venv
</pre>
You may replace 'venv' with a name of your choice, but remember to do so for the entire tutorial.
3. Enter this virtual environment using 
<pre>
        $source venv/bin/activate
</pre>
The path is different if you named the virtualenv differently
4. While the venv is active and in the .git directory for moc-gui-plugins, install necessary libraries
<pre>
        $pip install -r requirements.txt
</pre>
5. Start the Haas Plugin server locally
<pre>
$python manage.py runserver
</pre>
We recommend using python version 2.7



#Install and Run a HaaS Server
1. Clone HaaS:

    git clone https://github.com/CCI-MOC/haas

2. Install HaaS:

    cd haas
    
    sudo python setup.py install

3. Create a system user called "haas_user":

    sudo useradd haas_user -d /var/lib/haas -m -r

4. Create a HaaS configuration file:

    haas.cfgcontains settings for both the CLI client and the server. Copy one of the haas.cfg* files in examples/ into:
    
      a. haas main directory
      
      b. /etc

5. Create a symlink to the haas cfg in the HaaS user's home directory:

    sudo ln -s /etc/haas.cfg /var/lib/haas/ 

6. Intialize the HaaS Database:
    
    haas init_db

