import json
import time


def get_leo_admin_games():
    return json.load(open('data/games.json'))['docs']


def has_proper_fileds(game: dict):
    return 'rngSoftwareIds' in game and bool(game['rngSoftwareIds']) and 'uniqueId' in game


def has_italy_config(leo_admin_game: dict):
    return 'uniqueId' in leo_admin_game and 'aamsGameId' in leo_admin_game


def parse_adm_config(leo_admin_game: dict):
    return {
        'aamsGameId': leo_admin_game['aamsGameId'],
        'aamsGameType': leo_admin_game['regulatoryGameType'],
        'aamsBonusEnabled': leo_admin_game.get('bonusEnabled', False),
        'aamsJackpotEnabled': leo_admin_game.get('jackpotEnabled', False),
        'aamsAdditionalJackpotEnabled': leo_admin_game.get('additionalJackpotEnabled', False)
    }


def update_game(lemur_game: dict, leo_admin_game: dict):
    if lemur_game['game']['regulatoryGame'] is None:
        lemur_game['game']['regulatoryGame'] = {}
    lemur_game['game']['regulatoryGame']['adm'] = parse_adm_config(leo_admin_game)
    # Normalize input
    lemur_game['game']['liveInDK'] = lemur_game['game'].pop('liveInDk') or False
    return lemur_game


def parse_dga_config(leo_admin_game: dict):
    rng_software_ids_ = leo_admin_game['rngSoftwareIds'][0]
    return {
        'softwareId': rng_software_ids_['softwareId'],
        'rngId': rng_software_ids_['rngId']
    }


def update_game_dga_input(lemur_game: dict, leo_admin_game: dict):
    if lemur_game['game']['regulatoryGame'] is None:
        lemur_game['game']['regulatoryGame'] = {}
    lemur_game['game']['regulatoryGame']['dga'] = parse_dga_config(leo_admin_game)
    # Normalize input
    lemur_game['game']['liveInDK'] = lemur_game['game'].pop('liveInDk') or False
    return lemur_game

def to_json(game: dict):
    return json.dumps(game)


def is_success(response: dict) -> bool:
    try:
        return response['data']['game']['id'] is not None
    except Exception:
        return False


def format_time(seconds: float) -> str:
    return time.strftime('%H:%M:%S', time.gmtime(int(seconds)))


def p_failed(failed):
    f = open("reports/failed.txt", "a")
    f.write(f'{str(to_json(failed))}\n')
    f.close()
