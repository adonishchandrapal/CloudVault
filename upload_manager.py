import streamlit as st
from pathlib import Path

def upload_page(upload_dir):

    st.title("⬆️ Upload Center")

    folders = [
        f.name
        for f in upload_dir.iterdir()
        if f.is_dir()
    ]

    selected_folder = st.selectbox(
        "Select Folder",
        folders if folders else ["uploads"]
    )

    uploaded_file = st.file_uploader(
        "Choose a file"
    )

    if uploaded_file:

        if folders:

            target_dir = (
                upload_dir /
                selected_folder
            )

        else:

            target_dir = upload_dir

        file_path = (
            target_dir /
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        st.success(
            f"{uploaded_file.name} uploaded to {selected_folder}"
        )