Pet Recommender AI
Project Description
Pet Recommender AI is a data-driven application designed to help prospective pet owners find the perfect animal companion based on their lifestyle, personality, and living situation. By answering a short questionnaire, users receive a personalized recommendation of pet species that are a great match for them.

The Problem
Many new pet owners are unsure which animal best fits their life. This can lead to stress for both the owner and the pet, and in some cases, can result in pets being returned to shelters. This project aims to solve that problem by using data to make a more informed and responsible choice.

How It Works
The core of this project is a scoring algorithm. The system works in three steps:

Data Collection: A custom dataset (pets.csv) was created, containing key characteristics of various pet species (e.g., energy level, grooming needs, suitability for apartments).

User Questionnaire: The user provides information about their life through a simple survey.

Matching Algorithm: A Python script calculates a "compatibility score" between the user's answers and the traits of each pet in the dataset.

Recommendation: The application presents the top 3 pets with the highest compatibility scores to the user.

Key Features
An intuitive questionnaire for users.

A scoring system to rank pets based on compatibility.

A clean and simple display of the recommended pets.

Technologies Used
Language: Python

Libraries: Pandas (for data manipulation)

(Future additions): Scikit-learn (for machine learning models), Flask/Streamlit (for a web interface)
