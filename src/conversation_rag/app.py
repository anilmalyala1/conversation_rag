import streamlit as st
import requests

st.title("🧠 Java Code Assistant")

backend_url = "http://localhost:8000"

repos = requests.get(f"{backend_url}/repos").json()["repos"]
repo = st.selectbox("Select repo", repos)

if st.button("Re-index repo"):
    r = requests.post(f"{backend_url}/index", json={"repo_name": repo})
    st.success(r.json()["status"])

query = st.text_input("Ask a question about the codebase")
if query:
    r = requests.post(f"{backend_url}/query", json={"repo_name": repo, "question": query})
    st.code(r.json()["answer"])

filepath = st.text_input("Java file to edit")
instruction = st.text_area("Instruction")
if st.button("Apply Edit"):
    r = requests.post(f"{backend_url}/edit", json={"filepath": filepath, "instruction": instruction})
    st.success(r.json()["result"])
