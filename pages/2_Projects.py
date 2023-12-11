import streamlit as st

from utils import utils

st.set_page_config(
    page_title="Projects - davins90",
    page_icon="🥽",
)

utils.add_logo_and_name("images/foto_dani_cartoon.png","Daniele D'Avino",'Machine Learning Engineer @ Sky')

utils.sidebar_creation()

st.title("Projects")

st.image("https://media.giphy.com/media/ADD4w6XgqLBJohQdBK/giphy.gif")

st.markdown("""

Below is a list of the main projects i took part in.
- 2023: ...
- 2022: ...
- 2021: Developing a transactional data software solution, based on quantiative analysis, clustering and network analysis tecnique. *Software*: Python
- 2020: Developed a customer clustering and classification software, useful for data enrichment, artificial markets solutions and for addressing better solutions to final retail customers. *Software*: Python
- 2019: Developed a customer data analysis tool, integrated with machine learning algorithms, for wealth management institutions. *Software*: Python
- 2018: Developed digital reporting tools and risk based investment solutions. *Software*: Python, Matlab, Tableau
- 2017: Developed the framework of a profiling questionnaire. *Software*: Python, Matlab
- 2016: Developed a Web App for evaluating bond emission (yield and price) of the Italian landscape’ small cap (e.g. minibond). *Software*: Python, VBA

In my [Github](https://github.com/davins90) profile you'll find some of my hobby projects:
- **[Decision Intelligence Application](https://github.com/davins90/unsupervised_anomaly_detection)**: application for delivering fraud detection and clustering customers. Frontend in Streamlit, Backend with Fast API, deployed on GCP.
- **Meteo Adverse Classifier**: classification algorithm for predicting climate averse future conditions.
- **Network Analysis Pipeline**: Analysis of submarine telecommunication network via graph theory.
- **Stock Market Data**: tool for downloading stock market performance of the main worldwide indices.
- **Accumulation Plan**: tool for simulating a financial accumulation plan over the years, with performance and some other stats.
- **Churn Prediction**: classification algorithm for predicting churn risk for customers of an insurance company (this solution was built for a public challenge that reach 7th place on around 400 participants).
- **Auto Traffic Prediction**: regression algorithm for predicting hourly traffic on an interstate in the US.

""", unsafe_allow_html=True)