# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 06/05/2024
# Description: Defines the Movie, Streaming Service, and Streaming Guide classes as specified.
class Movie:
    """A class to represent a movie with title, genre, director and year information."""
    def __init__(self, title, genre, director, year):
        """Initialize the movie object."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year
    def get_title(self):
        """Return the title of the movie."""
        return self._title
    def get_genre(self):
        """Return the genre of the movie."""
        return self._genre
    def get_director(self):
        """Return the director of the movie."""
        return self._director
    def get_year(self):
        """Return the year of the movie."""
        return self._year
class StreamingService:
    """A class to represent a streaming service with a name and a catalog of movies."""
    def __init__(self, name):
        self._name = name
        self._catalog = {}
    def get_name(self):
        return self._name
    def get_catalog(self):
        return self._catalog
    def add_movie(self, movie):
        self._catalog[movie.get_title()] = movie
    def delete_movie(self, title):
        if title in self._catalog:
            del self._catalog[title]
            return True
        else:
            return None
class StreamingGuide:
    """A class to represent a guide to streaming movies."""
    def __init__(self):
        self._streaming_services = []
    def add_streaming_service(self, service):
        self._streaming_services.append(service)
    def delete_streaming_service(self, name):
        for service in self._streaming_services:
            if service.get_name() == name:
                self._streaming_services.remove(service)
                return
    def where_to_watch(self, title):
        for service in self._streaming_services:
            catalog = service.get_catalog()
            if title in catalog:
                movie = catalog[title]
                return [f"{movie.get_title()} - ({movie.get_year()})", *service.get_name()]
        return None
