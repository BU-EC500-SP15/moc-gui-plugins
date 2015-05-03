moc-gui-plugins
Plugin architecture for The Mass Open Cloud GUI
===============================================

#Run the HaaS Server
	Go to the HaaS directory
		$cd ~/haas
	
	The first time you start working in the repository, set up a clean test environment:
		$virtualenv .venv

	Next, each time you start working, enter the environment:
		$source .venv/bin/activate

	Then, proceed with installing the HaaS and its dependencies into the virtual environment:
		$pip install -e .
	
	Run the server with
		$haas serve 
	
	Then, run the networks server in a new terminal:
	
	Go to the HaaS directory
		$cd ~/haas

	enter the environment:
		$source .venv/bin/activate

	start the networks with
		$haas serve_networks

------------------------------------------------------

#Run the HaaS UI Server

	Go to the moc-gui-plugins directory
		$cd ~/MOCUI

	Start the Moc UI's virtual environment
		$source mocui/bin/activate

	Go to the moc-gui-plugins directory
		$cd ~/MOCUI/moc-gui-plugins

	Start the Haas Plugin server locally
		$python manage.py runserver 9000
------------------------------------------------------

#Run the MOC UI
	Go to the moc-gui-plugins directory
		$cd ~/MOCUI

	Start the Moc UI's virtual environment
		$source mocui/bin/activate

	Go into the UI directory
		$cd ~/MOCUI/ui

	Go to the moc-gui-plugins directory
		./runserver.sh
	Run the UI
		open browser and point it to localhost:8000

		Register as a new user

		Go to the HaaS tab on the navigation bar
------------------------------------------------------
