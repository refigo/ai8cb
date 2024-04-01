import os
from openai import OpenAI
import sys
from common import download, get_text_from_html, toknize_gpt2, detokenize_gpt2, split_text

MAX_TOKENS = 1024
MAX_NEW_TOKENS = 400

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
		temperature=0,
		max_tokens=max_tokens
	)
	return response.choices[0].message.content

def inference(prompt, max_tokens=MAX_NEW_TOKENS):
	return openai_inference_gpt3_5_turbo(prompt, max_tokens)

def summarize(text):
	tokenized = toknize_gpt2(text)
	split = split_text(tokenized, TOKEN_BUDGET)

	if len(split) > 1:
		summaries = []
		for i, chunk in enumerate(split):
			decoded = detokenize_gpt2(chunk)
			summaries.append(summarize(decoded))
			print(i, summaries[-1])
		summaries = " ".join(summaries)
	else:
		summaries = text
	
	prompt = PREPROMPT + summaries + POSTPROMPT
	return inference(prompt)


url = sys.argv[1]
html = download(url)
text = get_text_from_html(html)

summarized = summarize(text)
print(summarized)

# result = copywrite(summarized)

# print(result)
