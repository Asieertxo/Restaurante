


def Chatbot(message):
    print(message)
    import os
    import openai


    openai.api_key = "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"

    conversation = "Human: Hello\nAI: Hello, how can I help you today?"

    i = 1
    while (i != 0):
        conversation += "\nHuman:" + message + "\nAI:"
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = conversation,
            temperature = 0.7,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0,
        )
        answer = response.choices[0].text.strip()
        print(answer)
        conversation += answer
        return "AI: " + answer