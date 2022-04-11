import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\trans\Documents\GitHub\COSC310_IndividualProject\chatbot-key.json"

translate_client = translate.Client()

text = 'Good morning'
target = 'es'

def translate_to_target(text, target):
    output = translate_client.translate(text, target_language=target)
    return(output.get('translatedText'))

def translate_to_english(text):
    output = translate_client.translate(text, target_language='en')
    return(output.get('translatedText'))

"""while True:
    message = input("")
    output = translate_to_target(message, 'ko')"""

message = "안녕"
print(translate_to_english(message))

