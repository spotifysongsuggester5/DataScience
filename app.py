
"""
	Flask app for receiving spotify track IDs and returning suggested songs
	based on acoustic similarities
"""

import pickle
from flask import Flask, request, render_template
from model import DB, Song, User

app = Flask( __name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB.init_app( app)


def fillDB():
	"""
	"""
	pass


def suggestSong():
	"""	An example:
	with open( 'model.pickle', 'rb') as mod:
		model = pickle.load( mod)

	return model.predict([[ ]])
	"""

	pass


def exportSuggestion():
	""" An example:
	sendBack = {'suggestion': output}
	send_back_dummy = {'dummy': 1}
	send_back_input = {
		'track_id': track_id
	}
	"""
	pass



@app.route( '/', methods= ['POST'])
def root():
	DB.drop_all()
	DB.create_all()

	# < For loop here, potentially > (if track ID(s) will be passed in a list)
#	track_id = request.values[ 'track_id']

	lines = request.get_json( force= True)
	track_id = lines[ 'track_id']
	assert isinstance( track_id, str)


	DB.session.add( track_id)
	DB.commit()





if __name__ == "__main__":
	root()


"""
populate Song table with csv
user > inputs( track_id)    (^ up there)
add that User.track_id to db > compare to Song.track_id to get all other fields
run model to find similar songs
export new track_ids OR Song.songName and Song.artistName


"""


