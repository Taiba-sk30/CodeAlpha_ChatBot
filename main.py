from groq import Groq

client = Groq(api_key="Your_Api_Key")

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
