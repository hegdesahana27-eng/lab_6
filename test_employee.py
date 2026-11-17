from employee import employee_details
def test_employee_details():
    result = employee_details("Rahul", "EMP101", "IT", "50000")
    assert result == expected
