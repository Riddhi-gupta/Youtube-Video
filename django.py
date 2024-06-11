# importing all the required modules 
#initialiaze django to give web application framework

from django.shortcuts import render, redirect 
from pytube import *

pip install pytube 
#It is a python module used to download youtube videos

def youtube(request): 

	# checking whether request.method is post or not 
	if request.method == 'POST': 
		
		# getting link from frontend 
		link = request.POST['link'] 
		video = YouTube(link) 

		# setting video resolution 
		stream = video.streams.get_lowest_resolution() 
		
		# downloads video 
		stream.download() 

		# returning HTML page 
		return render(request, 'youtube.html') 
	return render(request, 'youtube.html')
