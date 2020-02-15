import requests
from bs4 import BeautifulSoup
import json
import re

difficulty = ['easy', 'medium', 'hard']


def getBoard(level):
	global difficulty


	url = 'https://www.nytimes.com/puzzles/sudoku/' + difficulty[level]
	try:
		response = requests.get(url)
		if response:
			soup = BeautifulSoup(response.text, "html.parser")

			pattern = re.compile(r"window.gameData\s+=\s+({.*?})")

			script = soup.find("script", text=pattern)
			script = re.sub("<script.>", "", script.text).split('=', 1)[1]
			data = json.loads(script)

			board_data = data[difficulty[level]]['puzzle_data']['puzzle']
			return [board_data[x:x + 9] for x in range(0, len(board_data), 9)]
		else:
			response.raise_for_status()
	except requests.exceptions.RequestException as e:
		print(e)
		return
	except Exception as e:
		print(e)
		return

print(getBoard(1))