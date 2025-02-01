# ptomts creares using loops 
topics = ['artificial intelligence', 'space exploration', 'ancient history']
tones = ['serious', 'humorous', 'adventurous', 'funny', 'sad']

prompts = []

for topic in topics:
    for tone in tones:
        prompt = f"Write a {tone} story about {topic}."
        prompts.append(prompt)

for prompt in prompts:
    print(prompt)