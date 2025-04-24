# Overwatch Player Performance Analyzer

Analyze Overwatch player stats like a pro using AI. This tool pulls data from the [OverFast API](https://overfast-api.tekrop.fr/) and sends it to OpenAI’s GPT for performance evaluation and coaching feedback.

---

## Features

Fetches detailed player stats (summary, general performance, hero performance)  
Generates a structured analysis 
Offers coaching insights:  
  • Strengths & Weaknesses  
  • Playstyle detection  
  • Hero suitability  
  • Personalized improvement tips

---

## 🛠️ Tech Stack

| Tool            | Purpose                     |
|-----------------|-----------------------------|
| `Python`        | Base programming language   |
| `requests`      | API communication (OverFast)|
| `openai`        | GPT-4 analysis              |
| `python-dotenv` | API key management          |

---

## Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/overwatch-analyzer.git
   cd overwatch-analyzer

## Set your API key: Create a .env file with the following content:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

## Install dependencies:
pip install -r requirements.txt

## Run the app:
python main.py

## Enter a player ID when prompted: Example:
tekrop-2217

