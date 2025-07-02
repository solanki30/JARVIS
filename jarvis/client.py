from openai import OpenAI



client=OpenAI(
    api_key="API_KEY"

)
completion=client.chat.completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are virtual assistant named jarvis skilled in general tasks like alexa ang google cloud" },
        {"role":"user","content":"what is coding"}
    ]
)

print(completion.choices[0].messages.content)