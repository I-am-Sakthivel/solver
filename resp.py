import os
import requests
import json

from agent import fn 

url=os.getenv("url","https://aiproxy.sanand.workers.dev/openai/v1/chat/completions")
token=os.getenv("token")

headers={
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}

def send_req(q):
    response=requests.post(url=url,headers=headers,json={
    "model":"gpt-4o-mini",
    "messages":[
        {
            "role":"system","content":"You help in solving limerics involving simple maths"
        },
        {
        "role":"user","content":q,
    }],
    "tools":fn,
    "tool_choice":"auto"})
    message=response.json()['choices'][0]['message']['content']
    if message:
        return (None,None,message)
    name_of_function=response.json()['choices'][0]['message']['tool_calls'][0]['function']['name']
    args=json.loads(response.json()['choices'][0]['message']['tool_calls'][0]['function']['arguments'])
    return (name_of_function,args,message)