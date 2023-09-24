from fastapi.middleware.cors import CORSMiddleware

from app import app


# Define a list of allowed origins (in this case, only 'http://localhost:3000')
origins = [
    "http://localhost:3000",
]

# Configure CORS with the allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["*"],  # You can specify specific HTTP headers if needed
)

# Your FastAPI routes go here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)