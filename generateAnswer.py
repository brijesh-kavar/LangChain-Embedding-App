from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

def generateAnswer(question, retriever):
    template = """
    Given the following context, answer the quetion in the most appropriate way or respond with 'I don't know'. Don't make up your own answer.
    Context: {context}
    Quetion: {question}
    """
    prompt = PromptTemplate(input_variables=["context", "question"],template=template)
    chain = RetrievalQA.from_chain_type(
        llm=Ollama(model="mistral"),
        chain_type="stuff",
        retriever= retriever,
        input_key="query",
        chain_type_kwargs={"prompt": prompt}
    )

    response = chain.invoke(question)
    return response['result']
