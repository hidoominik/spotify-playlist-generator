# Spotify playlist generator

## Generate playlists with Billboard hot 100 songs from given day.

A Python program that scrapes data on the top 100 songs from a specified date using web scraping techniques. The user needs to provide the date for which they want to retrieve the song data. Additionally, the script requires certain credentials to be included in the `env` file, allowing the user to run the script with their Spotify API details.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hidoominik/spotify-playlist-generator.git

   ```

2. **Navigate to the project directory:**

   ```bash
   cd spotify-playlist-generator

   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Set Up Spotify API Credentials

Follow these steps to set up your Spotify API credentials:

1. **Create a Spotify Developer Account:**

   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Log in or create a new Spotify account.

2. **Create a New Application:**

   - Once logged in, click on the "Create an App" button.
   - Fill in the required information to create your application.
   - Note: This information is necessary to obtain the `client_id` and `client_secret` for authentication.

3. **Set Up a Redirect URI:**

   - After creating the application, go to the "Edit Settings" page.
   - Add a Redirect URI. This is the URI where Spotify will redirect after the user grants/denies permission.
   - Make sure the Redirect URI matches the one set in the `env` file.

4. **Create `env` File:**

   - In the project directory, create a file named `.env` (if not already present).
   - You can use `.env-template` file as a... template.
   - Add the following content to the file, replacing placeholders with your actual Spotify API credentials:

     ```env
     SPOTIPY_CLIENT_ID = your_client_id
     SPOTIPY_CLIENT_SECRET = your_client_secret
     SPOTIPY_USERNAME = your_spotify_username
     SPOTIPY_REDIRECT_URI = your_redirect_uri
     ```

     Replace `your_client_id`, `your_client_secret`, `your_spotify_username`, and `your_redirect_uri` with the corresponding credentials obtained from the Spotify Developer Dashboard.

Now, your Spotify API credentials are configured, and the program is ready to be run.
