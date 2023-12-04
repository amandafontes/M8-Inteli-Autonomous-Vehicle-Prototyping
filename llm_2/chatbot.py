import gradio as gr
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Carregar o arquivo de texto para o treinamento do modelo
loader = TextLoader("instructions.txt")
documents = loader.load()

# Dividir o texto em pedaços menores (chunks)
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0
)

docs = text_splitter.split_documents(documents)

# Criar a função de embedding do conteúdo
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Carregar o vetor no Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

# Criar o template para a pergunta
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# Instanciar o modelo do Ollama
model = Ollama(model="mistral")

# Criar a cadeia de execução
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

# Executar o modelo para o input informado
def execute_model(question):
    output = ""
    for s in chain.stream(question):
        output += s
    return output

interface = gr.Interface(
    fn=execute_model,
    inputs=gr.Textbox(placeholder="Digite aqui a sua dúvida sobre segurança do trabalho em ambientes industriais.", label="Question"),
    outputs=gr.Textbox(label="Answer"),
    title="Chatbot especialista em segurança do trabalho"
)

# Executar a interface de interação com o chatbot
if __name__ == "__main__":
    interface.launch(share=True)