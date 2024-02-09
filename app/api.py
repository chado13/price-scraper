from datetime import datetime
from typing import Any

import requests

from app.config import config
from app.constants import FreqEnum


def get_candle_data(
    symbol: str,
    interval: FreqEnum,
    start: datetime | None = None,
    end: datetime | None = None,
    time_zone: int = 0,
    limit: int = 500,
) -> list[list[Any]]:
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start.timestamp() if start else start,
        "endTime": end.timestamp() if end else end,
        "timeZone": time_zone,
        "limit": limit,
    }
    path = f"{config.binance_base_url}/api/v3/klines"
    res = requests.get(path, params)
    return res.json()
