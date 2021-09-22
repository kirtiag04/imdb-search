# imdb-search
Displays a list of top 250 movies and their details using IMDB API. 

**The imdb-search application is designed using Flask, Python-based web framework**

**On the home page, we display a list of top 250 movies**
* This list is generated using IMDB API
* There is also a filter text field on this page to filter movies from the results
* After you click on a movie, you are sent to another page which displays the details of a movie  

**On the movie details page, we display the details related to a movie**
* These details are generated using IMDB API
* There are also two buttons: Like and Dislike to save user opinion to the User model

Note: For now, opinions are saved for one particular user only. We can extend this application for multiple users as the table in the database has a field for username. 


## Requirements and steps to run application

Install Python3.6 

### Install pip
sudo apt-get install python-pip

### Install virtualenv
sudo pip install virtualenv

### Go into imdb-search directory 
cd imdb-search

### Create a virtual env
virtualenv imdbsearch

### Activate virtual environment
source imdbsearch/bin/activate\
source imdbsearch/scripts/activate (on Windows machine)

### Install depencies
pip install -r requirements.txt

### Create a database
python db_create.py

### Run flask application (by default it runs on port 5000)
python run.py


## API documentation

### Home page
Render home page of the application\
URL - / and /index\
Method - GET\
Success Response - 200\
Error response - 500\
Success Response Body - {'items': [{'id': 'tt0111161', 'rank': '1', 'title': 'The Shawshank Redemption',....}

### Save user opinion
Save user opinion to the database\
URL - /saveOpinion\
Method - POST\
Success Response - 200\
Error response - 500

### Movie Details 
Renders a movie details page\
URL - /movieDetails\
Method - GET\
Success Response - 200\
Error response - 500\
Success Response Body - [{'id': 'tt0111161', 'resultType': 'Title',...}]