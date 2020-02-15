import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import re

difficulty = ['easy', 'medium', 'hard']


def getBoard(level):
	global difficulty
	url = 'https://www.nytimes.com/puzzles/sudoku/' + difficulty[level]

	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")

	pattern = re.compile(r"window.gameData\s+=\s+({.*?})")

	script = soup.find("script", text=pattern)
	script = re.sub("<script.>", "", script.text).split('=', 1)[1]
	data = json.loads(script)

	board_data = data[difficulty[level]]['puzzle_data']['puzzle']

	return [board_data[x:x + 9] for x in range(0, len(board_data), 9)]


