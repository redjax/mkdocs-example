"""
A simple, example test package for demonstratining mkdocstring functionality.
"""
DEFAULT_NAME: str = "human"

def say_hello(name: str = DEFAULT_NAME) -> str:
    """
    Return a simple greeting, substituting an optional name value.
    
    Params:
        name (str): 
            The name of a person/object to greet. Longer lines can be
            broken up in the code.
    """
    return f"hello, {name}"


if __name__ == "__main__":
    greeting = say_hello()
    print(greeting)