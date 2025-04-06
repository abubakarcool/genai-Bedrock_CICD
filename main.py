import os
import boto3
import streamlit as st
from dotenv import load_dotenv

# ✅ Updated imports from the new langchain_community package
from langchain_community.llms import Bedrock
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

# Load credentials
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = os.getenv("region_name")

# ✅ Boto3 Bedrock client setup
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# ✅ Updated Bedrock model ID (Make sure it's available in your region/account)
model_id = "mistral.mistral-7b-instruct-v0:2"

llm = Bedrock(
    model_id=model_id,
    client=bedrock_client,
    model_kwargs={"temperature": 0.7}
)



# ✅ Prompt using the user input properly
prompt = PromptTemplate(
    input_variables=["user_text"],
    template="You are a helpful chatbot. Answer this question: {user_text}"
)

# ✅ Runnable chain using new LangChain pattern
chatbot_chain = prompt | llm  # This replaces LLMChain()

def my_chatbot(user_text):
    response = chatbot_chain.invoke({"user_text": user_text})
    return response

# ✅ Streamlit UI
st.title("Amazon Bedrock Chatbot (LangChain)")

user_text = st.sidebar.text_area(label="What is your question?", max_chars=300)

if user_text:
    response = my_chatbot(user_text)
    st.write(response)
