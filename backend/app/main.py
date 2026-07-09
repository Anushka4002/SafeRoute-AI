from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(

    title="SafeRoute AI",

    description="Accident Risk Route Advisor",

    version="1.0"

)

app.include_router(router)