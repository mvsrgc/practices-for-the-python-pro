import datetime
from pathlib import Path

from app import App

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Benefits of dependency injection
# 1. Methods are easier to test
# 2. Dependencies are easier to mock.
# 3. Tests don't have to change every time we extend the application.
# 4. It's easier to extend the application.
# 5. It's easier to maintain the application.


def test_read():
    app = App()

    for key, value in app.read(file_name=Path(BASE_DIR).joinpath("london.csv")).items():
        print(key)
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value
