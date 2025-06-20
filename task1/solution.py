import inspect

def strict(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        annotations = func.__annotations__

        for name, value in bound_args.arguments.items():
            expected_type = annotations.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(f"Argument '{name}' must be {expected_type}, got {type(value)} instead.")

        return func(*args, **kwargs)

    return wrapper
