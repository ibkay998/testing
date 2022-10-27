from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.model import AssignmentSchema

router = APIRouter()

notes = {
    "1": {
        "slackUsername": "ibkay998",
        "backend":True,
        "age":23,
        "bio":"Hi my name is ibukunoluwa oyeniyi and an aspiring software developer interested both in frontend and backend and I love solving problems"
    
    },
    "2": {
        "slackUsername": "eze",
        "backend":False,
        "age":24,
        "bio":"Hi my name is Eze i am a an aspiring front end engineer "
    }
}


@router.get("/")
async def get_notes() -> dict:
    return {
        "data": notes
    }

@router.get("/{id}")
async def get_note(id: str) -> dict:
    if int(id) > len(notes):
        return {
            "error": "Invalid note ID"
        }

    for note in notes.keys():
        if note == id:
            return {
                "data": notes[note]
            }