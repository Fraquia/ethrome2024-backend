from openai import OpenAI
from dotenv import load_dotenv
import os
import json

api_key = os.getenv("OPENAI_API_KEY")

load_dotenv()

# Set your OpenAI API key
client = OpenAI()

def compute_word_complexity(sentence):
  prompt_sentence = f"""
  Given this sentence {sentence}, Can you express with a number between 0 and 1:
  - how much the words in the previous sentence are complex between 0 and 1
  - how much the following sentence is: self-reference, other-reference between 0 and 1.
  - how much the following sentence express: certainty, uncertainty between 0 an 1.
  - how much the following sentence refers to: present, past, future between 0 and 1
  Give me the result in json format
  """

  response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt_sentence,
    max_tokens=1024,
    temperature=0
  )

  return json.loads(response.choices[0].text)


# res = compute_word_complexity(sentence)