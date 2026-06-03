import sys, os
from openai import OpenAI

def analyze_log(log_file):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    with open(log_file) as f:
        content = f.read()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a DevOps AI agent. Detect failures in Jenkins pipeline logs and explain root cause clearly with actionable suggestions."},
            {"role": "user", "content": content}
        ],
        max_tokens=500
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    analyze_log(sys.argv[1])
