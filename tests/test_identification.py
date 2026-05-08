

from quiz_types import identification as id


def test_convert_identification():
    dct = [
        {"term": "apple", "definition": "a red fruit"},
        {"term": "banana", "definition": "a yellow fruit"},
    ]
    quiz = [
        {"question": "a red fruit", "answer": "apple"},
        {"question": "a yellow fruit", "answer": "banana"},
    ]
    assert id.convert_identification(dct) == quiz