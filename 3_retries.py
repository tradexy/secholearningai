import instructor
import openai
from pydantic import BaseModel, field_validator

# Apply the patch to the OpenAI client
instructor.patch()

class UserDetails(BaseModel):
    name: str
    age: int

    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if v.upper() != v:
            raise ValueError("Name must be in uppercase.")
        return v

model = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    response_model=UserDetails,
    max_retries=1,
    messages=[
        {"role": "user", "content": "Extract jason is 25 years old"},
    ],
)

print(model.name)