import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

# Configuration de l'apparence de Streamlit avec un fond noir
st.markdown(
    """
    <style>
    .reportview-container {
        background: #2c2f38;
        color: white;
    }
    .sidebar .sidebar-content {
        background: #2c2f38;
        color: white;
    }
    .css-1d391kg {
        color: white;
    }
    .css-145kmo2 {
        color: white;
    }
    .css-1v3fvcr {
        background-color: #2c2f38;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Fonction pour afficher le tableau de bord principal
def display_dashboard():
    st.title('Data Analysis of OCTO Technologies')

    # Données pour les graphiques
    total_employees = 360
    female_employees = 120
    male_employees = 240

    # Données spécifiques au secteur
    it_services_employees = 150
    software_dev_employees = 100
    digital_transformation_employees = 110

    # Répartition par genre dans chaque secteur
    gender_sector_data = {
        "Sector": ["IT Services", "Software Development", "Digital Transformation"],
        "Women": [50, 30, 40],
        "Men": [100, 70, 70]
    }

    # Création de DataFrame pour la répartition par genre
    gender_sector_df = pd.DataFrame(gender_sector_data)

    # Données hypothétiques sur les salaires moyens et les niveaux d'expérience par secteur
    average_salaries = {
        "Sector": ["IT Services", "Software Development", "Digital Transformation"],
        "Average Salary": [60000, 65000, 70000]
    }

    experience_levels = {
        "Sector": ["IT Services", "Software Development", "Digital Transformation"],
        "Average Years of Experience": [5, 6, 7]
    }

    # Création de DataFrames pour les nouvelles données
    average_salaries_df = pd.DataFrame(average_salaries)
    experience_levels_df = pd.DataFrame(experience_levels)

    # Disposition en colonnes pour organiser les graphiques comme un tableau de bord
    col1, col2 = st.columns(2)

    # Premier graphique: Répartition par genre
    with col1:
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.pie([female_employees, male_employees], labels=["Women", "Men"], colors=["#ff9999","#66b3ff"], autopct='%1.1f%%', startangle=140)
        ax1.axis('equal')
        st.pyplot(fig1)
        plt.close(fig1)

    # Deuxième graphique: Répartition des employés par secteur
    with col2:
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.bar(["IT Services", "Software Development", "Digital Transformation"], [it_services_employees, software_dev_employees, digital_transformation_employees], color=['#ff9999','#66b3ff','#99ff99'])
        plt.title('Employment Distribution by Sector')
        plt.ylabel('Number of Employees')
        plt.xlabel('Sectors')
        st.pyplot(fig2)
        plt.close(fig2)

    # Troisième graphique: Répartition par genre dans les différents secteurs (graphique linéaire)
    with col1:
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        ax3.plot(gender_sector_df["Sector"], gender_sector_df["Women"], marker='o', label='Women', color='#ff9999')
        ax3.plot(gender_sector_df["Sector"], gender_sector_df["Men"], marker='o', label='Men', color='#66b3ff')
        plt.title('Gender Distribution Across Sectors')
        plt.ylabel('Number of Employees')
        plt.xlabel('Sectors')
        plt.legend()
        st.pyplot(fig3)
        plt.close(fig3)



    # Cinquième graphique: Salaires moyens par secteur
    with col1:
        fig5, ax5 = plt.subplots(figsize=(8, 5))
        ax5.plot(average_salaries_df["Sector"], average_salaries_df["Average Salary"], marker='o', color='#ffa500')
        plt.title('Average Salaries by Sector')
        plt.ylabel('Average Salary (€)')
        plt.xlabel('Sectors')
        st.pyplot(fig5)
        plt.close(fig5)

    # Sixième graphique: Années d'expérience moyennes par secteur
    with col2:
        fig6, ax6 = plt.subplots(figsize=(8, 5))
        ax6.bar(experience_levels_df["Sector"], experience_levels_df["Average Years of Experience"], color=['#ff9999','#66b3ff','#99ff99'])
        plt.title('Average Years of Experience by Sector')
        plt.ylabel('Average Years of Experience')
        plt.xlabel('Sectors')
        st.pyplot(fig6)
        plt.close(fig6)

    # Septième graphique: Relation entre les salaires et les années d'expérience
    st.subheader('Salaries vs. Years of Experience (Scatter Plot)')
    fig7, ax7 = plt.subplots(figsize=(16, 10))
    ax7.scatter(average_salaries_df["Average Salary"], experience_levels_df["Average Years of Experience"], color='#00bfff')
    plt.title('Salaries vs. Years of Experience')
    plt.ylabel('Average Years of Experience')
    plt.xlabel('Average Salary (€)')
    st.pyplot(fig7)
    plt.close(fig7)

    # Nouveau graphique: Chiffre d'affaires et bénéfice net au fil du temps
    st.subheader('Revenue and Net Income Over Time')
    revenue_data = {
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Revenue": [100, 110, 120, 128.3, 135],
        "Net Income": [7, 8, 8.5, 9.3, 10]
    }
    revenue_df = pd.DataFrame(revenue_data)
    fig8, ax8 = plt.subplots(figsize=(10, 5))
    ax8.plot(revenue_df['Year'], revenue_df['Revenue'], marker='o', label='Revenue')
    ax8.plot(revenue_df['Year'], revenue_df['Net Income'], marker='o', label='Net Income')
    plt.title('Revenue and Net Income Over Time')
    plt.xlabel('Year')
    plt.ylabel('Amount (€ millions)')
    plt.legend()
    st.pyplot(fig8)
    plt.close(fig8)

    # Nouveau graphique: Répartition des employés par département
    st.subheader('Employee Distribution by Department')
    employee_distribution = {
        "Department": ["IT Services", "Software Development", "Digital Transformation"],
        "Employees": [150, 100, 110]
    }
    employee_distribution_df = pd.DataFrame(employee_distribution)
    fig9, ax9 = plt.subplots(figsize=(10, 5))
    ax9.bar(employee_distribution_df['Department'], employee_distribution_df['Employees'], color=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Employee Distribution by Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')
    st.pyplot(fig9)
    plt.close(fig9)

    # Nouveau graphique: Répartition par genre dans les départements
    st.subheader('Gender Distribution by Department')
    gender_department_data = {
        "Department": ["IT Services", "Software Development", "Digital Transformation"],
        "Women": [50, 30, 40],
        "Men": [100, 70, 70]
    }
    gender_department_df = pd.DataFrame(gender_department_data)
    fig10, ax10 = plt.subplots(figsize=(10, 5))
    ax10.bar(gender_department_df['Department'], gender_department_df['Women'], label='Women', color='#ff9999')
    ax10.bar(gender_department_df['Department'], gender_department_df['Men'], bottom=gender_department_df['Women'], label='Men', color='#66b3ff')
    plt.title('Gender Distribution by Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')
    plt.legend()
    st.pyplot(fig10)
    plt.close(fig10)

    # Nouveau graphique: Salaires moyens par département
    st.subheader('Average Salary by Department')
    salary_department_data = {
        "Department": ["IT Services", "Software Development", "Digital Transformation"],
         "Average Salary": [60000, 65000, 70000]
    }
    salary_department_df = pd.DataFrame(salary_department_data)
    fig11, ax11 = plt.subplots(figsize=(10, 5))
    ax11.bar(salary_department_df['Department'], salary_department_df['Average Salary'], color=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Average Salary by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Salary (€)')
    st.pyplot(fig11)
    plt.close(fig11)

    # Nouveau graphique: Années d'expérience moyennes par département
    st.subheader('Years of Experience by Department')
    experience_department_data = {
        "Department": ["IT Services", "Software Development", "Digital Transformation"],
        "Average Years of Experience": [5, 6, 7]
    }
    experience_department_df = pd.DataFrame(experience_department_data)
    fig12, ax12 = plt.subplots(figsize=(10, 5))
    ax12.bar(experience_department_df['Department'], experience_department_df['Average Years of Experience'], color=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Years of Experience by Department')
    plt.xlabel('Department')
    plt.ylabel('Average Years of Experience')
    st.pyplot(fig12)
    plt.close(fig12)

    # Nouveau graphique: Scores de diversité et d'inclusion
    st.subheader('Diversity and Inclusion Scores')
    diversity_scores_data = {
        "Metric": ["Diversity, Equity & Inclusion", "Economic Impact", "Civic Engagement & Giving", "Supply Chain Management"],
        "Score": [4.8, 4.5, 3.6, 1.4]
    }
    diversity_scores_df = pd.DataFrame(diversity_scores_data)
    fig13, ax13 = plt.subplots(figsize=(10, 5))
    ax13.bar(diversity_scores_df['Metric'], diversity_scores_df['Score'], color='#66b3ff')
    plt.title('Diversity and Inclusion Scores')
    plt.xlabel('Metric')
    plt.ylabel('Score')
    st.pyplot(fig13)
    plt.close(fig13)

     # Ajouter la section des sources à la fin de la page OCTO
    st.subheader('Sources')
    st.markdown("""
    - [PitchBook](https://pitchbook.com/)
    - [Craft.co](https://craft.co/)
    - [OCTO Technology Official Website](https://www.octo.com/)
    - [B Lab Global](https://bcorporation.net/)
    """)

# Locations of OCTO Technology offices
def display_locations():
    st.subheader('Locations of OCTO Technology offices')
    # Locations of OCTO Technology offices
    locations = {
        "Paris, France": (48.8566, 2.3522),
        "Lille, France": (50.6292, 3.0573),
        "Marseille, France": (43.2965, 5.3698),
        "Toulouse, France": (43.6047, 1.4442),
        "Rabat, Morocco": (34.0209, -6.8417)
    }

    # Create a map centered around France and Morocco
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=5)

    # Add the locations to the map
    for location, coords in locations.items():
        folium.Marker(location=coords, popup=location).add_to(m)

    # Save the map to an HTML file
    m.save('octo_offices_map.html')

    # Read the HTML file and display it in Streamlit
    with open('octo_offices_map.html', 'r') as f:
        map_html = f.read()

    st.components.v1.html(map_html, width=700, height=500)



# Fonction pour afficher les informations de certifications
def display_certifications():
    st.title("Certifications")

    st.markdown("""
    ### Microsoft Azure Fundamentals AZ900
    This certification demonstrates foundational level knowledge of cloud services and how those services are provided with Microsoft Azure. It covers general cloud computing concepts as well as services such as Azure subscriptions, planning and management, and Azure pricing and support. [Learn more](https://docs.microsoft.com/en-us/learn/certifications/azure-fundamentals/)
    """)
    st.image("/workspaces/octo-dashboard/AZ900.png", width=300)
    
    st.markdown("""
    ### Microsoft Azure AI Fundamentals AI900
    This certification is an opportunity to demonstrate knowledge of common AI and machine learning workloads and how to implement them on Azure. It covers AI considerations, fundamental principles of machine learning on Azure, and features of computer vision workloads on Azure. [Learn more](https://docs.microsoft.com/en-us/learn/certifications/azure-ai-fundamentals/)
    """)
    st.image("/workspaces/octo-dashboard/data/azure-ai-fundamentals-600x600.png", width=300)
    
    st.markdown("""
    ### Google Data Analytics Professional Certificate
    This certification enables you to gain job-ready skills that are in demand, like how to analyze and process data to gain key business insights. Topics covered include data cleaning, data analysis, data visualization, SQL, R programming, and developing a data-driven mindset. [Learn more](https://www.coursera.org/professional-certificates/google-data-analytics)
    """)
    st.image("/workspaces/octo-dashboard/data/google.png", width=300)

    st.markdown("""
    ### Coursera: Machine Learning Specialization, University of Washington, USA
    This specialization provides a broad introduction to modern machine learning, including supervised learning (multiple linear regression, logistic regression, neural networks, support vector machines), unsupervised learning (clustering, dimensionality reduction, recommender systems), and best practices in machine learning (bias/variance theory, innovation process in machine learning and AI). [Learn more](https://www.coursera.org/specializations/machine-learning)
    """)
    
    st.markdown("""
    ### AWS Certified Data Engineer (In Progress)
    This certification demonstrates expertise in data lakes and analytics services in the AWS ecosystem. It includes understanding the lifecycle of data, ingestion, storage, processing, and visualization, and working with AWS services like AWS Glue, Amazon Redshift, and Amazon Quicksight. [Learn more](https://aws.amazon.com/certification/certified-data-analytics-specialty/)
    """)
    st.image("data/Screenshot 2024-07-29 at 7.40.19 AM.png", width=300)


# Fonction pour afficher le profil
def display_profile():
    st.title("Profile")
    
    # Display the image
    st.image("/workspaces/octo-dashboard/data/IMG_4333.JPG", width=300)
    st.markdown("""
    ## Sabine Dawaliby

    ### Education
    - **Master Software Engineering**, EFREI Paris, Panthéon-Assas University, 2021-2024
    - **Bachelor's Degree in Advanced Mathematics**, University of Poitiers, Faculty of Fundamental and Applied Sciences, 2019-2021
    - **Specialization in Business Intelligence and Analytics**

    ### Experience
    - **Data Engineer/Data Analyst**, Société Générale, Paris (September 2022 - August 2024)
        - Structuring and analyzing the data from the Group referential
        - Deploying CI/CD pipelines and monitoring production deployments
        - Districts of each datalake used by the Group

    - **Mobile Developer**, Caplogy, Paris (September 2021 - August 2022)
        - Developing applications using Flutter and Dart
        - Creating multi-purpose digital interfaces

    - **Cross-Functional Project**, Bouygues Telecom, Paris (September 2023 - January 2024)
        - Modeling the data ontology as part of the development of the Data Market place of Bouygues Telecom
        - Mapping and enriching their databases with web scraping (using openAI models to clean the data)

    - **COVID-19 Referent**, CROUS, Paris (April 2020 - July 2020)
        - Calling residents of the CROUS to ask and help people in need
        - Connecting students in need to specialists and psychologists

    ### Skills

    #### Languages
    - **French**: Fluent
    - **English**: Fluent (TOEIC Score: 945)
    - **Arabic**: Native language

    #### Technical Skills
    - **Programming Languages**: Python, R, Scala, Spark, Java, Dart/Flutter
    - **Data Processing**: Hadoop (HDFS, Hive), Talend
    - **Machine Learning & Data Analytics**: Pandas, NumPy, Scikit-Learn, PowerBI, Tableau
    - **Databases**: SQL, Excel, Elastiksearch, MongoDB, Cassandra
    - **Dev Tools**: Git, Docker, Jenkins
    - **ETL Tools**: Talend

    #### Soft Skills
    - Leadership
    - Decision making
    - Effective communication
    - Adaptability

    ### Hobbies
    - Photography
    - Cultural exploration
    - Painting/Drawing

    ### Contact Information
    - **Phone**: 07 79 56 62 89
    - **LinkedIn**: [Sabine Dawaliby](https://www.linkedin.com/in/sabinedawaliby)
    - **Email**: sabinedawaliby@gmail.com
    - **Driver's license**: B
    """)
# Create a Streamlit app with navigation
page = st.selectbox(
    "Navigation",
    ["OCTO", "Locations", "Certifications", "Profile"]
)

# Call the appropriate function based on the selected page
if page == "OCTO":
    display_dashboard()
elif page == "Locations":
    display_locations()
elif page == "Certifications":
    display_certifications()
elif page == "Profile":
    display_profile()

