# NEOapp 
# what is it about
nasa provides restfull api  https://api.nasa.gov/ first generate a key , later go for browse api's in the same page you will find Asteroids - NeoWs you can find all
information to call  https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-05-18&end_date=2021-05-18&api_key=
in key section put your key. and you can chnage the start date and end date in the above url ,hit the above url in a browser copy all the json data , the aim is to find out some specify data from this Hypermedia as the Engine of Application State(HATEOAS) to some specific data those are  neo_reference_id", name, nasa_jpl_url, is_potentially_hazardous_asteroid . The app will be able to parse the json data and return the above specific data . 
# Prerequsties 
get the api key from the nasa website 
# Purpose of app
To learn about to consume a public api with Hypermedia as the Engine of Application State(HATEOAS) data and try to create multiple objects or resources with a
single post request , dockerize the app if it's go with sqlite3 you would be okay with single docker file because it's embeded   but if you choose mysql or postgres you needs to write another docker file eventually needs to create network to bridge the apps.  
# App componets
please refer requiremnets.txt , docker and docker compose installed locally for runtime

# How to start it 
    
first clone this project, create a new folder named api_nasa and paste the cloned project into the api_nasa folder .next you have to install the venv virtual enviornment where you need to run the django and django rest framework. if you copy the path to api_nasa folder and python3 -m venv /path/api_nasa      , your path is like home/some_name/api_nasa in linux   activate the virtual env    source /path/api_nasa/bin/activate  (api_nasa) ni@N-computer: , you can see the activated virtual env (api_nasa) in your terminal run the   pip install -r requirements.txt , to install all dajgno and django restframework do ls you can see the folders cd sample_project now run python manage.py runserver paste the below url in your browser. http://127.0.0.1:8000/neos/  . Then run the migrations like python manage.py makemigrations and python manage.py migrate this is the normal way to do using virtualenv.

next you can use docker build -t app_name -f Dockerfile  to create a docker image . you may ask why can't make a dockerimage without doing the above steps, yesyou can do that then you need a specify volume to execute the docker commands , that is not desirable if you want to port the image to someother platform , the integrated embeded database is the reason for it , you need to migrate to the database in the old fashion (above mentioned)to do so you need to install dependencies (mentioned above) but once you have the database then you can make the image with it and when you run it you do not need a volume becasue you are storing the data inside the database but one problem is ahead once you plan to do more migrations you need to execute inside a container .

The best practice to use postgres or mysql and make it as two docker files . 

















