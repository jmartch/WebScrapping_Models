from langchain_ollama import OllamaLLM  # Import OllamaLLM from langchain_ollama
from langchain_core.prompts import ChatPromptTemplate  # Import ChatPromptTemplate from langchain_core.prompts

# Template for the prompt that will be used to extract information
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the model with a specific version
model = OllamaLLM(model="llama3.2")


# Function for parsing chunks of DOM content with the Ollama model
def parse_with_ollama(dom_chunks, parse_description):
    # Create a ChatPromptTemplate from the predefined template
    prompt = ChatPromptTemplate.from_template(template)
    # Chain the prompt with the model
    chain = prompt | model

    # List to store parsed results
    parsed_results = []

    # Iterate over the chunks of DOM content
    for i, chunk in enumerate(dom_chunks, start=1):
        # Invoke the chain with the current chunk and description
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        # Print progress information
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        # Append the response to parsed results
        parsed_results.append(response)

    # Return the concatenated parsed results
    return "\n".join(parsed_results)
