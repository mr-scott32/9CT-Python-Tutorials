import spotipy  # Import the Spotipy library for interacting with the Spotify API
from spotipy.oauth2 import SpotifyOAuth  # Import SpotifyOAuth for authentication

# Set up your Spotify app credentials
client_id = '3b30137c0f2842518c6e33befcd22b78'  # Your Spotify client ID
client_secret = '3d731db349634f80bebda8c8e16203d7'  # Your Spotify client secret
redirect_uri = 'http://localhost:3000/callback'  # Redirect URI after authorization, adjust as needed
scope = 'playlist-modify-public'  # Scope for the authorization, adjust as needed

# Obtain the authorization URL
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
auth_url = sp_oauth.get_authorize_url()  # Get the authorization URL

# Print the authorization URL and visit it in your browser
print("Please visit this URL to authorize your Spotify account:", auth_url)

# After authorization, paste the redirected URL here
redirect_response = input("Paste the redirect URL here: ")

# Extract the authorization code from the redirected URL
code = sp_oauth.parse_response_code(redirect_response)

# Exchange the authorization code for an access token
token_info = sp_oauth.get_cached_token()
access_token = token_info['access_token']

# Check if access token was obtained successfully
if token_info:
    # Use the access token to make Spotify API requests
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    # Fetch the user's information
    user_info = sp.current_user()
    user_id = user_info['id']
    
    # Example: Create a playlist
    playlist_name = "My Playlist"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    
    # Fetch the five most popular Taylor Swift songs
    artist = "Taylor Swift"
    results = sp.search(q=artist, type='artist')
    taylor_swift_id = results['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(taylor_swift_id)

    # Extract the track URIs
    track_uris = [track['uri'] for track in top_tracks['tracks']]

    # Add the tracks to the playlist
    sp.playlist_add_items(playlist['id'], track_uris)

    print(f"Playlist created successfully and populated with the top {artist} songs!")

else:
    print("Failed to obtain access token.")
