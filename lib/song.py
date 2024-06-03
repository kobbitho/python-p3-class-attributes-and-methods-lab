class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self._increment_count()
        self._add_to_genres(genre)
        self._add_to_artists(artist)
        self._add_to_genre_count(genre)
        self._add_to_artist_count(artist)

    def _increment_count(self):
        Song.count += 1

    def _add_to_genres(self, genre):
        Song.genres.append(genre)

    def _add_to_artists(self, artist):
        Song.artists.append(artist)

    def _add_to_genre_count(self, genre):
        if genre in self.genre_count:
            self.genre_count[genre] += 1
        else:
            self.genre_count[genre] = 1

    def _add_to_artist_count(self, artist):
        if artist in self.artist_count:
            self.artist_count[artist] += 1
        else:
            self.artist_count[artist] = 1