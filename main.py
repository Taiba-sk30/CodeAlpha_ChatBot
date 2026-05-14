from groq import Groq

client = Groq(api_key="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")

print("🤖 Groq AI Bot Started")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        break

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print("Bot:", chat_completion.choices[0].message.content)