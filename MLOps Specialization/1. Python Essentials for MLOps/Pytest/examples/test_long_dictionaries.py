def test_log_dictionaries():
    result = {
        "key": "value",
        "lastname": "deza",
        "firstname": "alfredo"
    }

    expected = {
        "key": "value",
        "lastame": "deza",
        "firstname": "alfredo"
    }
    assert result == expected