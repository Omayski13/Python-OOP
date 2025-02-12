from project.song import Song

class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot add songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published =True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f"Album {self.name}\n"]
        for song in self.songs:
            info.append(f"== {song.get_info()}\n")
        return "".join(info)


