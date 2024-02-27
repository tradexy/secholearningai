import openai
import instructor
from pydantic import BaseModel
# from typing import List

instructor.patch()

class Portfolioetf(BaseModel):
    etf_ticker: str
    etf_name: str
    etf_aum: str
    etf_qualities: str

class PortfolioetfsDetail(BaseModel):
    # standard list doesnt allow definin what type of data it contains but pydantic does
    portfolioetfs: list[Portfolioetf]

# Read the text from the file
with open('portfolioetf.txt', 'r', encoding="utf-8") as file:
    text = file.read()

# Create a chat model
portfolioetfs: PortfolioetfsDetail = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    response_model=PortfolioetfsDetail,
    messages=[
        {"role": "user", "content": text},
    ]
)
print(portfolioetfs)

for p in portfolioetfs.portfolioetfs:
    print(p.etf_ticker)
    print(p.etf_name)
    print(p.etf_aum)
    print(p.etf_qualities)
    print()