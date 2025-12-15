# Musical Time Machine (Spotify Playlist Generator)

A Python script that travels back in time to create a custom Spotify playlist of the top global hits from any specific date in history.

By combining web scraping with the Spotify API, this tool fetches historical chart data and automatically builds a private playlist in your Spotify account, allowing you to experience the music of the past instantly.

## Demo

![Spotify Playlist Demo](spotify_playlist_screenshot.png)

## Key Features

-   **Historical Data Scraping:** Scrapes `kworb.net` to retrieve the top global songs from a specific date input by the user.
-   **Spotify Integration:** Uses the `Spotipy` library to authenticate with your Spotify account securely.
-   **Intelligent Searching:** Searches the Spotify catalog for each song title, filtering by the correct year to ensure accuracy.
-   **Automated Playlist Creation:** Creates a new private playlist (e.g., "old_gold 2010-05-20") and adds the found tracks automatically.
-   **Error Handling:** Gracefully handles cases where a song from the charts isn't available on Spotify, skipping it without crashing the program.

## Technologies Used

-   **Python 3.x**
-   **[Spotipy](https://spotipy.readthedocs.io/)**: A lightweight Python library for the Spotify Web API. It handles the complex OAuth authentication and API requests.
-   **[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)**: Used for parsing HTML and scraping song titles from historical chart archives.
-   **[Requests](https://pypi.org/project/requests/)**: Used to fetch the HTML data from the chart website.
-   **pprint**: Utilized to structure the complex JSON responses from Spotify for better readability.

## Project Setup

This project requires a bit of setup on the Spotify Developer Dashboard. Follow these steps carefully.

### 1. Prerequisites

-   Python 3.x installed.
-   A Spotify Account (Free or Premium).
-   `pip` (Python package installer).

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dheerajdhami2001-cyber/musical-time-machine.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd musical-time-machine
    ```

3.  **Install dependencies:**
    ```bash
    pip install requests bs4 spotipy
    ```

### 3. Spotify API Configuration (Crucial Step)

To allow Python to talk to your Spotify account, you need to create a "Spotify App".

1.  Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
2.  Click **"Create An App"**. Give it a name (e.g., "Time Machine") and a description.
3.  Once created, click **"Edit Settings"**.
4.  Scroll down to **Redirect URIs**. Add the following URL exactly:
    `http://127.0.0.1:8888/callback`
5.  Click **"Save"**.
6.  On your App's main page, find your **Client ID** and **Client Secret**. (Click "Show Client Secret" to see it).

### 4. Configure the Script

Open `main.py` and replace the placeholder values with your actual credentials:

```python
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="YOUR_ACTUAL_CLIENT_ID",
        client_secret="YOUR_ACTUAL_CLIENT_SECRET",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token_new.txt"
    )
)
```
How to Run
Run the script:
code
Bash
python main.py
Authentication: The first time you run this, a browser window will open asking you to authorize the app to access your Spotify account. Click Agree.
Redirect: You will be redirected to a page (likely Not Found or Localhost). Copy the entire URL from your browser's address bar.
Paste: Paste that URL into the terminal where the script is running and hit Enter. (This creates a token_new.txt file so you won't have to log in again).
Enter Date: When prompted, type the date you want to travel to in YYYYMMDD format.
Example: For August 12, 2000, type 20000812.
Enjoy: Open your Spotify app, and check your Library. Your new "Time Capsule" playlist will be there!
Acknowledgments
This project was inspired by and completed with the guidance of the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.
