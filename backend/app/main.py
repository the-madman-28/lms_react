from fastapi import FastAPI

from app.api.routes.books import router as books_router


app = FastAPI(
    title="Library Management System API",
    version="1.0.0",
)


app.include_router(books_router)


@app.get("/")
def root():
    return {
        "message": "Library Management System API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }