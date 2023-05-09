from game.screen_size import width, height


def assert_types_height():
    assert isinstance(height, int) == True


def assert_types_width():
    assert isinstance(width, int) == True


def assert_size_width():
    assert width <= 1920


def assert_size_height():
    assert height <= 1080
