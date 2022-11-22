


def Chatbot(message):
    import openai


    openai.api_key = "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"

    conversation = "Human: Hello\nAI: Hello, how can I help you today?"

    i = 1
    while (i != 0):
        conversation += "\nHuman:" + message + "\nAI:"
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = conversation,
            temperature = 0.7,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0,
            stop = ["\n", " Human:", " AI:"]
        )
        answer = response.choices[0].text.strip()
        conversation += answer
        return "AI: " + answer