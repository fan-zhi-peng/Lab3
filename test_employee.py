import employee_info 
def test_get_employee_by_age_range():
    result = employee_info.get_employees_by_age_range(30,50)
    expected = [{"name" :"Chloe","age":35,"department":"Engineering","salary":70000},
                {"name" :"Mike","age":32,"department":"Engineering","salary":65000},
                {"name" :"Peter","age":40,"department":"Sales","salary":60000}]
    assert result == expected

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    expected = 60166.67
    assert result == expected

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Engineering")
    expected = [{"name" :"Chole","age":35,"department":"Engineering","salary":70000},
                {"name" :"Mike","age":32,"department":"Engineering","salary":65000}]

