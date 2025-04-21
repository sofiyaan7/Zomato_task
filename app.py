import streamlit as st
import pandas as pd
import openai
st.set_page_config(page_title="Restaurant Hunter 🤖🍛", page_icon="🍴")
# Groq API setup
openai.api_key = "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"
openai.api_base = "https://api.groq.com/openai/v1"

# Load data
df = pd.read_csv("restaurants.csv")

# Build context from CSV
@st.cache_data
def create_context():
    context = ""
    for idx, row in df.iterrows():
        context += f"""
Restaurant Name: {row['Restaurant Name']}
Location: {row['Location']}
Cuisine: {row['Cuisine']}
Price: {row['Price']}
Ratings (Dining, Delivery): {row['Ratings(Dining, Delivery)']}
Operating Hours: {row['Operating Hours']}
Contact: {row['Contact']}
More Info: {row['More Info']}

"""
    return context

context = create_context()

# Function to query the model
def ask_bot(question):
    messages = [
        {"role": "system", "content": "You are a helpful assistant answering queries about restaurants in New Delhi. Use only the data provided. If asked about menu list some random items but do not say that they are random also add a resonable price tag only add items which looks relevant to the restraunt name."},
        {"role": "user", "content": f"Here is some restaurant data:\n\n{context}\n\nNow answer this question: {question}"}
    ]
    response = openai.ChatCompletion.create(
        model="llama3-8b-8192",
        messages=messages
    )
    return response['choices'][0]['message']['content']

# Page title


st.title("🍴 Restaurant Hunter: Your Food Craving Companion")

st.markdown("""
Welcome to the **Restaurant Hunter** chatbot!  
I’m your foodie assistant 🤖 here to satisfy your cravings and help you explore restaurants. 
Just ask me stuff like _“Top 3 romantic restaurants”_ or _“Where can I get good North Indian food?”_
""")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_prompt = st.chat_input("Type your food question here...")

if user_prompt:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_bot(user_prompt)
            st.markdown(response)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
