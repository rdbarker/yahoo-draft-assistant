import yahoo_fantasy_api as yahoo_fantasy


class Yahoo:
    def __init__(self, config):
        self.config = config
        self.draft_picks_player_ids = []
        self.league = self._get_current_league()
        self.team_details = self.league.teams()

    def _find_current_league_id(self, leagues, league_id):
        for league in leagues:
            if league.endswith(league_id):
                return league
        print("ERROR - Could not find league id for the logged in user")
        return ""

    def _get_current_league(self):
        game = yahoo_fantasy.Game(self.config.oauth, self.config.game_code)
        leagues = game.league_ids()
        actual_league_id = self._find_current_league_id(leagues, self.config.league_id)
        return game.to_league(actual_league_id)

    def update_draft_results(self):
        draft_results = self.league.draft_results()
        drafted_player_ids = []
        for pick in draft_results:
            drafted_player_ids.append(pick["player_id"])
        self.league.player_details(drafted_player_ids)
        self.draft_picks_player_ids = drafted_player_ids

    def draft_picks(self):
        self.update_draft_results()
        for pick in self.draft_picks_player_ids:
            yield self.league.player_details(pick)[0]
