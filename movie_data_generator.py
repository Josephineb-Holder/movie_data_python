import requests  # For handling HTTP requests
import json  # For working with JSON data

# User inputs the movie title
movie_title = input("Enter the movie title: ")

# API URL with the key included
api_key = '4bbf40d'
url = f'http://www.omdbapi.com/?t={movie_title}&apikey={api_key}&plot=short&r=json'

# Sending the request to the API
response = requests.get(url)

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    movie_data = response.json()

    # Check if the movie data contains an error
    if 'Error' in movie_data:
        raise ValueError("No data found for the provided movie title.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
except ValueError as ve:
    print(ve)
else:
    print("Movie data retrieved successfully!")

if 'movie_data' in locals():  # Check if movie_data exists
    # Extract the title, year, and director from the movie data
    title = movie_data.get('Title', 'N/A')
    year = movie_data.get('Year', 'N/A')
    director = movie_data.get('Director', 'N/A')

    # Store the extracted information in a dictionary
    movie_info = {
        'Title': title,
        'Year': year,
        'Director': director
    }

    # Display the extracted movie information
    print(movie_info)

with open('movie_info.txt', 'w') as file:
    # Write the movie information to the text file in JSON format
    file.write(json.dumps(movie_info, indent=4))


def display_stored_movie_info():
    try:
        # Open and read the stored movie information from the file
        with open('movie_info.txt', 'r') as file:
            stored_data = json.load(file)
            print("Stored Movie Information:")
            # Print the stored data in a readable JSON format
            print(json.dumps(stored_data, indent=4))
    except FileNotFoundError:
        print("The file does not exist.")
    except json.JSONDecodeError:
        print("Error decoding the JSON data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Call the function to display the stored movie information
display_stored_movie_info()