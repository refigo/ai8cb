
# Use GPT2TokenizerFast to tokenize the text
def toknize_gpt2(text):
	from transformers import GPT2TokenizerFast
	tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
	return tokenizer.encode(text)

def detokenize_gpt2(tokenized):
	from transformers import GPT2TokenizerFast
	tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
	return tokenizer.decode(tokenized)

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

def split_text(tokenized, budget):
	split = []
	for i in range(0, len(tokenized), budget):
		split.append(tokenized[i:i+budget])
	
	if len(split[-1]) < budget and len(split) > 1:
		remaining_budget = budget - len(split[-1])
		split[-1] = split[-2][:remaining_budget] + split[-1]

	return split
