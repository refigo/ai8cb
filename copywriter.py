import os
from openai import OpenAI
import sys
from common import download, get_text_from_html, toknize_gpt2, split_text

MAX_TOKENS = 4000
MAX_NEW_TOKENS = 100

PREPROMPT = "SUMMARIZE THE FOLLOWING DOCUMENT IN KOREAN \n=====\n"
POSTPROMPT = "\n=====\nSUMMARY:\n"

TOKEN_BUDGET = MAX_TOKENS - len(toknize_gpt2(PREPROMPT)) - len(toknize_gpt2(POSTPROMPT)) - MAX_NEW_TOKENS

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def openai_inference_gpt3_5_turbo(prompt: str, max_tokens: int = MAX_NEW_TOKENS):
	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			# {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
			{"role": "user", "content": prompt}
		],
		temperature=0.5,
		max_tokens=max_tokens
	)
	return response.choices[0].message

def inference(prompt, max_tokens=MAX_NEW_TOKENS):
	return openai_inference_gpt3_turbo(prompt, max_tokens)

def summarize(text):
	prompt = "SUMMARIZE THE FOLLOWING DOCUMENT IN KOREAN \n=====\n" + text + "\n=====\nSUMMARY:\n"
	return inference(prompt)


url = sys.argv[1]
html = download(url)
text = get_text_from_html(html)

tokenized = toknize_gpt2(text)

split = split_text(tokenized, TOKEN_BUDGET)

# result = summarize(text)

print(split)

print([len(x) for x in split])


