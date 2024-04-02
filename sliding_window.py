def sliding_window(elements, window_size):
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
        yield elements[i : i + window_size]
