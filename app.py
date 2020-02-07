
"""
	Flask app for receiving spotify track IDs and returning suggested songs
	based on acoustic similarities
"""

import json
import pickle
from flask import Flask, request, render_template
from model import DB, Song, User
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

APP = Flask( __name__)
APP.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotify.db'
APP.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB.init_app( APP)

df_fileName = 'spotify2019.csv'
# engine = create_engine( 'sqlite:///spotify.db')
engine = create_engine( 'SQLALCHEMY_DATABASE_URI')
curse = engine.connect()


def fillSongDB():
	"""
	Fill db's Song table with given CSV
		(Does not need to execute every time app is run?)
	"""
	df = pd.read_csv( df_fileName)
	df.to_sql( con= engine, index_label= 'id', 
			   name= Song.__tablename__, if_exists= 'replace')


def parseInput():
	""" USE THIS IF: json input has song_url and not track_id """
	"""  """
	# test_case
	with open( 'test_in.json') as test:
		lines = json.load( test)
	#/test_case

  trackList = []

	for line in lines:
		track = line[ 'song_url'][-22:]
		
		if not isinstance( track, str):
			raise ValueError( 'Inappropriate type: must be a valid Spotify track ID')
		if track.rfind( "/") != -1:
			raise ValueError( "Inappropriate type: Entry " + \
					line[ 'song_name'] + \
				"'s ID ({}) is not a valid Spotify song ID".format( 
					line[ 'song_url'][-22:])
			)
		trackList.append( track)

	# 	DB.session.add( User.track_id)
	# DB.commit()

	return trackList


def suggestSong( trackList):

	whatDoesThisDo = []

	with open( 'knn', 'rb') as pred:
		model = pickle.load( pred)

	for track in trackList:
		# songInput = Song.query.filter( Song.track_id == track)

		t = text( "SELECT * FROM Song WHERE track_id IN (:trackID);")
		songInput = curse.execute( t, trackID= track)
		referenceData = songInput.fetchall()
		referenceData = list( referenceData[0])

		songData = referenceData
		del songData[:4], songData[2], songData[4], songData[6], songData[8]

		"""
		drop cols 0,1,2,3,6,9,12,15 = 
			id, a-name, t-id, t-name, 
			duration, key, mode, t-sig,

		keep cols 4,5,7,8,10,11,13,14,16, 17 = 
			ac-ness, d-lity, nrg, inst, 
			liven, loudn, spchn, tmpo, 
			vale, pop

		0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
		--------------------------------------------
		X  X  X  X 
		4  5  6  7  8  9 10 11 12 13 14 15 16 17
			  X
		4  5  7  8  9 10 11 12 13 14 15 16 17
					X
		4  5  7  8 10 11 12 13 14 15 16 17
						 XX
		4  5  7  9 10 11 13 14 15 16 17
							   XX
		4  5  7  9 10 11 13 14 16 17

		"""

		whatDoesThisDo = model.predict( [[songData]])

		return whatDoesThisDo


# def exportSuggestion():

#	< Does this need to be in a For loop? >
#	sendBack = {'suggestion': 'track_id'}
#	sendBack = ['artists', {'test': 'artist1'},
#				'songs', {'another test': 'artist2'}
#	]
#	return sendBack
	

def main():
	"""	Create main instance of Song Suggester flask application """


	@APP.route( '/', methods= ['POST'])
	def root():

		# if database_exists( engine.url) == False:
		# 	"""if specified db doesn't exist, create and run function to populate"""
		DB.drop_all()
		DB.create_all()
		fillSongDB()

		# < Alternative methods to get track id? > (depends on backend, who has been MIA since Tuesday..)
		# lines = request.values[ 'track_id']
		# lines = request.args.get( 'seed', 
		# 						default= '5xTtaWoae3wi06K5WfVUUH',	# Haters gonna hate, hate, hate, hate, hate
		# 						type= 'str')

		# """ get input from front-end/json and save it to User table in db """
		# lines = request.get_json( force= True)
		# for line in lines:
		# 	User.track_id = lines[ 'track_id']
		# 	assert isinstance( User.track_id, str)
		# 	DB.session.add( User.track_id)
		# DB.commit()


		export = suggestSong( parseInput())


		return APP.response_class( 
			response= json.dumps( export),
			status= 200,
			mimetype= 'application/json'
		)


	# return APP

if __name__ == "__main__":
	main()


"""
populate Song table with csv
user > inputs( track_id)    (^ up there)
add that User.track_id to db > compare to Song.track_id to get all other fields
run model to find similar songs
export new track_ids OR Song.songName and Song.artistName


"""


