
"""
	Flask app for receiving spotify track IDs and returning suggested songs
	based on acoustic similarities
"""

from flask import Flask, request, render_template
from model import Song, User

app = Flask( __name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB.init_app( app)


@APP.route( '/', methods= ['POST'])
def root():
	DB.drop_all()
	DB.create_all()

	# < Potential For loop here > (if multiple trackIDs will be passed in a list)
	track_id = request.values[ 'track_id']

	DB.session.add( track_id)
	DB.commit()


def suggestSong():
	pass


def exportSuggestion():
	pass



"""
populate Song table with csv
user > inputs( track_id)    (^ up there)
add that User.track_id to db > compare to Song.track_id to get all other fields
run model to find similar songs
export new track_ids OR Song.songName and Song.artistName