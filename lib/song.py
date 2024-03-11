class Song:
    all =[]
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_all(self)
        Song.add_genre_to_Song(genre)
        Song.add_artist_to_Song(artist)
        Song.add_genre_count(genre)
        Song.add_artist_count(artist)
        Song.count +=1

    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)

    @classmethod
    def add_genre_to_Song(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_artist_to_Song(cls,artist):
        cls.artists.append(artist)

    @classmethod 
    def add_genre_count(cls, genre):

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            
    @classmethod 
    def add_artist_count(cls, artist):

        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
            



runaway = Song('Runaway', 'Kanye', 'Rap')
power = Song('Power', 'Kanye', 'R&B')
vultures = Song('Vultures', 'Kanye', 'HipHop')





