from flask import Flask, render_template
from wm import app
import pytest

@pytest.fixture
def client():
	app.config["TESTING"] = True
	with app.test_client() as client:
		yield client

def test_base_route(client):
	url = "/"
	
	response = client.get(url)
	print(response)
	assert b"MyDumbApp" in response.get_data()
	assert response.status_code == 200
	
def test_second_page(client):
	url = "/José/3"
	
	response = client.get(url)
	print(response)
	assert b"Nico" not in response.get_data()
	assert response.status_code == 200
