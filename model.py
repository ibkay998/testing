from typing import Optional
from pydantic import BaseModel

class AssignmentSchema(BaseModel):
  slackUserName: str
  backend: bool
  age: int
  bio: str

  class Config:
    schema_extra = {
        "example": {
            "slackUsername": "ibkay998",
            "backend":True,
            "age":23,
            "bio":"Hi my name is ibukunoluwa oyeniyi and an aspiring software developer interested both in frontend and backend and I love solving problems"
    }
    }