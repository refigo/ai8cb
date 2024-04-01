import os
from openai import OpenAI
import sys

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def openai_inference_gpt3_turbo(prompt: str, max_tokens: int = 100):
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

def inference(prompt, max_tokens=100):
	return openai_inference_gpt3_turbo(prompt, max_tokens)

# print(inference("Hi, how are you? Answer using korean: "))


def download(url):
	import requests
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
	}
	response = requests.get(url, headers=headers)
	response.encoding = 'UTF-8'
	return response

def get_text_from_html(html):
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html.text, 'html.parser')
	return soup.get_text()

# Take url from the first argument
url = sys.argv[1]

html = download(url)

text = get_text_from_html(html)

print(text)


