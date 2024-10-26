import chatLlama

query = ''
content = ''

with open('input.txt') as f:
    content = f.read()

response = chatLlama.get_response(f"Summarise this text to 1/4 of its original length and just me the text without any of your justification or closure: {content}")
with open('output.txt', "w") as f:
    content = f.write(response)