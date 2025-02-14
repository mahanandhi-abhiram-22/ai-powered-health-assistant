import streamlit as st
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model
chatbot = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

# Preprocess user input
def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))  # Fixed typo in 'stopwords'
    words = word_tokenize(user_input)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)  # Fixed string joining to add spaces between words

def healthcare_chatbot(user_input):
    user_input = preprocess_input(user_input).lower()  # Corrected usage of preprocess_input
    if "sneeze" in user_input or "sneezing" in user_input:
        return "Frequent sneezing may indicate allergies or a cold. Consult a doctor if symptoms persist."
    elif "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule a doctor's appointment?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        # Provide a general healthcare context for unsupported queries
        context = """Common healthcare-related scenarios include management of colds, flu, and allergies, 
        along with medication guidance and appointment scheduling.
        """
        response = chatbot(question=user_input, context=context)
        return response['answer']

# Streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("Enter your query:")

    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Assistant:", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
