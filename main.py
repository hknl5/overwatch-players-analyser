from api import get_player_summary, get_player_stats
from report import print_full_player_report
from gpt_analysis import build_prompt, analyze_with_gpt

if __name__ == "__main__":
    player_id = input("Enter player_id (e.g., issku-2329): ").strip()

    summary = get_player_summary(player_id)
    stats = get_player_stats(player_id)

    if not summary or not stats:
        print("Failed to fetch player data.")
        exit()

    print_full_player_report(player_id)

    prompt = build_prompt(summary, stats)
    result = analyze_with_gpt(prompt)
    print("\n=== GPT ANALYSIS ===\n")
    print(result)
