import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(summary, stats):
    general = stats.get("general", {})
    avg = general.get("average", {})
    total = general.get("total", {})
    heroes = stats.get("heroes", {})

    prompt = f"""You are a coach analyzing the performance of an Overwatch player using raw data.

Here’s the player summary and stats:
Username: {summary.get("username")}
Title: {summary.get("title")}
Endorsement Level: {summary.get("endorsement", {}).get("level", "N/A")}
Last Updated: {summary.get("last_updated_at")}

General Total Stats:
Games Played: {general.get("games_played")}
Wins: {general.get("games_won")}
Losses: {general.get("games_lost")}
Winrate: {general.get("winrate")}%
KDA: {general.get("kda")}
Time Played: {general.get("time_played")}
Eliminations: {total.get("eliminations")}
Deaths: {total.get("deaths")}
Assists: {total.get("assists")}
Damage: {total.get("damage")}
Healing: {total.get("healing")}

General Averages Per Game:
Avg Eliminations: {avg.get("eliminations")}
Avg Deaths: {avg.get("deaths")}
Avg Assists: {avg.get("assists")}
Avg Damage: {avg.get("damage")}
Avg Healing: {avg.get("healing")}

Hero Performance:
"""
    for hero, data in heroes.items():
        avg = data.get("average", {})
        prompt += f"{hero.title()}:\n"
        prompt += f"Games Played: {data.get('games_played', 0)}, Wins: {data.get('games_won', 0)}, KDA: {data.get('kda', 0)}\n"
        prompt += f"Avg Damage: {avg.get('damage', 0)}, Avg Healing: {avg.get('healing', 0)}, Avg Assists: {avg.get('assists', 0)}, Time Played: {data.get('time_played', 0)}s\n\n"

    prompt += """Instructions:
Give a structured analysis of the player's overall performance including:
- Strengths and weaknesses
- Style of play
- Most suitable roles and heroes
- Training advice to improve winrate
- Any notable insights or patterns
"""
    return prompt

def analyze_with_gpt(prompt):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content
