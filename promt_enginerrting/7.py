import openai
import streamlit as st

# Set up your OpenAI API key
openai.api_key = "your-api-key-here"

# Function to retrieve information (this seems to be a placeholder)
def retriever_info(query):
    # You can replace this with actual logic to fetch relevant information
    return "about the Prime Minister of India"  # Placeholder response

# Function to register a query and interact with the OpenAI API
def reg_query(query):
    # Retrieve additional information based on the query
    retrieved_info = retriever_info(query)

    # Prepare the argument for the prompt
    argumented_prompt = f"user query: {query}\nretrieved info: {retrieved_info}"

    # Create a completion request to OpenAI's API
    response = openai.Completion.create(
        model="text-davinci-003",  # Use GPT-3 model (change to a different model if needed)
        prompt=argumented_prompt,
        max_tokens=150  # Limit the response length (adjust as needed)
    )

    # Return the generated response
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Prompt Engineer Workshop")
user_input = st.text_input("Enter your query")  # Fixed variable assignment and capitalization

if st.button("Submit"):  # Fixed button function
    response = reg_query(user_input)  # Call the correct function and fixed variable naming
    st.write("Response:", response)  # Fixed output logic
else:
    st.write("Please enter a query and click on Submit.")
