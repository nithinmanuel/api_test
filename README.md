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
    
first clone this project, create a new folder named api_nasa and paste the cloned project into the api_nasa folder .next you have to install the venv virtual enviornment where you need to run the django and django rest framework. if you copy the path to api_nasa folder and python3 -m venv /path/api_nasa      , your path is like home/some_name/api_nasa in linux   activate the virtual env    source /path/api_nasa/bin/activate  (api_nasa) ni@N-computer: , you can see the activated virtual env (api_nasa) in your terminal run the   pip install -r requirements.txt , to install all dajgno and django restframework do ls you can see the folders cd sample_project now run python manage.py runserver paste the below url in your browser. http://127.0.0.1:8000/neos/ 
















