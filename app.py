import streamlit as st
import os
import pickle
from generateAnswer import generateAnswer
from generateVector import generateVector

if __name__=="__main__": 
    st.title('Train with your data.')    

    if 'file_path' not in st.session_state:
        st.session_state.file_path="vector.pkl"
    if 'vector' not in st.session_state:
        if os.path.exists(st.session_state.file_path):
            with open(st.session_state.file_path, "rb") as f:
                st.session_state.vector = pickle.load(f)
        else:
            st.session_state.vector = None
    if 'method' not in st.session_state:
        st.session_state.method = None

    if st.session_state.vector:
        st.subheader("Vector generated.")            
        clicked = st.button('Remove vector index', type="primary")
        if clicked:
            os.remove(st.session_state.file_path)
            st.session_state.vector = None
            st.rerun()
        question = st.text_input('Ask anything...')
        if (question):
            st.write(generateAnswer(question=question, retriever=st.session_state.vector.as_retriever()))
    else:
        st.session_state.method = st.selectbox(options = ["Upload document", "Webpage link"], label="Training method:")

        if st.session_state.method == "Upload document":
            file = st.file_uploader(label="Select a file", accept_multiple_files=False, type=['txt'])
            if file:
                clicked = st.button('Generate vector', type="primary")
                if clicked:
                    st.session_state.vector = generateVector(file)
                    # create a file
                    with open(st.session_state.file_path, "wb") as f:
                        pickle.dump(st.session_state.vector, f)
                    st.rerun()
        elif st.session_state.method == "Webpage link":
            url = st.text_input('Enter webpage url')
            if url:
                clicked = st.button('Generate vector', type="primary")
                if clicked: 
                    st.session_state.vector = generateVector(url)
                    # create a file
                    with open(st.session_state.file_path, "wb") as f:
                        pickle.dump(st.session_state.vector, f)
                    st.rerun()
