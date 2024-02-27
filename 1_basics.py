# python3 -m venv .mm                                       (for Mac)
# source .mm/bin/activate                                   (for Mac)
# python3 -m pip install -r requirements.txt                (for Mac)
# execute with: python3 basics.py                      (for Mac)
import openai
import instructor
from pydantic import BaseModel

instructor.patch()

class UserDetail(BaseModel):
    sectors: str
    country: str
    constituents: int
    model: str


user: UserDetail = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    response_model=UserDetail,
    messages=[
        {"role": "user", "content": "Their first task was constructing an index based on Greek large-cap stocks representing 40 stocks made up of diverse sectors like banking, energy production & distribution companies tourism-related businesses—the backbone industries of one proud Hellenic economy. The team meticulously analyzed each company’s fundamentals using quantitative models while considering qualitative aspects like corporate governance practices ensuring only robust firms made it into their index basket—they wanted reliable returns for investors who entrusted them with hard-earned money"},
    ]
)

print(user)