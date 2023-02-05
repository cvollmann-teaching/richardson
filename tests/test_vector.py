from src.linalg import vector


def test_add():
    data_x = [[0, 0, 0], [1] * 100]
    data_y = [[0, 1, 0], [-1] * 100]
    expected_sum = [[0, 1, 0], [0] * 100]
    for i, data in enumerate(zip(data_x, data_y, expected_sum)):
        x, y, z_exp = data
        x = vector(x)
        y = vector(y)
        z = x + y
        assert any([zi == zi_exp for zi, zi_exp in
                    zip(z, z_exp)]), "example {} incorrect".format(i)


def test_matmul():
    data_x = [[0, 0, 0], [1] * 100]
    data_y = [[0, 1, 0], [-1] * 100]
    expected_sum = [0, -100]
    for i, data in enumerate(zip(data_x, data_y, expected_sum)):
        x, y, z_exp = data
        x = vector(x)
        y = vector(y)
        assert z_exp == x @ y, "example {} incorrect".format(i)


def test_mul():
    data_x = [[1, 0, 1], [1] * 100, [1] * 100]
    data_scalar = [0, -1, -2.0]
    expected = [[0] * 3, [-1] * 100, [-2] * 100]
    for i, data in enumerate(zip(data_x, data_scalar, expected)):
        x, scalar, z_exp = data
        x = vector(x)
        # test mul
        z = x * scalar
        assert any([zi == zi_exp for zi, zi_exp in
                    zip(z, z_exp)]), "example {} incorrect".format(i)
        # test rmul
        z = scalar * x
        assert any([zi == zi_exp for zi, zi_exp in
                    zip(z, z_exp)]), "example {} incorrect".format(i)


def test_average():
    from src.linalg import average_vector
    data = [[1] * 100, [2, 4]]
    expected = [[1] * 100, [3, 3]]
    for i, data in enumerate(zip(data, expected)):
        x, z_exp = data
        x = vector(x)
        z = average_vector(x)
        assert any([zi == zi_exp for zi, zi_exp in
                    zip(z, z_exp)]), "example {} incorrect".format(i)
