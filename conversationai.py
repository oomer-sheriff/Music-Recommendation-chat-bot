import requests as rq
import json
import openai
openai.api_key ="api-key"
def ai2(i,lis):
    var=""
    for i in lis:
        var=var+i+"\n"
    if i==0:
        conversation=input("talk about how you are feeling today : \n you :  ")
        var=" chatbot : talk about how you are feeling today"+"person : " +var+conversation
    else :
        conversation=input("you : ")
        var=var+conversation
    sentiment=openai.Completion.create(
        model="text-davinci-003",
        prompt='''continue the following conversation and ask some questions and help the person to make decisions,output only one sentence and dont output multiple lines:  '''+var ,
        temperature=1.5,
        max_tokens=3000
        )
    var=var+sentiment["choices"][0]["text"]
    print(" chatbot : ", sentiment["choices"][0]["text"])
    lis.append("person : " +conversation)
    lis.append("chat bot: "+ sentiment["choices"][0]["text"])