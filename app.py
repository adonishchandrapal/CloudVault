from upload_manager import upload_page
from file_manager import file_manager_page
from folder_manager import folder_manager_page
import streamlit as st
from pathlib import Path
from dashboard import get_dashboard_data

st.set_page_config(
    page_title="CloudVault",
    page_icon="☁️",
    layout="wide"
)

upload_dir = Path("uploads")
upload_dir.mkdir(exist_ok=True)

st.sidebar.title("☁️ CloudVault")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload Center",
        "File Manager",
        "Folder Manager"
    ]
)

if page == "Dashboard":

    st.title("📊 Dashboard")

    data = get_dashboard_data(
        upload_dir
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Files",
        data["files"]
    )

    col2.metric(
        "Total Folders",
        data["folders"]
    )

    col3.metric(
        "Storage Used (MB)",
        data["size_mb"]
    )

elif page == "Upload Center":

    upload_page(
        upload_dir
    )

elif page == "File Manager":

    file_manager_page(
        upload_dir
    )

elif page == "Folder Manager":

    folder_manager_page(
        upload_dir
    )