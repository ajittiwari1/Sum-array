import os
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

system_prompt = "You are a helpful assistant."
model_name = 'llama3-8b-8192'

groq_chat = ChatGroq(
    groq_api_key=groq_api_key,
    model_name=model_name
)

def get_response(user_input):
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )

    conversation = LLMChain(
        llm=groq_chat,
        prompt=prompt,
        verbose=False,
    )

    response = conversation.predict(human_input=user_input)
    return response