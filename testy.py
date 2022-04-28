# import timeit
#
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
#
# print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
#
# print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))


action = {
    "click": "left",
    "dx": 123,
    "dy": 231,
}


def test(**kwargs):
    print(kwargs['dy'])

test(**action)
