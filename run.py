from fastapi import FastAPI

app = FastAPI()

# App handlers
@app.get("/hello")
async def root():
    return {"message": "Hello"}

# Health handlers
@app.get("/healthz")
def get_heatlhz() -> dict[str, str]:
    return {"status": "UP"}
