import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Jarvis Mobile AI Backend",
    description="FastAPI Backend for Jarvis Mobile AI assistant app",
    version="1.0.0"
)

# Configure CORS so Flutter frontend can call this backend (mobile, desktop, and web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to allowed app domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
async def root_endpoint():
    return {"status": "running"}

# Register routes
app.include_router(chat_router, tags=["Chat"])
