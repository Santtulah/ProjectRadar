from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import get_decisions

app = FastAPI(
    title="ProjectRadar API",
    description="Rajapinta Kuopion kaupungin rakennus- ja investointipäätöksiin.",
)

@app.get("/")
def health_check():
    return {"status": "API pystyssä", "message": "Tämä on ProjectRadar API, joka tarjoaa tietoa Kuopion kaupungin rakennus- ja investointipäätöksistä."}


@app.get("/decisions")
def get_decisions_endpoint(relevant_only: bool = False):
    decisions = get_decisions(relevant_only)
    return decisions
