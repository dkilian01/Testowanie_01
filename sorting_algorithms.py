from typing import Iterable, List, Any


def _validate_sort_input(data: Iterable[Any]) -> List[Any]:
    """
    Sprawdza, czy dane wejściowe można posortować.

    Funkcja zwraca kopię danych jako listę, aby algorytmy sortujące
    nie modyfikowały oryginalnej kolekcji przekazanej przez użytkownika.

    Args:
        data: Kolekcja elementów do posortowania.

    Returns:
        Lista elementów do dalszego sortowania.

    Raises:
        TypeError: Gdy data jest None, tekstem albo obiektem nieiterowalnym.
    """
    if data is None:
        raise TypeError("Dane wejściowe nie mogą być puste.")

    if isinstance(data, (str, bytes)):
        raise TypeError("Dane wejściowe nie mogą być tekstem ani bajtami.")

    try:
        return list(data)
    except TypeError as exc:
        raise TypeError("Dane wejściowe muszą być iterowalne.") from exc


def insertion_sort(data: Iterable[Any]) -> List[Any]:
    """
    Sortowanie przez wstawianie.

    Jest to algorytm o złożoności obliczeniowej O(n^2).
    Dobrze nadaje się do pokazania prostego algorytmu sortowania
    oraz testowania pętli i przypadków brzegowych.

    Args:
        data: Kolekcja elementów do posortowania.

    Returns:
        Nowa lista zawierająca posortowane elementy.
    """
    result = _validate_sort_input(data)

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result


def merge_sort(data: Iterable[Any]) -> List[Any]:
    """
    Sortowanie przez scalanie.

    Jest to algorytm o złożoności obliczeniowej O(n log n).
    Algorytm dzieli listę na mniejsze części, sortuje je rekurencyjnie,
    a następnie scala w jedną uporządkowaną listę.

    Args:
        data: Kolekcja elementów do posortowania.

    Returns:
        Nowa lista zawierająca posortowane elementy.
    """
    result = _validate_sort_input(data)

    if len(result) <= 1:
        return result

    middle = len(result) // 2
    left = merge_sort(result[:middle])
    right = merge_sort(result[middle:])

    return _merge(left, right)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    """
    Scala dwie posortowane listy w jedną posortowaną listę.

    Funkcja pomocnicza używana przez merge_sort.

    Args:
        left: Lewa posortowana lista.
        right: Prawa posortowana lista.

    Returns:
        Posortowana lista zawierająca elementy z left i right.
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result