import configparser
import json
from pathlib import Path
from yahoo_oauth import OAuth2


def load_config(config_path, oath_json_path):
    config_parsed = configparser.ConfigParser()
    config_parsed.read(config_path)
    config = {}
    config["workbook_location"] = config_parsed["EXCEL"]["WORKBOOK_LOCATION"]
    config["sheet_name"] = config_parsed["EXCEL"]["SHEET_NAME"]
    config["league_id"] = config_parsed["YAHOO"]["LEAGUE_ID"]
    config["game_code"] = config_parsed["YAHOO"]["GAME_CODE"]
    config["refresh_rate"] = config_parsed["YAHOO"]["REFRESH_RATE"]
    config["consumer_key"] = config_parsed["SECRETS"]["CONSUMER_KEY"]
    config["consumer_secret"] = config_parsed["SECRETS"]["CONSUMER_SECRET"]
    config["oauth"] = load_key_file(
        oath_json_path, config["consumer_key"], config["consumer_secret"]
    )
    return config


def load_key_file(oath_json_path, consumer_key, consumer_secret):
    if Path(oath_json_path).is_file():
        oauth = auth_key_file(oath_json_path)
        return refresh_token(oauth)
    else:
        gen_key_file(consumer_key, consumer_secret, oath_json_path)
        oauth = auth_key_file(oath_json_path)
        return refresh_token(oauth)


def gen_key_file(consumer_key, consumer_secret, oath_json_path):
    creds = {"consumer_key": consumer_key, "consumer_secret": consumer_secret}
    with open(oath_json_path, "w") as f:
        f.write(json.dumps(creds))


def auth_key_file(oath_json_path):
    return OAuth2(None, None, from_file=oath_json_path)


def refresh_token(oauth_token):
    if not oauth_token.token_is_valid():
        oauth_token.refresh_access_token()
    return oauth_token
