from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(prefix="/api", tags=["Prayer Times"])

@router.get("/prayer-times")
def get_prayer_times(city: str, country: str):
    try:
        response = requests.get(
            "https://api.aladhan.com/v1/timingsByCity",
            params={
                "city": city,
                "country": country,
                "method": 2
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Prayer service unavailable"
        )
