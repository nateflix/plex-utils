import requests
import xmltodict
import os


def get_users(plex_token):
    url = 'https://plex.tv/api/users'
    params = {'X-Plex-Token': plex_token}
    response = requests.get(url, params=params)
    parsed_users = xmltodict.parse(response.text)['MediaContainer']['User']
    return parsed_users


def handler():
    # comma separated string of tokens
    plex_tokens = os.environ['PLEX_TOKENS'].split(',')

    all_emails = []
    user_count = 0
    for token in plex_tokens:
        users = get_users(token)
        server_name = users[0]['Server']['@name']
        for user in users:
            # print(f"{user['@title']} -- {user['@email']}")
            all_emails.append(user['@email'])

        print(f'{server_name} users: {len(users)}')
        user_count += len(users)

    print(f'Total Users: {user_count}\n')
    print(','.join(all_emails))


if __name__ == '__main__':
    handler()
