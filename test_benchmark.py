import random
import pytest

from sorting_algorithms import insertion_sort, merge_sort


def generate_random_data(size, seed=12345):
    """
    Generuje losową listę liczb całkowitych.

    Seed zależy od rozmiaru danych, aby wyniki były powtarzalne.
    Dzięki temu dla danego rozmiaru zawsze powstaje ten sam zestaw danych.
    """
    rng = random.Random(seed + size)
    return [rng.randint(-1_000_000, 1_000_000) for _ in range(size)]


COMMON_SIZES = [10, 100, 1000, 5000, 10000, 100000]

BENCHMARK_CASES = []

for size in COMMON_SIZES:
    BENCHMARK_CASES.append(("insertion_sort", size))
    BENCHMARK_CASES.append(("merge_sort", size))


ALGORITHMS = {
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
}


@pytest.mark.parametrize("algorithm_name,size", BENCHMARK_CASES)
def test_sorting_performance(benchmark, algorithm_name, size):
    """
    Test wydajnościowy algorytmów sortowania.

    benchmark.pedantic pozwala kontrolować liczbę rund pomiarowych.
    Dla każdego przypadku sprawdzamy również poprawność wyniku,
    porównując rezultat z wbudowaną funkcją sorted().
    """
    sort_function = ALGORITHMS[algorithm_name]
    data = generate_random_data(size)

    result = benchmark.pedantic(
        sort_function,
        args=(data,),
        rounds=3,
        iterations=1
    )

    assert result == sorted(data)
