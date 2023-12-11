import streamlit as st

from utils import utils

st.set_page_config(
    page_title="Resumé - davins90",
    page_icon="💼",
)

utils.add_logo_and_name("app/images/foto_dani_cartoon.png","Daniele D'Avino",'Machine Learning Engineer @ Sky')

utils.sidebar_creation()

st.title("Resumé")

st.markdown("""

<sub><sup>Downloadable pdf version link at the bottom of the page</sup></sub>

## Employment

**Feb 2022 - Present : Machine Learning Engineer @ [Sky](https://www.skygroup.sky/)**
- I play a pivotal role in developing and deploying innovative machine learning solutions in the cloud for diverse challenges. My responsibilities include:
    1) Machine Learning Development:
        - Optimizing algorithms and tuning parameters for object detection, achieving a 10% improvement in accuracy.
        - Creating and deploying Generative AI tools for computer vision tasks (Speech Recognition).
        - Developing knowledge graphs and machine learning models for monitoring fraudulent activities over broadcast networks, focusing on real-world applicability.
    2) Cloud Engineering and Deployment:
        - Participating in the cloud migration strategy, transitioning from VMs to a microservices architecture using Docker and APIs, resulting in a 30% reduction in execution time and enhanced logging management.
        - Conducting code reviews and debugging, ensuring robust and efficient team output, and fostering collaboration within the team.

**June 2018 - Feb 2022 : Data Scientist @ [Wealthype](https://wealthype.ai/it/)**
- I've contributed to the development and management of several machine learning solutions delivered either as services (via API), as products (via Docker), or as consulting projects, following CRISP-DM process in an MLOps infrastructure. Main tasks:
    - Supervised & Unsupervised analysis on structured mixed data
    - Bayesian programming
    - Dataset Enrichment and Simulation
    - Network analysis
    - Master thesis projects tutoring
    - Webapp prototyping

**Feb 2016 - June 2018 : Quantitative Analyst @ AdviseOnly**
- Managed a wealth management digital platform on every field of the management flow (Engagement tools, profiling, asset allocation, risk analytics and CRM). Main tasks:
    - Portfolio construction & simulation
    - Forecasting scenarios
    - Risk metrics
    - Prepared report, analysis and wrote news about economics and financial thematic for financial blogs and banking institution.

## Volunteering

**November 2023 - Present : Data Scientist @ [MeteoNetwork ODV](https://www.meteonetwork.it/)**
- As a Data Scientist, I focus on ensuring the data quality of information sourced from weather stations to improve anomaly detection and guarantee the credibility of the data.

## Professional Certifications

**Microsoft**
- [Microsoft Professional Program in Data Science](app/attachments/MPP_DS.pdf)

  *Hot topics*: Querying and processing data, deploying supervised and unsupervised machine learning model, visualizing results and creating storytelling for data communication.
  
  *Software*: Power BI, Azure ML, T-SQL, Python
  
  *Final project*: Developed supervised machine learning model for predicting county-level rents in US, given socio-economic/demographic information.

- [Microsoft Professional Program in Artificial Intelligence](app/attachments/MPP_AI.pdf)

  *Hot topics*: Processing data, deploying deep learning and reinforcement learning model for imagine recognition and classification tasks.
  
  *Software*: Azure ML, Python
  
  *Final project*: Developed deep learning model (CNN) for classifying 11 types of appliances from their spectrogram, quantified by current and voltage measurements.

**Deeplearning.ai**
- [Deep Learning Specialization](https://www.coursera.org/account/accomplishments/specialization/FDUVU3VB74A2?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n)

  *Hot topics*: Deep Learning, Optimization, CNN, RNN, Structuring ML Projects

**Google**
- [Smart Analytics, Machine Learning and AI on Google Cloud Platform](https://www.coursera.org/account/accomplishments/certificate/EZN88N8XMET6)

  *Hot topics*: Google Cloud Platform, Google App Engine, Machine Learning, Big Query

- [Google Cybersecurity Certificate](https://www.credly.com/badges/a78db000-7a61-425e-a27a-a93e2425e488/linked_in_profile)

  *Hot topics*: Network Analysis, NIST Cybersecurity Framework, Intrusion Detection, SIEM tools


## Education

**Fourth Brain**
- 2022 - 2023: Machine Learning Engineer Curriculum

  *Hot topics*: Data-centric AI, AI application, MLOps, Artifical Intelligence, Machine Learning
  
  *Software*: Python, Docker, GCP, Airflow, Databricks

  *Thesis*: Developed and deployed [web application](https://www.linkedin.com/in/daniele-d-avino/overlay/education/854220748/multiple-media-viewer/?profileId=ACoAAAuBNf4Bv3yuFD3V8atLC4286uPUa4eqgmw&treasuryMediaId=1635518320160&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3B4REB0ZwDQFCyRKdXKJmbow%3D%3D) for delivering fraud detection and clustering customers for an e-commerce company. Frontend in Streamlit, Backend with Fast API, deployed on GCP.

**Università degli studi di Milano - Bicocca**
- 2013 -2016 : Master degree in Quantitative Finance

  *Hot topics*: Econometrics, Investment strategies & asset allocation, Investment banking
  
  *Software*: Matlab, R, Eviews, Stata, VBA, C++
  
  *Thesis*: Developed a risk-based investment strategies for my master’s degree thesis, using a Bayesian statistics model strengthen by an orthogonal GARCH model for risk estimation.

- 2009 - 2013 : Bachelor degree in Economics, marketing & market analysis

  *Hot topics*: Market-driven management, Macroeconomics, Statistics for marketing and customer clustering tecnique
  
  *Software*: VBA, C++, SQL
  
  *Thesis*: Synthetic ETF between financial innovation and regulatory constraints.

## Skills

I developed an agile working methodology using the following tools:
- *Proficient*: Python, SQL, GIT, Google Cloud Product (Cloud Storage, Artifact, Vertex AI), Docker, LLM
- *Familiar*: C++, Matlab, VBA, R, Tableau, AWS, Power BI, Bloomberg

[Click here](app/attachments/cv_daniele_davino.pdf) for a pdf version of my CV!
""", unsafe_allow_html=True)

