import xlwings as xw
import yahoo_fantasy_api as yahoo_fantasy
from src.load_config import load_config


# oauth = OAuth2(None, None, from_file="oauth2.json")
# wb = xw.Book("draft.xlsx")
# sheet1 = wb.sheets["Sheet1"]
# sheet1.range("B2").value = 45


def find_current_league_id(leagues, league_id):
    for league in leagues:
        if league.endswith(league_id):
            return league
    print("ERROR - Could not find league id for the logged in user")
    return ""


def get_current_league(config):
    game = yahoo_fantasy.Game(config["oauth"], config["game_code"])
    leagues = game.league_ids()
    actual_league_id = find_current_league_id(leagues, config["league_id"])
    return game.to_league(actual_league_id)


def write_draft_results(draft_results, config):
    wb = xw.Book("draft.xlsx")
    sheet = wb.sheets["Sheet1"]
    sheet["B1"].value = [["Foo 1", "Foo 2", "Foo 3"], [10.0, 20.0, 30.0]]
    sheet["B1"].expand().value


config = load_config("config.ini", "oauth2.json")
league = get_current_league(config)
write_draft_results(league.draft_results(), config)

print("Done")
