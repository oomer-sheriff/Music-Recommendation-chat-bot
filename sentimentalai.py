import requests as rq
import json
import openai
def ai(l):
    var=""
    for i in l:
        var=var+i+"\n"
    sentiment=openai.Completion.create(
        model="text-davinci-003",
        prompt=var+": read the conversation between the person and chat bot and only output a genre of music in a single word according to the person :" ,
        temperature=0.0,
        max_tokens=2000
    )
    return sentiment["choices"][0]["text"]