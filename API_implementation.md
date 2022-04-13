## API Implentation

Two APIs were added for the individual project assignment:

1. Google Transalte API
2. Flickr API

### Google Translate API

Files added to implement Google Translate API:

1. translator.py - this script connects to the google cloud platform and is responsible for all the translation

The api is implemented in following parts:

1. Authentication of Google Credentials
2. Methods to convert from one language to the other
3. Adding the translated responsed to the GUI

Firstly, the translator.py script uses the translate_v2 module from google.cloud. Then I use the Service Account credentials JSON file obtained while creating a new Service Account Key to set up the Google Cloud environment variable and hence authenticate my project details.

The script uses two methods to translate the conversation -

def translate_to_target(text, target):
Takes two parameters text (Conversation text passed as a String), and target(Code of the language you need to convert to as String)

Once the parameters are set, I use the translate method of the google translate client to convert the string of conversation to the target language set by the user.

def translate_to_english(text):
Takes one parameter i.e text

![GUI Screenshot](https://user-images.githubusercontent.com/60047109/162898843-91084a98-a5e7-46d3-9f23-d86ac891fc77.png)

Once the parameters are set, I use the translate method of the google translate client to convert the string of conversation to english.

Final part of the implementation was to add the responses to the GUI so that the user can see it. This is was implemented in the chatbot.py script. User conversation is stored in the message variable which is passed as parameter to the def translate_to_eng(text): function so that the conversation can be understand by the program in english. After that, the program obtains a response using the ML model (training and predict) which is stored in the response variable. Finally, the response variable is converted to the language selected by the user, using the def translate_to_target(text, target): function.

### Flickr API

Files added to implement Flickr API:

1. flickr.py - script that parses the images from the flickr dataset into usable urls and also downloads a local copy.
2. images/cute_pets/ - this directory stores the images locally that are fetched from the api.

The api is implemented in following parts:

1. Authentication of Flickr Credentials
2. Methods to Search images according to a term and download them
3. Adding the url to the gui

The flickr API key and secret key are obtained from the flickr developer website. These keys are used for authentication.

There are two functions that are used in this script: def searchFlickrImages(term, category) and def url_to_jpg(i, url, filepath, saved_name)

![GUI Screenshot](https://user-images.githubusercontent.com/60047109/162898790-6d0d29e4-b6ae-44e8-9d16-b7f066cf48ab.png)

The searchFlickrImages function uses the passed term and category to look for specific images from its dataset. This is possible using the flickr.photos_search function provided by the api to parse image details in a JSON format. After capturing the details, these details are used to make a url of the image. Finally all the urls are collected in a list and returned. The other function uses urllib.request to download images locally using the urls obtained from the previous function.

![GUI Screenshot](https://user-images.githubusercontent.com/60047109/162898717-3e0736c6-2b1d-456f-9f89-06cd52cfad6a.png)

The implemtation of these images was in tandem with the sentiment analysis. Whenever the user responded in a frustrated manner or the negative vibes probability is over 0.65 the user is shown given the url of the image to improve their mood.
