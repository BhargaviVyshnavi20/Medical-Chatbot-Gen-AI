from flask import Flask, render_template, request, jsonify
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from groq import Groq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)
load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


embedding = download_embeddings()


index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    embedding=embedding,
    index_name=index_name,
)


retriver = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def retrieve_context(query):
    # This uses your existing docsearch to find relevant text
    docs = docsearch.similarity_search(query, k=3)
    return "\n\n".join(doc.page_content for doc in docs)



def ask_groq(question, context):
    # context = context[:6000]
    prompt = f"""
You are a Community Health Assistant for rural areas. Use very simple, supportive language.
Provide health facts based ONLY on the context below. Follow these rules strictly:

1. LANGUAGE & TONE
- Use the 10-Year-Old Rule: Use "belly," "breathing," and "signs." No medical jargon.
- Action-Oriented: Use "Drink," "Rest," "Wash."
- No Extra Details: Keep instructions to one short sentence.
- Strict Neutrality: NO EMOJIS. No phrases like "I am sorry" or "Don't worry."

2. GREETING & SCOPE
- If the user says "Hi" or "Hello" without a question: Say "Hello!" and nothing else. Stop.
- If the user asks a question: Start with facts immediately. No "I can help with that" filler.
- If the information is not in the context: Say only "I do not have much information about this problem. Please ask a health worker." Do not include the footer.

3. MANDATORY MARKDOWN FORMATTING
- Use a Markdown bulleted list (using *) for all facts.
- Every single bullet point MUST be on its own new line.
- Use a Bold Heading for the footer: **⚠️ WHEN TO SEE A DOCTOR**

4. MANDATORY FOOTER (Only if context was found)
- List warning signs in a Markdown list.
- Disclaimer: 'This is for information only. Please speak with a healthcare provider for medical diagnosis.'

Context:
{context}

Question:
{question}
"""


    response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct", # Updated Model ID
    messages=[{"role": "user", "content": prompt}],
    temperature=0
    )   

    return response.choices[0].message.content




def rag_answer(question):
    context = retrieve_context(question)
    return ask_groq(question, context)




@app.route('/')
def index():
    return render_template('chat.html')



@app.route("/get", methods=["POST"])
def chat():
    # Use .get() to avoid errors if "msg" is missing
    msg = request.form.get("msg")
    if not msg:
        return "No message received."
    # This calls your RAG logic and returns the response
    response = rag_answer(msg)
    return str(response)



if __name__ == '__main__':
    app.run(debug=True)