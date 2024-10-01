import requests

from fastapi import FastAPI

from custom_types import EV_API_Data, EV_Make_Metadata
from utils import get_make_details



app = FastAPI()

WASHINGTON_EV_BASE_API = "https://data.wa.gov/resource/f6w7-q2d2.json"


@app.get("/ev/{year}")
async def get_ev_data(year: int) -> list[EV_Make_Metadata]:
    # TODO sanitize the year parameter

    MODEL_YEAR_PARAM = "?model_year="

    response = requests.get(WASHINGTON_EV_BASE_API + MODEL_YEAR_PARAM + str(year), timeout=10)
    data = response.json()

    cars = [EV_API_Data(**item) for item in data]
    return get_make_details(cars)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    