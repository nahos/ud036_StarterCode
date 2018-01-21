#Creates a class movie
import webbrowser 
class Movie():
    #Below is the constructor for Movie Class
    def __init__(self, movie, storyline, image, trailer):#constructor, self is the object being created
        self.title = movie
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
	#Below Function shows the trailer of the movie instance
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
