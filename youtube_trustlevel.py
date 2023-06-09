import openai

import re

f = open("enter_transcript.txt", 'r')
f_content = f.read()

openai.api_key = "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"

print("\n------------------------------------------")
print("Welcome to YouTube Trust Level Calculator")
print("------------------------------------------\n")

transcript =f_content
func = f"{transcript}----Based on the information provided. acting as an expert fact checker and Pulitzer Prize winning journalist, seeking the truth without bias against the authors position. Find parts of the information that seems biased, put it in bracket"
print(transcript)
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=[{"role": "user", "content": func}])


print("\n\n------------------------\n\n")


result = completion.choices[0].message.content
bracketed_results = re.findall(r'\[(.*?)\]', result)


full_misleading  = "".join(bracketed_results)



if " no " in completion.choices[0].message.content or len(bracketed_results) == 0:
    print(f'TRUST LEVEL: 100%')
    print("\n***************************\n")
    print(completion.choices[0].message.content)
    print("\n***************************\n")
else:
    percentage = (len(transcript) - len(full_misleading))/len(transcript) * 100
    print(f'TRUST LEVEL: {int(percentage)}%')
    print("\n***************************\n")
    print("Misleading Part:")
    for i in bracketed_results:
        print("-", i)
    print("\n***************************\n")


