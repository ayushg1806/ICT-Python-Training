#String Start Check Lambda
starts_with = lambda s, prefix: s.startswith(prefix)
def check_start(lst, prefix):
    return list(filter(lambda s: starts_with(s, prefix), lst))
print(check_start(['apple', 'banana', 'cherry', 'date'], 'a'))
