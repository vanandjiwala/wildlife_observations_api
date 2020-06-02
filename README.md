# wildlife_observations_api


## Description
Simple app to record bird/wildlife sightings.  

##TODO
* Script to populate lookup table
* Import and export functionality for the lookup table
* Validation and additional fields to cover date/time and other useful information
* Implement dashboard for admin to create summary or perform other analysis on the combined data 

## Models
* Total three models user in this project. ```User, Species and Observation```.
* User hold user related info. provided by django
* Species is a lookup table which hold species name and its scientific name
* Observation holds the detail like Country, state, species id(Foreign Key), user(Foreign key) 

## Endpoints
* ```/api/species/``` - User with valid token can perform CRUD
* ```/api/observations/``` - User with valid token can perform CRUD. Observations are displayed for the logged in user only. 
* ```/api/dashboard/``` - Work in progress. Admin should only get data and on front end the data can be used in report or can be visualized.
* ```login``` - POST request to obtain authentication token

## Testing
Testing performed using 2 tools: [postman](https://www.postman.com/downloads/) and [ModHeader chrome plugin](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en)

####Note
Make sure to turn off ModHeader plugin after testing, else it can mess up other website operations as well. 


## Installing Vagrant server

There are 2 requirements to setup vagrant server
* Install [vagrant](https://www.vagrantup.com/)
* Install [Virtualbox](https://www.virtualbox.org/)

youtube reference for the same can be found [here](https://www.youtube.com/watch?v=IzGO9t6cNk8).
___

## Setting up vagrant box
* Navigate to root of the django project
* Copy the vagrant file provided in the [github repo](https://github.com/LondonAppDev/profiles-rest-api/blob/master/Vagrantfile)
* Use command ```vagrant up``` to set up the virtual box
* Once processing is done then you are all set to test your app on virtual box
* Use command ```vagrant ssh``` to ssh into the newly created virtual box
* Naviagate to vagrant directory using command ```cd /vagrant/```. This directory will always sync with the project directory. This is a 2 way sync sp file added on your system will show up in virtual machine and similarly file added to VM will be displayed in your project. 
___

## Create virtual environment on vagrant box
* Use command ```python -m venv ~/env``` to create a new virtual environment
* Use command ```source ~/env/bin/activate``` to activate the virtual environment.
* Once you are in the virtual environment, use command ```deactivate``` to get out of virtual environment.

## Installing django and drf
* Make sure to activate virtual environment before performing this step.
* From the project folder run command python ``` pip install -r requirements.txt``` to install required python libraries.
* Once libraries are installed, django app can be tested using VM. 
