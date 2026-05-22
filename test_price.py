import price_info
print("Test_price_info")

def test_total_cost_shopping():
    expected_result = 46.75
    result = price_info.total_cost_shopping()
    assert result == expected_result


def  test_total_of_fruits():
    expected = 10
    result = price_info.cost_of_fruits("apple",10)
    assert result == 12