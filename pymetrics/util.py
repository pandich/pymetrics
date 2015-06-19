def coalesce(*args):
    if args:
        for arg in args:
            if arg is not None:
                return arg

    return None
