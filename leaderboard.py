'''
This file defines the Leaderboard class.
'''
class Leaderboard:
    def __init__(self):
        self.leaderboard = []
    def add_lap_time(self, lap_time):
        self.leaderboard.append(lap_time)
    def get_leaderboard(self):
        sorted_leaderboard = sorted(self.leaderboard)
        return sorted_leaderboard