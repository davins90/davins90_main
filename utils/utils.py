import streamlit as st
import base64
import validators

from pathlib import Path

def sidebar_creation():
    """

    """
    st.sidebar.header("Contatcs")
    
    # Contact information with icons
    contact_info = """
    <div style='text-align: left;'>
        <p><a href='mailto:daniele.davino12@gmail.com'>
            <img src='https://img.icons8.com/ios-filled/50/000000/email.png' style='width: 30px;'/>Email
        </a></p>
        <p><a href='https://www.linkedin.com/in/daniele-d-avino/'>
            <img src='https://img.icons8.com/ios-filled/50/000000/linkedin.png' style='width: 30px;'/>LinkedIn
        </a></p>
        <p><a href='https://github.com/davins90'>
            <img src='https://img.icons8.com/ios-filled/50/000000/github.png' style='width: 30px;'/>GitHub
        </a></p>
        <p><a href='https://twitter.com/DAvinoDaniele'>
            <img src='https://img.icons8.com/ios-filled/50/000000/x.png' style='width: 30px;'/>Twitter/X
        </a></p>
    </div>
    """
    
    return st.sidebar.markdown(contact_info, unsafe_allow_html=True)


def add_logo_and_name(logo_url: str, name: str, title: str, height: int = 200):
    """Add a logo and name on the top of the navigation page of a multipage app.
    The url can either be a URL to the image or a local path to the image.

    Args:
        logo_url (str): URL/local path of the logo
        name (str): Name to be displayed above the logo
        title (str): Title to be displayed below the name
    """

    if validators.url(logo_url):
        logo = f"url({logo_url})"
    else:
        # Convert the local image to a base64 string
        logo = f"url(data:image/png;base64,{base64.b64encode(Path(logo_url).read_bytes()).decode()})"

    # Adjust padding-top for the space needed by the logo and the name
    padding_top = height + 40  # Adjust the padding as necessary

    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: none;
                padding-top: {padding_top}px;
            }}
            
            [data-testid="stSidebarNav"]::before {{
                content: "{name}\\A{title}";
                display: block;
                position: absolute;
                top: 20px; /* Adjust top positioning as necessary */
                left: 0;
                right: 0;
                white-space: pre-wrap;
                text-align: center;
                color: white; /* Or any color that fits the sidebar theme */
                font-size: 18px; /* Or the size that fits the sidebar theme */
                font-weight: bold;
            }}
            
            [data-testid="stSidebarNav"]::after {{
                content: "";
                display: block;
                position: absolute;
                top: 120px; /* Position right below the name and title */
                left: 20px;
                right: 20px;
                height: {height}px;
                background-image: {logo};
                background-repeat: no-repeat;
                background-size: contain; /* contain will ensure the image fits within the element */
                background-position: center;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )






