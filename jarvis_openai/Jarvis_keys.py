import openai
from userinfo import name
API_KEY = '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'
Bot_name = 'Jarvis'
openai.api_key = API_KEY
def jarvis_operation(order):
    response=''
    # if 'code' in order:
    #     response = openai.Completion.create(
    #     model="code-davinci-002",
    #     prompt=order,
    #     temperature=0,
    #     max_tokens=256,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    #     )
    # else:
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=order,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(
        name + ":", 1)[0].split(Bot_name + ":", 1)[0]

    return response_str