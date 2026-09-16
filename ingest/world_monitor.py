import requests

def fetch_world_monitor():
    url = "https://worldmonitor.io/feed.json"  # primjer feeda
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
