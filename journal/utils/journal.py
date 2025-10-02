import json

from pydantic import BaseModel


class Record(BaseModel):
    id: int
    subject: str
    teacher: str
    grade: int
    date: str  # too many problems with parse


def get_records() -> list[Record]:
    with open('journal.json', 'r') as file:
        return list(map(lambda r: Record(**r), json.load(file)))


def save_record(record: Record) -> bool:
    records: list[Record] = get_records()
    records.append(record)
    with open('journal.json', 'w') as file:
        json.dump(list(map(lambda r: r.model_dump(), records)), file)
        return True


def delete_record(record: Record) -> bool:
    records: list[Record] = get_records()
    records.remove(record)
    with open('journal.json', 'w') as file:
        json.dump(list(map(lambda r: r.model_dump(), records)), file)
        return True    
