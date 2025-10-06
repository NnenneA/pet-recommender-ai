import pandas as pd

def get_pet_recommendations():
    """
    Main function to get pet recommendations based on user input.
    """
    # --- Step 1: Load the Data ---
   
    github_csv_url = 'https://raw.githubusercontent.com/Nnennea/pet-recommender-ai/main/pets.csv'
    
    try:
        pets_df = pd.read_csv(github_csv_url)
    except Exception as e:
        print(f"Error loading data from GitHub: {e}")
        print("Please ensure the repository is public and the file path is correct.")
        return

    # --- Step 2: Get User Input ---
    print("--- Pet Recommender Quiz ---")
    print("Answer the following questions to find your perfect pet match!\n")

    # Ask questions and store answers. We convert text answers to a consistent format.
    user_prefs = {}
    user_prefs['apartment_friendly'] = 'Yes' if input("Do you live in an apartment? (yes/no): ").lower() == 'yes' else 'No'
    user_prefs['energy_level'] = input("What is your desired energy level for a pet? (Low, Medium, High): ").capitalize()
    user_prefs['good_with_kids'] = 'Yes' if input("Do you have children or plan to? (yes/no): ").lower() == 'yes' else 'No'
    user_prefs['time_alone_tolerance'] = input("How long will the pet be alone most days? (Low, Medium, High tolerance needed): ").capitalize()
    user_prefs['grooming_needs'] = input("How much grooming are you willing to do? (Low, Medium, High): ").capitalize()

    # --- Step 3: Calculate Match Scores ---
    pets_df['match_score'] = 0 # Create a new column to store the score for each pet

    for index, pet in pets_df.iterrows():
        score = 0
        
        # Compare each user preference with the pet's attributes
        if pet['apartment_friendly'] == user_prefs['apartment_friendly']:
            score += 25 # This is a very important factor
        
        if pet['energy_level'] == user_prefs['energy_level']:
            score += 20
        
        if pet['good_with_kids'] == user_prefs['good_with_kids']:
            score += 20
            
        if pet['time_alone_tolerance'] == user_prefs['time_alone_tolerance']:
            score += 15
            
        if pet['grooming_needs'] == user_prefs['grooming_needs']:
            score += 10
        
        # Update the DataFrame with the calculated score for the current pet
        pets_df.loc[index, 'match_score'] = score

    # --- Step 4: Sort and Recommend ---
    # Sort the pets by the match score in descending order (highest score first)
    recommendations = pets_df.sort_values(by='match_score', ascending=False)

    print("\n--- Your Top 3 Pet Recommendations ---")
    # Get the top 3 pets from the sorted DataFrame
    top_3_pets = recommendations.head(3)

    for index, pet in top_3_pets.iterrows():
        print(f"\n1. {pet['pet_name']} (Score: {pet['match_score']})")
        print(f"   - Type: {pet['pet_type']}")
        print(f"   - Size: {pet['size']}")
        print(f"   - Average Monthly Cost: £{pet['avg_monthly_cost']}")
        print(f"   - Average Lifespan: {pet['avg_lifespan_years']} years")

# --- Run the recommender ---
if __name__ == '__main__':
    get_pet_recommendations()