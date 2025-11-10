from urllib import request
from player import Player


class PlayerReader:
    def __init__(self, url):

        self._url = url

    def get_players(self):
        
        players = []

        with request.urlopen(self._url) as players_file:
            for line in players_file:
                parts = line.decode("utf-8").strip().split(";")

                if len(parts) >= 5:
                    name = parts[0].strip()
                    team = parts[1].strip()
                    goals = int(parts[3].strip())
                    assists = int(parts[4].strip())

                    players.append(Player(name, team, goals, assists))

        return players
