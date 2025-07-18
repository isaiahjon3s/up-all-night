import requests
import sys

class DaftPunkSong:
    def __init__(self, title, release, date, album, length=None, artists=None):
        self.title = title
        self.release = release
        self.date = date
        self.album = album
        self.length = length  # in milliseconds
        self.artists = artists or []

    def __str__(self):
        length_str = self.format_length(self.length) if self.length else 'Unknown'
        artists_str = ', '.join(self.artists) if self.artists else 'Unknown'
        lines = [
            ("Title", self.title),
            ("Release", self.release),
            ("Date", self.date),
            ("Album", self.album),
            ("Length", length_str),
            ("Artists", artists_str)
        ]
        # Calculate max width for pretty box
        label_width = max(len(label) for label, _ in lines)
        value_width = max(len(str(value)) for _, value in lines)
        total_width = label_width + value_width + 7
        top = "┌" + "─" * (total_width - 2) + "┐"
        bottom = "└" + "─" * (total_width - 2) + "┘"
        result = [top]
        for label, value in lines:
            result.append(f"│ {label.ljust(label_width)} │ {str(value).ljust(value_width)} │")
        result.append(bottom)
        return "\n".join(result)

    @staticmethod
    def format_length(ms):
        if ms is None:
            return 'Unknown'
        seconds = int(ms // 1000)
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{str(seconds).zfill(2)}"

class DaftPunkLibrary:
    BASE_URL = "https://musicbrainz.org/ws/2/"

    @staticmethod
    def search_song(title):
        params = {
            'query': f'artist:"Daft Punk" AND recording:"{title}"',
            'fmt': 'json',
            'limit': 1
        }
        url = DaftPunkLibrary.BASE_URL + "recording/"
        response = requests.get(url, params=params, headers={"User-Agent": "DaftPunkSongInfo/1.0 ( email@example.com )"})
        if response.status_code != 200:
            print("Error fetching data from MusicBrainz.")
            return None
        data = response.json()
        if not data.get('recordings'):
            print("No song found.")
            return None
        rec = data['recordings'][0]
        title = rec.get('title', 'Unknown')
        release = rec['releases'][0]['title'] if rec.get('releases') else 'Unknown'
        date = rec['releases'][0].get('date', 'Unknown') if rec.get('releases') else 'Unknown'
        album = rec['releases'][0]['title'] if rec.get('releases') else 'Unknown'
        length = rec.get('length')
        artists = [a['artist']['name'] for a in rec.get('artist-credit', []) if 'artist' in a]
        return DaftPunkSong(title, release, date, album, length, artists)

def main():
    if len(sys.argv) < 2:
        print("Usage: python dp.py <song title>")
        sys.exit(1)
    title = " ".join(sys.argv[1:])
    song = DaftPunkLibrary.search_song(title)
    if song:
        print(song)

if __name__ == "__main__":
    main() 