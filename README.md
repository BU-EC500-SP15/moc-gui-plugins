# moc-gui-plugins
Plugin architecture for The Mass Open Cloud GUI

##Install and Run a HaaS Server
1. Clone HaaS:

    <pre> $git clone https://github.com/CCI-MOC/haas </pre>

2. Install HaaS:

    <pre> $cd haas </pre>
    
    <pre> $sudo python setup.py install </pre>

3. Create a system user called "haas_user":

    </pre> $sudo useradd haas_user -d /var/lib/haas -m -r </pre>

4. Create a HaaS configuration file:

    haas.cfgcontains settings for both the CLI client and the server. Copy one of the haas.cfg* files in examples/ into:
    
      a. haas main directory
      
      b. /etc

5. Create a symlink to the haas cfg in the HaaS user's home directory:

    <pre>$sudo ln -s /etc/haas.cfg /var/lib/haas/ </pre>

6. Intialize the HaaS Database:
    
    <pre> $haas init_db </pre>

7. Run the HaaS server by following the instructions [here]:

    https://github.com/CCI-MOC/haas/blob/master/HACKING.rst

