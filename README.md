# moc-gui-plugins
Plugin architecture for The Mass Open Cloud GUI

#Install and Run a HaaS Server
1. Clone HaaS: \n
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

