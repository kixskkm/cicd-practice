from app import calc_and_convert, temp_pipeline

def test_calc_and_convert():
    result = calc_and_convert(3, 7)
    assert round(result, 3) == 6.214

def test_temp_pipeline():
    result = temp_pipeline(100)
    assert result == 212.0