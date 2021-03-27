from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=8CD4E7FA-71DE-42D5-A146-F9898A15B5CB")

	#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=8CD4E7FA-71DE-42D5-A146-F9898A15B5CB

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."
		

	return render(request, 'home.html' , {'api': api})


def about(request):
	return render(request, 'about.html' , {})