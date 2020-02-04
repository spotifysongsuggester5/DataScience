
"""
	Classes for Spotify (Spotipy?) database
"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Song( DB.model):
	track_id = DB.Column( DB.String( 25), primary_key= True)
	songName = DB.Column( DB.String( 50), nullable= False)
	artistName = DB.Column( DB.String( 50), nullable= False)
	acousticness
	danceability
	duration
	energy
	instrumentalness
	musicalKey
	liveness
	loudness
	modulespeechiness
	tempo
	timeSig
	valence
	popularity


	def __repr__( self):
		return '{} - {}'.format( self.artistName, self.songName)

class User( DB.Model):
	track_id = DB.Column( DB.String( 25), primary_key= True)

	def __repr__( self):
		return '{}'.format( self.track_id)