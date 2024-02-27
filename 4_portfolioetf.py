import openai
import instructor
from pydantic import BaseModel

instructor.patch()

class PortfolioetfDetail(BaseModel):
    biggest_etf: str
    biggest_etf_aum: str
    numner_of_etfs: int
    lest_traded_etf: str
    growth_and_innovation_favourite: str
    ticket_VOO_admired_for: str

# Read the text from the file
with open('portfolioetf.txt', 'r', encoding="utf-8") as file:
    text = file.read()

# Create a chat model
portfolioetf: PortfolioetfDetail = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    response_model=PortfolioetfDetail,
    messages=[
        {"role": "user", "content": text},
    ]
)

print(portfolioetf)