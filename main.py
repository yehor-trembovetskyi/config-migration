from utils import *
from lemur import LemurGraphQLClient
import lemur_client_config

if __name__ == '__main__':
    games = get_leo_admin_games()
    leo_admin_games = [game for game in games if has_proper_fileds(game)]
    graphql_config = lemur_client_config.dev_casino
    client = LemurGraphQLClient(**graphql_config)

    print(f'Client config used: {graphql_config}')
    print(f'Total games count: {len(games)}')
    print(f'Games with softwareIds count: {len(leo_admin_games)}')

    i = -1
    successful = 0
    update_failed = 0
    start_time = time.time()

    for leo_admin_game in leo_admin_games:
        i += 1
        print('\n-----------------------------------------\n')
        print(f'Start processing game #{i} (uniqueId={leo_admin_game["uniqueId"]}, name={leo_admin_game["name"]})')
        lemur_game = client.get_game(leo_admin_game['uniqueId'])

        if 'errors' in lemur_game:
            update_failed += 1

            for e in lemur_game['errors']:
                if "No game was found with id: " in e['message']:
                    p_failed({
                        'message': 'Lemur doesnt have game with id',
                        'uniqueId': leo_admin_game['uniqueId']
                    })
                    print('-- NON-EXISTING GAME CASE --')
                    continue

            p_failed({
                'unique_id': leo_admin_game['uniqueId'],
                'lemur_response': lemur_game,
                'leo_admin_game': leo_admin_game
            })
            print('-- REQUEST FAILED --')
            continue

        lemur_game = lemur_game['data']['gameInformation']

        print(f'Lemur game config: {to_json(lemur_game)}')

        lemur_game = update_game_dga_input(lemur_game, leo_admin_game)
        print(f'Updated lemur game config: {to_json(lemur_game)}')
        response = client.update_game(lemur_game)
        print(f'Lemur response: {to_json(response)}')

        if is_success(response):
            successful += 1
        else:
            update_failed += 1
            p_failed({
                'unique_id': leo_admin_game['uniqueId'],
                'lemur_response': response,
                'leo_admin_game': leo_admin_game
            })
            print('-- REQUEST FAILED --')

    print('\n-----------------------------------------\n')
    print(f"Execution time: {format_time(time.time() - start_time)}")
    print(f'Total games: {len(leo_admin_games)}')
    print(f'Successful: {successful}')
    print(f'Update failed: {update_failed}')
