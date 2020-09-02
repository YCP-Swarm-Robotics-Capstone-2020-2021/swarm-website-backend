## Obtain secret files
- secrets.json (goes into swarmdjango directory)
- env.list (goes into swarmpostgres directory)

## Build backend Docker containers
sh dockerUpBackend.sh

## coverage lib commands
#####all commands run in django container  
run after any code addition: ```coverage run --source='.' manage.py test```  
then run ```compare report``` or ```compare html``` to get report 
- The former will simply show report in the terminal
- The latter will make a 'htmlcov' dir (gitignored) with an 'index.html' you can view and look at the report in the browser
