from fastapi import FastAPI
from Auth.authmake import Settings
from beanie import Document, Indexed, init_beanie

openapi_url = f"{Settings.API}/openapi.json"
app = FastAPI(title=Settings.PROJECT_NAME, 
              description="A simple ToDoApp", 
              version="1.0.0",
              openapi_url=openapi_url,
                
    
)

from routes.approutes import approutes

app.include_router(approutes)




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.0.104", port=8000)