DebugMode = True

def debug(msg, params = None):
    if DebugMode is True:
        if params is None:
            print(msg)
        else:
            print("{} - {}".format(msg, params))
