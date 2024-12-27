from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv

load_dotenv()

# Prompt template
temp_flash = ChatPromptTemplate.from_template("can you create an essay about {topic} in 50 words?")
temp_pro = ChatPromptTemplate.from_template("can you create a poem about a {topic} in 100 words?")

# models 
flash = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
pro = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Fast API App 
app = FastAPI(title='Langchain server', 
              version='1.0', 
              description='A Simple Server for routing models')

# adding routes for both models

add_routes(
    app, 
    temp_flash|flash, 
    path='/essay'
)

add_routes(
    app, 
    temp_pro|pro, 
    path='/poem'
)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost')