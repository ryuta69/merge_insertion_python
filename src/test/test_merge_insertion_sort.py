from src import merge_insertion_sort as mis


def test_positive_integer() -> None:
    collection = [100, 20, 1, 99]
    assert mis.merge_insertion_sort(collection) == [1, 20, 99, 100]


def test_negative_integer() -> None:
    collection = [-100, -20, -1, -99]
    assert mis.merge_insertion_sort(collection) == [-100, -99, -20, -1]
