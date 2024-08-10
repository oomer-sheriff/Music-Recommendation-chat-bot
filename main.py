
from spotify1 import spotify
from conversationai import ai2
from sentimentalai import ai
from storyai import ai2 as sai
import requests as rq
import json
import openai
openai.api_key ="api-key"
lis=[]
for i in range(20):
    sai(i,lis)
    decision=input("do you wanna continue? y or n  :  ")
    if decision=='n':
        typ=ai(lis)
        spotify(typ)
        break