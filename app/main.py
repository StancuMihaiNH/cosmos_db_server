import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import (message_controller, prompt_controller,
                             tag_controller, topic_controller, user_controller)

app = FastAPI()

app.include_router(user_controller.router, prefix="/api")
app.include_router(topic_controller.router, prefix="/api")
app.include_router(message_controller.router, prefix="/api")
app.include_router(tag_controller.router, prefix="/api")
app.include_router(prompt_controller.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
