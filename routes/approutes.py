from fastapi import APIRouter, Depends, HTTPException, status
from schema import basicnoteshema

approutes = APIRouter()

from models.mainmodel import BasicNotes, NotesList

@approutes.get("/")
async def home():
    return {"message": "Hello World", "status": "success"}

@approutes.get("/notes", response_model=NotesList)
async def getNotes():
    
    
    
    return {"listofNotes": []}