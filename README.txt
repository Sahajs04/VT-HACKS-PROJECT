Before running webcam.py, paste the following into the terminal:

curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=4d502f92f4834f4483913b53415b4e24&client_secret=4b050805c79940aeb6fc5d84eab88ba2"

this grants an access token that is valid for one hour
