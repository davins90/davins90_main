import streamlit as st

from utils import utils

st.set_page_config(
    page_title="Utilities - davins90",
    page_icon="🛠️",
)

utils.add_logo("app/images/foto_dani_cartoon.png","Daniele D'Avino",'Machine Learning Engineer @ Sky',200,"black",False)

utils.sidebar_creation()

st.title("Utilities")

st.image('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd211eGxwYXVzaDExaTBzYjZiazAzbTFlZjUwYnU5ajVxaDBjcnMwcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Mah9dFWo1WZX0WM62Q/giphy.gif', caption='Page Under Construction...')