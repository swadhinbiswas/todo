from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class BasicNotes(BaseModel):
    title: str
    description: str
    status: str
    created_at: str= datetime.now()
    updated_at: str= datetime.now()
    id: int
    
    
class NotesList(BaseModel):
   listofNotes: List[BasicNotes]
    