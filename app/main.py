from fastapi import FastAPI

app = FastAPI(
    title="Restaurant AI Agent API",
    description="Backend API for Restaurant AI Agent Assessment",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/")
def get_root():
    return {"message": "Restaurant AI Agent is running"}


@app.get("/health")
def get_health():
    return {"status": "healthy"}
