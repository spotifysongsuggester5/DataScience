  
"""
	Flask app for receiving spotify track IDs and returning suggested songs
	based on acoustic similarities
"""

from flask import Flask
from flask import request

APP = Flask( __name__)


@APP.rout( '/')