from openai import OpenAI
#from main import *
client = OpenAI()

def parse_text(text):
    #text = "get the screw driver"
    #text = "Screw Gear Shaft into Hole using Wrench "
    #Please extract the following information from the given text and return it as a python dictionary:
    #print(user_msg)
    # A simple prompt to extract action and object from an instruction.
    prompt1 = f'''
    extract actions and the associated objects and output in a python dictionary format 
    example:
    text = "Place the cylinder sub-assembly onto assembly plate 1, aligning the housing holes 
    to the assembly plate holes"
    action:place
    objects:[cylinder sub assembly, assembly plate1]
    action:align
    objects:[housing holes,assembly plate holes]

    This is the body of text to extract the information from:
    {text}
    '''
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a assistant to identify actions and objects from a given instructions."},
        {"role": "user", "content": prompt1}

    ]
    )
    out_dict = completion.choices[0].message.content
    return out_dict
    


#print(out_dict)
