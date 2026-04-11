from typing import List,TypedDict,Literal
# when raw data try to enter in application by api(json format) pydantic validate it and possible convert it into suitable formate
from pydantic import BaseModel  
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS    # vector DATABASE
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv
