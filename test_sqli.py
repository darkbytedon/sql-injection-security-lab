
import json
from urllib.request import urlopen
from urllib.parse import urlencode

BASE_URL = "http://127.0.0.1:5001/search"


def search_user(username):
    params = urlencode({"username": username})
    url = f"{BASE_URL}?{params}"

    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


tests = [
    {
        "name": "Normal Alice search",
        "username": "alice",
        "expected_count": 1,
        "expected_user": "alice",
    },
    {
        "name": "Normal Bob search",
        "username": "bob",
        "expected_count": 1,
        "expected_user": "bob",
    },
    {
        "name": "Unknown username",
        "username": "unknown",
        "expected_count": 0,
        "expected_user": None,
    },
    {
        "name": "SQL injection attempt",
        "username": "' OR '1'='1' --",
        "expected_count": 0,
        "expected_user": None,
    },
]

passed = 0

for test in tests:
    results = search_user(test["username"])

    count_correct = len(results) == test["expected_count"]

    if test["expected_user"] is None:
        user_correct = True
    else:
        user_correct = (
            len(results) > 0
            and results[0]["username"] == test["expected_user"]
        )

    if count_correct and user_correct:
        print(f"PASS: {test['name']}")
        passed += 1
    else:
        print(f"FAIL: {test['name']}")
        print(f"Expected count: {test['expected_count']}")
        print(f"Actual results: {results}")

print(f"\nSecurity test results: {passed}/{len(tests)} passed")
