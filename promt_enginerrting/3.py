topics = ['artificial intelligence', 'space exploration', 'ancient history']
tones = ['serious', 'humorous', 'adventurous', 'funny', 'sad']

def generate_prompts_from_data(data_list):
    prompts = []
    for item in data_list:
        prompt = f"Explain {item} in simple terms."
        prompts.append(prompt)
    return prompts

# Create a list to store prompts
prompts = []

# Generate prompts by combining topics and tones
for topic in topics:
    for tone in tones:
        prompt = f"Write a {tone} story about {topic}."
        prompts.append(prompt)

# Print all generated prompts
for prompt in prompts:
    print(prompt)

# Example usage of generate_prompts_from_data
data_list = ['quantum computing', 'machine learning', 'climate change']
data_prompts = generate_prompts_from_data(data_list)

# Print prompts generated from the data list
for data_prompt in data_prompts:
    print(data_prompt)
