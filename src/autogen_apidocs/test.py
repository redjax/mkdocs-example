"""
Another example module for the autogen_apidocs example.

This one has a class!
"""
from pathlib import Path
from dataclasses import dataclass, field

cwd = Path.cwd()

@dataclass
class SearchPath:
    """A Dataclass object representing a file or directory path.
    Defaults to the current working directory.
    
    Params:
    -------
    
    * starting_path: str A file or directory path
    """
    starting_path: Path = field(default_factory=cwd)
    
if __name__ == "__main__":
    pathobj: SearchPath = SearchPath()