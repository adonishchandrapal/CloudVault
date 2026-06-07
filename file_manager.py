
import streamlit as st
from datetime import datetime

def file_manager_page(upload_dir):

    st.write("VERSION 2")

    st.title("📂 File Manager")

    search = st.text_input("🔍 Search Files")

    files = [
        f for f in upload_dir.rglob("*")
        if f.is_file()
    ]

    if search:
        files = [
            file for file in files
            if search.lower() in file.name.lower()
        ]

    if not files:
        st.info("No files found.")
        return

    for file in files:

        size_kb = round(
            file.stat().st_size / 1024,
            2
        )

        modified_date = datetime.fromtimestamp(
            file.stat().st_mtime
        )

        st.markdown("---")

        st.write(
            f"📄 {file.name}"
        )

        st.caption(
            f"Folder: {file.parent.name}"
        )

        st.caption(
            f"Size: {size_kb} KB | Modified: {modified_date.strftime('%d-%m-%Y %H:%M')}"
        )

        col1, col2, col3 = st.columns(3)

        # Download
        with col1:

            with open(file, "rb") as f:

                st.download_button(
                    "⬇ Download",
                    data=f,
                    file_name=file.name,
                    key=f"download_{file.name}"
                )

        # Open & Edit
        with col2:

            if st.button(
                "📖 Open",
                key=f"open_{file.name}"
            ):

                st.session_state[
                    f"opened_{file.name}"
                ] = True

        # Delete
        with col3:

            if st.button(
                "🗑 Delete",
                key=f"delete_{file.name}"
            ):

                file.unlink()

                st.rerun()

        # Editor
        if st.session_state.get(
            f"opened_{file.name}",
            False
        ):

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                edited_content = st.text_area(
                    f"Editing {file.name}",
                    value=content,
                    height=250,
                    key=f"editor_{file.name}"
                )

                if st.button(
                    "💾 Save Changes",
                    key=f"save_{file.name}"
                ):

                    with open(
                        file,
                        "w",
                        encoding="utf-8"
                    ) as f:

                        f.write(
                            edited_content
                        )

                    st.success(
                        f"{file.name} saved successfully!"
                    )

                    st.rerun()

            except Exception as err:

                st.error(
                    f"Unable to open file: {err}"
                )