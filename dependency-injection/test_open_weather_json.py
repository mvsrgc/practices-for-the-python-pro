from pathlib import Path

from open_weather_json import DataSource

import datetime

BASE_DIR = Path(__file__).resolve(strict=True).parent


def test_read():
    reader = DataSource()

    for key, value in reader.read(file_name="moscow.json").items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value
