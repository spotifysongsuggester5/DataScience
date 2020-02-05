
"""
	Flask app for receiving spotify track IDs and returning suggested songs
	based on acoustic similarities
"""

import pickle
from flask import Flask, request, render_template
from model import DB, Song, User
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

app = Flask( __name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB.init_app( app)

dfFileName = 'spotify2019.csv'
engine = create_engine( 'sqlite:///spotify.db')

def fillSongDB():
	"""
	Fill DB's Song table with given CSV
		(Does not need to execute every time app is run?)
	"""
	df = pd.read_csv( dfFileName)
	df.to_sql( con= engine, index_label= 'id', 
			   name= Song.__tablename__, if_exists= 'replace')



def suggestSong():
	"""	An example:
	with open( 'model.pickle', 'rb') as mod:
		model = pickle.load( mod)

	songInput = Song.query.filter( Song.track_id == User.track_id)
	return model.predict([[ songInput]])
	"""
	pass


def exportSuggestion():
	""" An example:
	sendBack = {'suggestion': 'track_id'}
	sendBackDummy = {'dummy': 1}		# minimal functionality for testing
	sendBackInput = {					# verify input working as expected
		'track_id': track_id
	}

	return sendBack
	"""
	pass



@app.route( '/', methods= ['POST'])
def main():

	if database_exists( *engine.url):
		DB.drop_all()
		DB.create_all()

		fillSongDB()


	# < For loop here, potentially > (if track ID(s) will be passed in a list)
#	track_id = request.values[ 'track_id']

	lines = request.get_json( force= True)
	User.track_id = lines[ 'track_id']
	assert isinstance( User.track_id, str)

	DB.session.add( User.track_id)
	DB.commit()

"""
	return app.response_class( 
		response= json.dumps( send_back),
		status= 200,
		mimetype= 'application/json'
	)
"""


if __name__ == "__main__":
	main()


"""
populate Song table with csv
user > inputs( track_id)    (^ up there)
add that User.track_id to db > compare to Song.track_id to get all other fields
run model to find similar songs
export new track_ids OR Song.songName and Song.artistName


"""


