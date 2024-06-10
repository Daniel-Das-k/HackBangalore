from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_tools_agent, AgentExecutor

sme_keywords = ["SME", "Small and Medium Enterprises","MSME","Micro, Small, and Medium Enterprises", "small and medium enterprises", "business loans", "financing", "loan applications","working capital","assessment","collateral","interest rates","terms" "conditions","loan","credit","loan guarantees","eligibility","Loan Disbursement Process","Loan Application Status","SME Banking Services","Banking Services"]

def contains_sme_keywords(query):
    return any(keyword in query.lower() for keyword in sme_keywords)

loader = WebBaseLoader(["https://msme.gov.in/", "https://udyamregistration.gov.in/", "https://en.wikipedia.org/wiki/Ministry_of_Micro_Small_and_Medium_Enterprises"])
docs = loader.load()
documents = RecursiveCharacterTextSplitter(chunk_size=0, chunk_overlap=0).split_documents(docs)

vectordb = FAISS.from_documents(documents, OpenAIEmbeddings(api_key="sk-proj-FfPGagp6wyt1vjEmk7IQT3BlbkFJI5a5XNrku0JtG4DlqIFm"))
retriever = vectordb.as_retriever()

retriever_tool = create_retriever_tool(retriever, "sme_search", "Search for information relevant to small and medium enterprises (SMEs). If you have any questions about SMEs, you can use this tool.")

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.2, api_key="your-api-key")
prompt = hub.pull("hwchase17/openai-functions-agent")
agent = create_openai_tools_agent(llm, [retriever_tool], prompt)
agent_executor = AgentExecutor(agent=agent, tools=[retriever_tool], verbose=False)

query = input("Enter The Query: ")

if contains_sme_keywords(query):
    response = agent_executor.invoke({"input": query})["output"]
    print(response)
else:
    print("This query is not related to small and medium enterprises.")
