from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.onrender.com",
    "https://localhost.onrender.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# r: the mobile phone user will be assigned to move right
# l: the mobile phone user will be assigned to move left
# u: the mobile phone user will be assigned to move up
# s: the mobile phone user will be assigned to shoot
actions = ["s", "u", "l", "r"]

@app.get("/actions")
def read_root():
    if len(actions) > 0:
        action = actions.pop()
    else:
        action = None

    content = {"action": action}
    headers = {"Access-Control-Allow-Origin": "https://render-pygame-backend.onrender.com", "Content-Language": "en-US"}
        
    return JSONResponse(content=content, headers=headers)
