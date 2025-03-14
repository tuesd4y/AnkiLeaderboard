import os

def get_db_path():
	db = os.environ.get('LEADERBOARD_DB')
	if db is None:
		# todo
		db = 'Leaderboard.db'

	return db

def praw_config():
	return None

def smtp_config():
	return None