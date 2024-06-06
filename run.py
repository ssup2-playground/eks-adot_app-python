import logging
import time

from fastapi import FastAPI

app = FastAPI()

# Ping handlers
@app.get("/ping")
async def get_ping():
    logging.info("pong")
    return {"message": "pong"}

@app.get("/pingsleep5s")
async def get_pingsleep5():
    time.sleep(5)
    logging.info("pong sleep 5s")
    return {"message": "pong sleep 5s"}

@app.get("/pingsleep10s")
async def get_pingsleep10():
    time.sleep(10)
    logging.info("pong sleep 10s")
    return {"message": "pong sleep 10s"}

# Health handlers
@app.get("/healthz")
def get_heatlhz() -> dict[str, str]:
    logging.info("healthz")
    return {"status": "up"}
