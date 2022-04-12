# Hudson's Drip™ customer service AI Chatbot

  We created an Artificial-intelligence powered chatbot to serve the customers of our online clothing store: Hudson's Drip. We used an agile SDLC methodology, with our development cycle consisting of two scrums.
  
  Our software consists of two input JSON files used to train the neural network and make personalized answers based on customer information. The training.py imports data from intents.py and trains the neural network. training.py outputs words and classes pk1 files, which are used by the predict.py module to estimate the probability that a user input addresses a particular topic in the intents.JSON. A random response from the most likely topic is outputted by the chatbot. Our bot is also able to empathize with the user and take into account the mood of the user when generating responses.

Several libraries were used: tkntr, random, json, pickle, numpy, nltk (Porterstemmer, word net lemmatizer, Sentiment intensity analyzer), and tensorflow.

[JIRA Roadmap](https://durvan.atlassian.net/jira/software/projects/CT3/boards/).  
[Reference material](https://www.youtube.com/watch?v=1lwddP0KUEg). 
  
## COSC 310 Group members:
- Guiherme Durvan António Zandamela
- Lakshay Karnwal
- Abdulaziz Almutlaq
- Ravil Bigvava
- Jordan onwuvuche

### Individual Project tasks:

For the individual project, I utilized two public APIs: Google translate API and Flickr API. Implementing these two APIs increased the functionality of my chatbot. I have explained the use of the two APIs below.

#### Google Translate API
![GUI Screenshot](https://raw.githubusercontent.com/durvanZ/COSC310_Team3/main/screenshots/botdemo.png)

The translate API is used to add three different language options for the users. Since, Hudson's drip customer service chatbot is going to be used in Canada, I have included the option for users to choose among the top three languages spoken in Canda. The three language options are: English, French and Chinese (since mandarin is not provided by google translate).

When the chatbot starts, the user is asked to choose their language of choice. After the user makes their selection the conversation proceeds in that selected language. For the implementation details check the API_implementation file.

#### Flickr API

The Flickr API is well known for its image and caption datasets. I decided to use this api to include media in the chatbot. Using the Flickr api I was able to scrape images of cute pets from their online dataset. Then, I used these images to be displayed whenever the user was extremely frustrated during the conversation. It is always helpful to make a person smile, when they are not feeling the best :)

For the implementation details check the API_implementation file.


### Assignment 3 tasks:

#### GUI Implementation
![GUI Screenshot](https://raw.githubusercontent.com/durvanZ/COSC310_Team3/main/screenshots/botdemo.png)

The GUI was implemented using the Python tkinter module for graphical interfaces. Using this module we created a text box where the user enters their query/text. This helps the app become intuitivey easy-to-use for the user.

#### Test cases implementation

The Automated Unit Testing Framework used for this was pytest due to its easy to use module functions. We created multiple test cases for all the important functions which checks if all the functions are working as desired. You can run the Unit testing file using the pytest command. After running the test file, pytest displays a summary of failed and passed functions. If the functions do not pass that means the chatbot will have errors, if all the functions pass that means the program is working as desired.

![Unit Testing Screenshot](https://user-images.githubusercontent.com/60047109/159101549-550633ec-41f7-408e-8fa5-5a43b64d2d75.png)

In the screenshot example above, one of the functions failed because the value of probability was not correct. This is a useful feature as it reduces effort to debug the code.

#### Sentiment analysis

We used a natural language toolkit "Sentiment intensity analyzer" to obtain positivity and negativity scores from the words in the user input. This information was used to make conditional statements in which the response of the bot is either complemented or replaced (depending on the intensity) by a response designed to address the sentiment of the user.

![Sentiment analysis demo](https://raw.githubusercontent.com/durvanZ/COSC310_Team3/main/screenshots/sentimentdemo.png)

#### Word stemming in ambiguous cases

Word stemming was used in addition to unstemmed input. Our algorithm stems the user input if the bot is not able to find a probable intent (probability > 0.50).
This helps to prevent inaccurate responses and can address suffixes.

![Sentiment analysis demo](https://raw.githubusercontent.com/durvanZ/COSC310_Team3/main/screenshots/sentimentdemo.png)
