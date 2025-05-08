def lottery(collection, repetition_count):
    """
    Znajduje elementy powtarzające się dokładnie określoną liczbę razy.

    :param collection: Lista elementów do przeszukania
    :param repetition_count: Oczekiwana liczba powtórzeń
    :return: Lista elementów powtarzających się dokładnie repetition_count razy
    """
    if collection is None or repetition_count is None:
        return []

    # Zliczanie wystąpień
    occurrences = {}
    for item in collection:
        occurrences[item] = occurrences.get(item, 0) + 1

    # Wyszukiwanie elementów z dokładnie zadaną liczbą wystąpień
    result = [item for item, count in occurrences.items() if count == repetition_count]

    return result
