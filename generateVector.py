import os

def generateVector(fileOrUrl):
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.embeddings import OllamaEmbeddings
    from langchain_community.vectorstores import FAISS

    data = None

    if isinstance(fileOrUrl, str):
        from langchain_community.document_loaders import WebBaseLoader
        loader = WebBaseLoader(fileOrUrl)
        data = loader.load()
    else:
        from langchain_community.document_loaders import TextLoader
        
        with open('temp_' + fileOrUrl.name, mode='wb') as w:
            w.write(fileOrUrl.getvalue())
        loader = TextLoader('temp_' + fileOrUrl.name)
        data = loader.load()

        os.remove('temp_' + fileOrUrl.name)

    splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", "."], chunk_size=1000, chunk_overlap=200)
    doc = splitter.split_documents(data)
    try:
        embeddings = OllamaEmbeddings(model="mistral")
        vector = FAISS.afrom_documents(doc, embeddings)
        return vector
    except ValueError as e:
        print(f"Error generating embeddings: {e}")
        return None


