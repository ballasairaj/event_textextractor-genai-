import os
import json

from dotenv import load_dotenv
from mistralai import Mistral

from prompt_template import SYSTEM_PROMPT

load_dotenv()

client = Mistral(
    api_key=os.getenv("MISTRAL_API_KEY")
)


def extract_event_info(text):

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    try:
        return json.loads(result)

    except Exception:

        return {
            "event_name": "not_available",
            "event_date": "not_available",
            "event_time": "not_available",
            "event_location": "not_available",
            "organizer": "not_available"
        }