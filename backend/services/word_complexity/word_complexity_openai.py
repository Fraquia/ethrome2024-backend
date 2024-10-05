from openai import OpenAI
from dotenv import load_dotenv
import os
import json

api_key = os.getenv("OPENAI_API_KEY")

load_dotenv()

# Set your OpenAI API key
client = OpenAI()
# sentence = """ I can't express the gratitude we all have for this help and for all of the money raised.
#
# This page is being managed as a team of volunteers who are connected to the North Shore. We are contributing to relief efforts on the ground and also working to determine the right way to distribute these funds to everyone affected. It is our hope that we will be able to partner with a local non-profit to provide both short- and long-term relief, and will keep everyone updated as soon as we can. The GoFundMe team is also providing us with amazing support and guidance on how to move forward.
#
# We've been moved by the way the community has come together to support each other. People like Laird Hamilton and Gabby Reece have been out in their boat rescuing people and  we know we are stronger together.
#
# Your donations will help us move past this devastation, and we will remain transparent about how they are being managed. Thank you for your patience as we continue to work out logistics while also doing our part with impacted friends and neighbors. Thank you so much!
#
# Friends of ours have lost their homes. Here is some of what we are seeing in our day-to-day right now:"""


def compute_word_complexity(sentence):
  prompt_sentence = f"""
  Given this sentence {sentence}, Can you express with a number between 0 and 1:
  - how much the words in the previous sentence are complex between 0 and 1
  - how much the following sentence is: self-reference, other-reference between 0 and 1.
  - how much the following sentence express: certainty, uncertainty between 0 an 1.
  - how much the folloing sentence refers to: present, past, future between 0 and 1
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