from utils import Record, get_records


def get_form_template(record_id: int) -> dict:
    if record_id == 0:
        return {}
    else:
        records: list[Record] = list(filter(lambda r: r.id==record_id, get_records()))
        return records[0].model_dump()