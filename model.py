
"""
	Classes for Spotify (Spotipy?) database
"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Song( DB.Model):

	__tablename__ = 'Song'

	id = DB.Column( DB.Integer, primary_key= True)
	track_id = DB.Column( DB.String( 22), nullable= False)
	songName = DB.Column( DB.String( 50), nullable= False)
	artistName = DB.Column( DB.String( 50), nullable= False)
	acousticness = DB.Column( DB.Numeric( 5, 4), nullable= False)
	danceability = DB.Column( DB.Numeric( 5, 4), nullable= False)
	duration = DB.Column( DB.BigInteger, nullable= False)
	energy = DB.Column( DB.Numeric( 5, 4), nullable= False)
	instrumentalness = DB.Column( DB.Numeric( 5, 4), nullable= False)
	musicalKey = DB.Column( DB.Integer, nullable= False)
	liveness = DB.Column( DB.Numeric( 5, 4), nullable= False)
	loudness = DB.Column( DB.Numeric( 5, 4), nullable= False)
	mode = DB.Column( DB.Integer, nullable= False)
	modulespeechiness = DB.Column( DB.Numeric( 5, 4), nullable= False)
	tempo = DB.Column( DB.Numeric( 6, 3), nullable= False)
	timeSig = DB.Column( DB.Integer, nullable= False)
	valence = DB.Column( DB.Numeric( 5, 4), nullable= False)
	popularity = DB.Column( DB.Integer, nullable= False)



	def __repr__( self):
		return '{} - {}'.format( self.artistName, self.songName)

class User( DB.Model):

	id = DB.Column( DB.Integer, primary_key= True)
	track_id = DB.Column( DB.String( 22), nullable= False)
	songName = DB.Column( DB.String( 50), nullable= False)
	artistName = DB.Column( DB.String( 50), nullable= False)

	def __repr__( self):
		return '{} - {}'.format( self.artistName, self.songName)

