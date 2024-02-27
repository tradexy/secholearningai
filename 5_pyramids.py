import openai
import instructor
from pydantic import BaseModel
# from typing import List

instructor.patch()

class Pyramid(BaseModel):
    name: str
    location: str
    height: str
    builder: str

class PyramidsDetail(BaseModel):
    # standard list doesnt allow definin what type of data it contains but pydantic does
    pyramids: list[Pyramid]

# Read the text from the file
with open('pyramids.txt', 'r', encoding="utf-8") as file:
    text = file.read()

# Create a chat model
pyramids: PyramidsDetail = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    response_model=PyramidsDetail,
    messages=[
        {"role": "user", "content": text},
    ]
)
print(pyramids)

for p in pyramids.pyramids:
    print(p.name)
    print(p.location)
    print(p.height)
    print(p.builder)
    print()