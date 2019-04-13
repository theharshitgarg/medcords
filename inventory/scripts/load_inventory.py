import requests
import time
import random

def make_purchase():
	data = {
		"items": [
			{ "id": 1, "quantity": 100 },
			{ "id": 10, "quantity": 30 },
			{ "id": 100, "quantity": 10 },
		]
	}
	url = "http://127.0.0.1:8000/inventory/purchase"
	response = requests.post(url, json=data)
	print response.content


def get_list():
	url = "http://127.0.0.1:8000/inventory/list/?"
	params = "format=json&page=10&per_page=" + str(random.randint(1, 20))

	response = requests.get(url + "?" + params)

	print response.content

while True:
	if random.randint(0, 1) % 2 == 1:
		get_list()
	else:
		make_purchase()

	time.sleep(10)