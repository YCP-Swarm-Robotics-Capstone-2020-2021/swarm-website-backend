## Obtain .env file
File goes into the ```swarmdjango``` directory.
For local development all you need are the following variables to be set:
- DB_PASSWORD
- SECRET_KEY
- DEBUG=True  

Contact repo owners or contributors for these variable values.

## Build backend Docker containers
sh dockerUpBackend.sh

## coverage lib commands
##### -all commands run in django container-  
run after any code addition: ```coverage run --source='.' manage.py test```  
then run ```coverage report``` or ```coverage html``` to get report 
- The former will simply show report in the terminal
- The latter will make a 'htmlcov' dir (gitignored) with an 'index.html' you can view and look at the report in the browser
