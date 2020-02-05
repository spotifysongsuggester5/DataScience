# DataScience
Repo for the data science team


### Planned API usage (WIP)

At the app's address `spotify-song-suggester-5.heroku.com`, along the appropriate route (currently pointed at `/`), please send the
object `{'track_id': 'xxxxXxxxxXxxxxXxxxxXxx'}` (also known as Spotify ID, from Spotify's Web API: the 22-char, base-62 identifier that's unique for every song in Spotify's catalogue)

And along with a 200 status, you will receive the object `{'artist_name': 'artist name', 'song_name': 'song name'}`


#### What happens in between the above input/output (WIP)

- Internal `Spotify.db` database's Song table is populated from accompanying .csv

- Song table is filtered by received track_id or track_ids, to get songs' identifying metrics and characteristics

- Characteristics are fed to pickled prediction/comparison/suggestion model, which utilizes trained, unsupervised  
  K-Nearest Neighbour logic to find 10 most similar songs by characteristics, returning index_ids

- < TODO: CREATE VISUALIZATIONS, based on fed and returned characteristics >

- Refer back to Song table, filtering by returned index_ids to get artist and song names

- Build dictionary of filtered artist and song names to send back, along with vizualizations

