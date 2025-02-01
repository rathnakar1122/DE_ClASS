def create_prompt():
    topic = input("What is the topic for the story? ")
    tone = input("Enter the tone (serious, humorous, adventurous, funny, sad): ")

    prompt = f"Write a {tone} story about {topic}."
    return prompt

user_prompt = create_prompt()
print("Generated prompt:", user_prompt)
