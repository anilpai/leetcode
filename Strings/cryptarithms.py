from itertools import product
from multiprocessing import Pool, cpu_count

sequence = "123456789"

manipulations = "+-"
worker_count = cpu_count()


def slice_string(slice_tuple):
    """if slice_tuple == (2, 3, 4) return [12, 345, 6789] """

    final = []
    start = end = 0

    for slice in slice_tuple:
        end = slice + end
        final.append(sequence[start:end])
        start = end
    return final


def validate_slices(slice_dividers):
    """Convert slice_dividers items to int and skip invalid combinations."""

    slice_sum = 0
    int_slice_dividers = []

    for slice in slice_dividers:
        slice = int(slice)
        slice_sum += slice

        if slice_sum > 9:
            return False

        int_slice_dividers.append(slice)

    if slice_sum != 9:
        return False

    return int_slice_dividers


def run(slice_dividers):
    slice_dividers = validate_slices(slice_dividers)
    if not slice_dividers:
        return

    sliced = slice_string(slice_dividers)
    template = " %s ".join(sliced)

    for operations in product(manipulations, repeat=len(sliced) - 1):
        equation = template % operations
        equation_result = eval(equation)

        if equation_result == 100:
            print "%s = %s" % (equation, equation_result)


if __name__ == "__main__":

    pool = Pool(worker_count)

    for slice_count in (2, 3, 4, 5, 6, 7, 8):
        pool.map(run, product("12345678", repeat=slice_count), 1000)
