from fastapi import FastAPI
from server.routes import router as NoteRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
  return {
    "slackUsername": "ibkay998",
    "backend":True,
    "age":23,
    "bio":"Hi my name is ibukunoluwa oyeniyi and an aspiring software developer interested both in frontend and backend and I love solving problems"
   }

app.include_router(NoteRouter, prefix="/note")