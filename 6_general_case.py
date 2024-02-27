import openai
import instructor
from pydantic import BaseModel
from typing import Dict, Any, Optional

instructor.patch()

class GenericDetail(BaseModel):
    data: Dict[str, Any]

with open('pyramids.txt', 'r', encoding="utf-8") as file:
    pyramids_text = file.read()

pyramids: GenericDetail = openai.ChatCompletion.create(
    model="gpt-4",
    response_model=GenericDetail,
    messages=[
        {"role": "system", "content": "Extract pharaohs from the text below:"},
        {"role": "user", "content": pyramids_text},
    ]
)
print(pyramids)
