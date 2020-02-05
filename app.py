
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

dfFileName = 'spotify2019.csv'


def fillDB():
	"""
	Fill database with given CSV
	"""
	engine = create_engine( 'sqlite:///spotify.db')
	df = pd.read_csv( dfFileName)
	df.to_sql( con= engine, index_label= 'id', 
			   name= Song.__tablename__, if_exists= 'replace')



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
	sendBackDummy = {'dummy': 1}
	sendBackInput = {
		'track_id': track_id
	}
	"""
	pass



@app.route( '/', methods= ['POST'])
def root():
	DB.drop_all()
	DB.create_all()

	fillDB()


	# < For loop here, potentially > (if track ID(s) will be passed in a list)
#	track_id = request.values[ 'track_id']

	lines = request.get_json( force= True)
	track_id = lines[ 'track_id']
	assert isinstance( track_id, str)


	DB.session.add( track_id)
	DB.commit()

"""
	return app.response_class( 
		response= json.dumps( send_back),
		status= 200,
		mimetype= 'application/json'
	)
"""


if __name__ == "__main__":
	root()


"""
populate Song table with csv
user > inputs( track_id)    (^ up there)
add that User.track_id to db > compare to Song.track_id to get all other fields
run model to find similar songs
export new track_ids OR Song.songName and Song.artistName


"""


