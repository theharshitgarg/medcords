import requests
import time
import random

def make_purchase():
	pass


def get_list():
	url = "http://127.0.0.1:8000/inventory/list/?"
	params = "format=json&page=10&per_page=10"

	response = requests.get(url + "?" + params)

	print response.content

while True:
	if random.randint(0, 1) % 2 == 1:
		get_list()
	else:
		make_purchase()

	time.sleep(10)