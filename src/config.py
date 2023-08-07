import configparser
import json
from pathlib import Path
from yahoo_oauth import OAuth2


class Config:
    def __init__(self, config_path, oath_json_path):
        config_parsed = configparser.ConfigParser()
        config_parsed.read(config_path)
        self.config_path = config_path
        self.oath_json_path = oath_json_path
        self.refesh_keys = config_parsed["GENERAL"]["REFRESH_KEYS"]
        self.quit_keys = config_parsed["GENERAL"]["QUIT_KEYS"]
        self.workbook_location = config_parsed["EXCEL"]["WORKBOOK_LOCATION"]
        self.sheet_name = config_parsed["EXCEL"]["SHEET_NAME"]
        self.starting_cell = config_parsed["EXCEL"]["STARTING_CELL"]
        self.league_id = config_parsed["YAHOO"]["LEAGUE_ID"]
        self.game_code = config_parsed["YAHOO"]["GAME_CODE"]
        self.consumer_key = config_parsed["SECRETS"]["CONSUMER_KEY"]
        self.consumer_secret = config_parsed["SECRETS"]["CONSUMER_SECRET"]
        self.oauth = self._load_key_file()
        self.refresh_token()

    def _load_key_file(self):
        if not Path(self.oath_json_path).is_file():
            self._gen_key_file()
        return self._auth_key_file()

    def _gen_key_file(self):
        creds = {
            "consumer_key": self.consumer_key,
            "consumer_secret": self.consumer_secret,
        }
        with open(self.oath_json_path, "w") as f:
            f.write(json.dumps(creds))

    def _auth_key_file(self):
        return OAuth2(None, None, from_file=self.oath_json_path)

    def refresh_token(self):
        if not self.oauth.token_is_valid():
            self.oauth.refresh_access_token()
        return self.oauth

    def print_config_path(self):
        print(self.config_path)
