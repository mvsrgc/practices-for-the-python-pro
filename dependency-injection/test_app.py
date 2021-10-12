import datetime
from pathlib import Path

from unittest.mock import MagicMock

import matplotlib.pyplot

from app import App

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Benefits of dependency injection
# 1. Methods are easier to test
# 2. Dependencies are easier to mock.
# 3. Tests don't have to change every time we extend the application.
# 4. It's easier to extend the application.
# 5. It's easier to maintain the application.


def test_read():
    hour = datetime.datetime.now().isoformat()
    temperature = 14.52
    temperature_by_hour = {hour: temperature}

    data_source = MagicMock()
    data_source.read.return_value = temperature_by_hour
    app = App(data_source, MagicMock())
    assert app.read(file_name="something.csv") == temperature_by_hour


def test_draw(monkeypatch):
    plot_mock = MagicMock()

    app = App(MagicMock(), plot_mock)

    hour = datetime.datetime.now()
    iso_hour = hour.isoformat()

    temperature = 14.52
    temperature_by_hour = {iso_hour: temperature}

    app.draw(temperature_by_hour)

    plot_mock.draw.assert_called_with([hour], [temperature])
