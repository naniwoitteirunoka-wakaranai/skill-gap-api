import json
from pathlib import Path

DATA = Path(__file__).parent.parent / "mock" / "companies.json"


def get_companies():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def get_company(company, role):
    companies = get_companies()

    for jd in companies:
        if jd["company"] == company and jd["role"] == role:
            return jd

    return None