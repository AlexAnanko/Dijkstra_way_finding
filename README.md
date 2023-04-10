# Setup

1. First of all you can clone git:

	$ git clone https://github.com/AlexAnanko/Dijkstra_way_finding.git \
    $ cd shortest_way

2. Secondly create virtual environment:
	
    `$ virtualenv2 --no-site-packages env` \
	`$ source env/bin/activate`

3. Install poetry and dependencies:

	`$ pip3 install poetry` \
    `$ poetry install` 

4. Create database:
	
    `$ create db_name`
    

 
# Start working

1. Make migration of models:
	
    `$ python3 manage.py makemigrations` \
    `$ python3 manage.py migrate`

2. To load data into database:

	`$ python3 manage.py load_data`

3. Start app:
	
    `$ python3 manage.py runserver`

# Tests

To run tests:
	
    `$ python3 manage.py test`


# Start telegram bot

1. Search for `@botfather` in Telegram.

2. Write `/newbot` command

3. Come up with a name of your Telegram bot

4. Take your uniq Token

5. Then past your Token
	
    `$ config.py`
    
    Field `API_TOKEN`

6. Take your OpenWaeather token
	
    `1.` Go to https://openweathermap.org \
    `2.` Create an account \ 
    `3.` Sign in \
    `4.` Go to My API Keys Tab \
    `5.` Take your API Key \
    `6.` Past your API Key
   
   `$ config.py` \
   
   Field `OWM`

7. Start Telegram bot
	
    `$ python manage.py bot`
        
