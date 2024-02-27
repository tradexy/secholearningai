import openai
import instructor
from pydantic import BaseModel

instructor.patch()

class PyramidDetail(BaseModel):
    name: str
    location: str
    height: str
    builder: str

# Read the text from the file
with open('pyramids.txt', 'r', encoding="utf-8") as file:
    text = file.read()

# Create a chat model
pyramid: PyramidDetail = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    response_model=PyramidDetail,
    messages=[
        {"role": "user", "content": text},
    ]
)

print(pyramid)