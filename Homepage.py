import streamlit as st

from utils import utils

st.set_page_config(
    page_title="Home - davins90",
    page_icon="🏠",
)

utils.add_logo("app/images/foto_dani_cartoon.png","Daniele D'Avino",'Machine Learning Engineer @ Sky',200,"black",False)

utils.sidebar_creation()

st.title("About Me")

st.markdown("""
Ciao, I'm Daniele! 

I’m a Machine Learning Engineer with a deep passion for transforming data into actionable insights and cloud-based AI solutions.

How would I describe my professional evolution? Think of it as a perpetual Bayesian update of my skills. From delving into the depths of complex datasets to navigating the intricacies of cloud computing, I've embarked on a thrilling journey in the world of machine learning and AI.

My path has been a blend of qualitative and quantitative explorations. I’ve journeyed through the realms of statistical modeling, traversed the landscapes of machine learning algorithms, and now find myself at the forefront of cloud technology, especially within the Google Cloud Platform.

I’m not just about crunching numbers or coding algorithms. It’s about translating complex concepts into tangible solutions, mastering classification, regression, clustering, and beyond. Every step is an exciting adventure in decoding the language of data.

Equipped with Python, SQL, GIT, Docker, and more, I navigate these challenges with the curiosity of a quantitative analyst and the expertise of a seasoned data scientist.

And as Bayes would have it, my journey is far from over. It’s an ongoing quest to innovate, solve problems, and build bridges between technology and business strategy. Here's to continuing this incredible journey with creativity, collaboration, and a touch of Bayesian flair!
""", unsafe_allow_html=False)


