import requests

def search_player(name):
    url = f"https://overfast-api.tekrop.fr/players"
    params = {"name": name}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]["player_id"]
        else:
            print("No players found.")
    else:
        print(f"Search error: {response.status_code}")
    return None

def get_player_summary(player_id):
    url = f"https://overfast-api.tekrop.fr/players/{player_id}/summary"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Summary error: {response.status_code}")
    return None

def get_player_stats(player_id, gamemode="competitive", platform="pc"):
    url = f"https://overfast-api.tekrop.fr/players/{player_id}/stats/summary"
    params = {"gamemode": gamemode, "platform": platform}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Stats error: {response.status_code}")
    return None
