# Welcome to the HackNC REST API workshop!

# Below, you'll find a template outline the basics of REST API!





# First, we need to import the requests library from Python, which allows us to use REST APIs and access their data

import requests
from pandas.io.json import json_normalize


# Next, we need a URL. Specifically, we need a URL from our specific API, so that we're able to access the data they're providing.


# A basic URL can look like : https://api.example.com/<parameter>/<endpoints>
# <parameter> and <endpoints> are mutable aspects of the URL that allow us to access different types of data. I'll 
# I'll demonstrate this later. 


# Let's "consume" our Data-Muse API

# First, we'll use the requests library's wonderful GET method, which allows us to retreive data from an API

    # Let's define our URL- 

our_url = "" # Copy our url from the github markdown into the apostrophes

# Next, we need specific parameters for our URL. After seeing how the Data-Muse API works, let's ask the API for words that rhyme with "rest"


# Let's use the requests library's framework to simply ask it to "GET" the words in our parameter

# One note,  we cannot just use our URL the way we have defined it. It is important to read the documentation of our API to understand how links will work
# In our case, the documentation requires us to add "words" at the end of the URL.


# Querying input
    # Three options: mean like, sound like, spelled like, rhyme with
# option = input("Choose options: \n 'ml': mean like, \n 'sl': sound like, \n 'sp': spelled like, \n 'rl': rhyme with \n Choice: ")
# word = input("Enter word: ")


newURL = f"http://api.datamuse.com/words?{option}={word}" # <- add words based off the documentation to the end of our URL here

# Now, finally, let's call our API

response = requests.get(newURL)


# Finally, the last step in consuming our API is printing our responses in JSON format, a key-value store that is related to the the Python dictionary

print(response.status_code)
print(response.json())

print(json_normalize(response.json()))


# We can see, that we get a whole bunch of words that rhyme with Hackathon!
