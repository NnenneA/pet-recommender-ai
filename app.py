from flask import Flask, render_template, request
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# --- Load the Data ---
try:
    github_csv_url = 'https://raw.githubusercontent.com/Nnennea/pet-recommender-ai/main/pets.csv'
    pets_df = pd.read_csv(github_csv_url)
except Exception as e:
    print(f"Error loading data from GitHub: {e}")
    
    pets_df = pd.DataFrame() # Create an empty DataFrame

# --- Define Routes ---

# This is the main page with the quiz form
@app.route('/')
def home():
    # Renders the index.html template
    return render_template('index.html')

# This route handles the form submission and shows the results
@app.route('/recommend', methods=['POST'])
def recommend():
    if pets_df.empty:
        return "Sorry, the pet data could not be loaded. The application cannot proceed."

    # Get user's answers from the form
    user_prefs = {
        'apartment_friendly': request.form.get('apartment_friendly'),
        'energy_level': request.form.get('energy_level'),
        'good_with_kids': request.form.get('good_with_kids'),
        'time_alone_tolerance': request.form.get('time_alone_tolerance'),
        'grooming_needs': request.form.get('grooming_needs')
    }

   
    pets_df['match_score'] = 0
    for index, pet in pets_df.iterrows():
        score = 0
        if pet['apartment_friendly'] == user_prefs['apartment_friendly']:
            score += 25
        if pet['energy_level'] == user_prefs['energy_level']:
            score += 20
        if pet['good_with_kids'] == user_prefs['good_with_kids']:
            score += 20
        if pet['time_alone_tolerance'] == user_prefs['time_alone_tolerance']:
            score += 15
        if pet['grooming_needs'] == user_prefs['grooming_needs']:
            score += 10
        pets_df.loc[index, 'match_score'] = score

    # --- Sort and Get Top 3 Recommendations ---
    recommendations = pets_df.sort_values(by='match_score', ascending=False).head(3)
    
    # Convert the recommendations to a list of dictionaries to make it easy to use in the HTML template
    top_pets = recommendations.to_dict(orient='records')

    # Renders the results.html template, passing the recommendations to it
    return render_template('results.html', pets=top_pets)

# --- Run the App ---
if __name__ == '__main__':
    # The debug=True flag allows you to see errors in the browser and automatically reloads the app when you save changes.
    app.run(debug=True)