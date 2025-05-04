import nltk
import google.generativeai as genai

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Set your OpenAI API token here
genai.api_key = "AIzaSyCm3qaVkadN1jYvU13oEOOKMe"  # Replace with your actual token

# Function to analyze user input
def analyze_content(user_input):
    sentences = nltk.sent_tokenize(user_input)
    words = nltk.word_tokenize(user_input)
    pos_tags = nltk.pos_tag(words)
    key_terms = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
    return sentences, key_terms

# Function to enhance content using OpenAI
def enhance_content(key_terms, user_input, mode):
    prompt = f"Enhance the following content for {mode} using these key terms: {', '.join(key_terms)}.\nOriginal content: {user_input}"
    response = genai.Completion.create(
        engine="text-davinci-003",  # Replace with your preferred model
        prompt=prompt,
        max_tokens=150,
        temperature=0.9
    )
    return response.choices[0].text.strip()

# Function to generate debate arguments
def generate_debate_arguments(user_input):
    sentences, key_terms = analyze_content(user_input)
    for_arg = enhance_content(key_terms, user_input, "a strong argument in favor")
    against_arg = enhance_content(key_terms, user_input, "a strong argument against")
    return {"For": for_arg, "Against": against_arg}

# Function to generate blog content
def generate_blog(user_input):
    sentences, key_terms = analyze_content(user_input)
    blog_content = enhance_content(key_terms, user_input, "an engaging blog post")
    return blog_content

# Function to generate a story
def generate_story(user_input):
    sentences, key_terms = analyze_content(user_input)
    story_prompt = f"Write a creative story using these key terms: {', '.join(key_terms)}.\nStarting point: {sentences[0]}"
    response = genai.Completion.create(
        engine="text-davinci-003",
        prompt=story_prompt,
        max_tokens=300,
        temperature=1.2
    )
    return response.choices[0].text.strip()

# Main application logic
def think_and_ink_app():
    print("Welcome to Think and Ink!")
    print("Choose an option: 1) Debate Arguments, 2) Blog Writing, 3) Story Writing")
    choice = input("Enter your choice (1-3): ")
    user_input = input("Enter your content: ")

    if choice == '1':
        result = generate_debate_arguments(user_input)
        print("\nDebate Arguments:")
        print("For:", result["For"])
        print("Against:", result["Against"])
    elif choice == '2':
        result = generate_blog(user_input)
        print("\nBlog Post:")
        print(result)
    elif choice == '3':
        result = generate_story(user_input)
        print("\nStory:")
        print(result)
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

# Run the application
if __name__ == "__main__":
    think_and_ink_app()