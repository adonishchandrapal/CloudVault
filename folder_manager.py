import streamlit as st
from pathlib import Path

def folder_manager_page(upload_dir):

    st.title("📁 Folder Manager")

    folder_name = st.text_input(
        "Folder Name"
    )

    if st.button(
        "Create Folder"
    ):

        if folder_name:

            folder_path = (
                upload_dir /
                folder_name
            )

            folder_path.mkdir(
                exist_ok=True
            )

            st.success(
                f"{folder_name} created successfully!"
            )

    st.write("## Existing Folders")

    folders = [
        f for f in upload_dir.iterdir()
        if f.is_dir()
    ]

    if folders:

        for folder in folders:

            col1, col2 = st.columns(
                [4, 1]
            )

            with col1:

                st.write(
                    f"📁 {folder.name}"
                )

            with col2:

                if st.button(
                    "Delete",
                    key=f"delete_folder_{folder.name}"
                ):

                    try:

                        folder.rmdir()

                        st.success(
                            f"{folder.name} deleted."
                        )

                        st.rerun()

                    except:

                        st.error(
                            "Folder is not empty."
                        )

    else:

        st.info(
            "No folders found."
        )