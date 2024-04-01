import os
from openai import OpenAI

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

print(inference("Hi, how are you? Answer using korean: "))
