def my_range(start, end, step):
    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    elif step < 0:
        while current > end:
            yield current
            current += step
    else:
        raise ValueError


for i in my_range(1, 3, 0.5):
    print(i)