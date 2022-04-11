from predict import *
from tkinter import *
from translator import *
from nltk import stem

counter = 0
target_lang = ''
cat_vids = "https://www.youtube.com/results?search_query=cat+videos"
dank_memes = "https://www.reddit.com/r/dankmemes/"
res = ""
stemmer = stem.PorterStemmer()
root = Tk()

def send():
    message = e.get()
    global target_lang
    global counter
    if(counter == 0):
            if message == '1':
                txt.insert(END,"\n\nSelected English")
                counter = counter +1
                target_lang = 'en'
            elif message == '2':
                txt.insert(END,"\n\nSelected French")
                counter = counter +1
                target_lang = 'fr'
            elif message == '3':
                txt.insert(END,"\n\nSelected Chinese")
                counter = counter +1
                target_lang = 'zh-CN'
            else:
                print('stuck')
                txt.insert(END,"\n\nInvalid user input, try entering 1,2 or 3")

    else:
        usermood = get_mood(message)
        empathy_response = ""
        negative_vibes = usermood.get('neg')
        positive_vibes = usermood.get('pos')

        gui_output = "> You: {0}".format(
            "*makes eye contact" if not message else message)
        txt.insert(END, "\n" + gui_output)

        # if bot not sure what it means, get new prediction this time using stemmed input
        # message is to stemmed and then converted back to string
        message = translate_to_english(message)
        ints = predict_classes(message) 
        if float(ints[0].get('probability')) < 0.75 and ~(not message): 
            print("stemming")
            ints = predict_classes("".join(map(str, (stemmer.stem(x) for x in clean_up_sentence(message)))))

        response_predict = get_response(ints, intents)

        if (negative_vibes >= 0.55):
            empathy_response = random.choice(["I am really sorry to hear that.", "We're sorry about that...",
                                            ":(( That's so unfortunate.", "I understand your sentiment. Please allow me to help you, what do you need to know?"])
            res = empathy_response
            if (negative_vibes >= 0.65):
                response_predict += random.choice( ##replacement of predicted response
                    [f"Here are some cat videos: {cat_vids}", f"Here are some dank memes: {dank_memes}"])
        elif (positive_vibes >= 0.7):
            empathy_response = random.choice([":)", "Happy spring!!!", "I'm glad that you're satistifed with my service.",
                                            "Fantastic!!!", "Awesome!", "I LOVE to hear that!", "You fill my heart with joy :))"])+"\n"

        response_predict = translate_to_target(response_predict,target_lang)
        empathy_response = translate_to_target(empathy_response,target_lang)
        final_response = "> Bot: {0} ".format(empathy_response) + response_predict
        txt.insert(END, "\n" + final_response)
    
    e.delete(0, END)


txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=50)
send = Button(root, text="Speak", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("Customer Service Chatbot")
txt.insert(END, "Click 'Speak' to interact with the customer service bot")
txt.insert(END, '\n\n Select your language of choice: \n Type 1 for English, \n 2 for French and \n 3 for Chinese')

root.mainloop()
