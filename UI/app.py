import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import os
import zipfile
import shutil
from engine.modernizer import run_modernization

st.set_page_config(page_title="Legacy Modernizer", layout="wide")

st.title("🚀 Legacy Code Modernization Engine")

# Upload ZIP
uploaded_file = st.file_uploader("Upload Java Repository (ZIP)", type=["zip"])

start_method = st.text_input(
    "Enter Start Method ID (Example: UserService.java:login)"
)

if uploaded_file is not None:

    # Create temp folder
    if os.path.exists("temp_repo"):
        shutil.rmtree("temp_repo")

    os.makedirs("temp_repo", exist_ok=True)

    # Extract ZIP
    with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
        zip_ref.extractall("temp_repo")

    st.success("Repository uploaded successfully.")

    if st.button("Modernize Code"):

        if not start_method:
            st.warning("Please enter a start method ID.")
        else:
            with st.spinner("Processing..."):

                result = run_modernization("temp_repo", start_method)

            st.subheader("📌 Related Methods")
            st.write(result["related_methods"])

            st.subheader("📂 Files Used")
            st.write(result["files_used"])

            st.subheader("📉 Context Reduction")
            st.write(f'{result["context_reduction_percent"]}%')

            st.subheader("💻 Converted Python Code")
            st.code(result["converted_code"], language="python")