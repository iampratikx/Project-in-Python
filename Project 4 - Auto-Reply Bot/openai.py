from openai import OpenAI

command = ''' [14:48, 7/26/2024] X018: ruk
[14:48, 7/26/2024] X018: video call karle
[14:48, 7/26/2024] X018: abbey net ???
[14:48, 7/26/2024] X018: !!!!!!
[14:48, 7/26/2024] Prαtîk: net ka problem hai
[14:49, 7/26/2024] X018: haa
[14:49, 7/26/2024] X018: ruk karta hu
[14:49, 7/26/2024] Prαtîk: simple call kar
[14:49, 7/26/2024] X018: ha
[18:41, 7/27/2024] X018: https://www.youtube.com/watch?v=XXpqvGqgti4&list=LL&index=1
[13:06, 7/28/2024] X018: hum jabhi chup rahenge satya se '''
client = OpenAI(
    api_key="Your Openai API Key",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named Pratik who speak english as well as hindi. He is from India and is a coder. you analize chat history and respond like Pratik"},
        {"role": "user", "content": "command"}
    ]
)

print(completion.choices[0].message.content)
