import openai
import instructor
from pydantic import BaseModel
from typing import Dict, Any, Optional

instructor.patch()

class GenericDetail(BaseModel):
    data: Dict[str, Any]

with open('portfolioetf.txt', 'r', encoding="utf-8") as file:
    portfolioetfs_text = file.read()

portfolioetfs: GenericDetail = openai.ChatCompletion.create(
    model="gpt-4",
    response_model=GenericDetail,
    messages=[
        {"role": "system", "content": "Extract interesting facts from the text below:"},
        {"role": "user", "content": portfolioetfs_text},
    ]
)
print(portfolioetfs)
