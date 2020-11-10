def my_xrange(start, stop, step = 1):
    while start < stop:
        yield start
        start += step

if __name__ == "__main__":
    for i in my_xrange(start, stop):
        print "%i" % i
