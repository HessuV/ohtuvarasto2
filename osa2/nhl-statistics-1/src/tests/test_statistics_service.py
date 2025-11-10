import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Gretzky")

        self.assertIsNotNone(player)
        self.assertEqual("Gretzky", player.name)

    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Nonexistent")

        self.assertIsNone(player)

    def test_team_returns_players_of_given_team(self):
        edm_players = self.stats.team("EDM")

        self.assertEqual(3, len(edm_players))
        self.assertTrue(all(player.team == "EDM" for player in edm_players))

    def test_team_returns_empty_list_for_unknown_team(self):
        xyz_players = self.stats.team("XYZ")

        self.assertEqual(0, len(xyz_players))

    def test_top_returns_right_number_of_players(self):
        top_players = self.stats.top(3)

        self.assertEqual(3, len(top_players))

    def test_top_orders_players_by_points_descending(self):
        top_players = self.stats.top(5)
        points = [player.points for player in top_players]

        self.assertEqual(sorted(points, reverse=True), points)

    def test_top_zero_returns_empty_list(self):
        top_players = self.stats.top(0)

        self.assertEqual([], top_players)
