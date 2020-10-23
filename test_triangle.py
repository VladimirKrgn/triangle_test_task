import triangle


def test_existing_triangle():
    t = triangle.Triangle([0, 0], [2, 5], [4, 0])
    assert t.is_exist() == True, "Should be True"


def test_non_existent_triangle():
    t = triangle.Triangle([0, 0], [3, 0], [6, 0])
    assert t.is_exist() == False, "Should be False"


def test_negative_coordinates():
    t = triangle.Triangle([-3, -7], [-72, -15], [-1, -4])
    assert t.is_exist() == True, "Should be True"


def test_mixed_coordinates():
    t = triangle.Triangle([-3, 2], [-72, -15], [0, -4])
    assert t.is_exist() == True, "Should be True"


def test_mixes_float_int_negative_positive_coordinates():
    t = triangle.Triangle([-3.2345, 2.1111], [-72.007, -15], [0.1, -4])
    assert t.is_exist() == True, "Should be True"


def test_one_point_coordinates():
    t = triangle.Triangle([0, 0], [0, 0], [0, 0])
    assert t.is_exist() == False, "Should be False"


def test_two_same_points_coordinates():
    t = triangle.Triangle([6, -6], [6, -6], [0.1, -4])
    assert t.is_exist() == False, "Should be False"
