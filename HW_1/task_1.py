

def calculate_discount(total: float, discount: float) -> float:
    if discount > total:
        raise ArithmeticError(f'Discount {discount} must be equal or less than total sum {total}')
    if discount == 0:
        return total
    result = total - (total / 100 * discount)
    return result


def test_calculate_discount_positive():
    assert calculate_discount(100, 80) == 20, "Calculate discount positive test failed"


def test_calculate_discount_negative():
    assert calculate_discount(100, 110) == -10, "Calculate discount negative test failed"


def test_calculate_discount_zero():
    assert calculate_discount(100, 0) == 100, "Calculate discount zero test failed"


def test_calculate_total_discount():
    assert calculate_discount(100, 100) == 0, "Calculate total discount test failed"


if __name__ == '__main__':
    test_calculate_discount_positive()
    test_calculate_discount_negative()
    test_calculate_discount_zero()
    test_calculate_total_discount()
