def flatten(source_dir: str, target_dir: str | None = None, recursive: bool = False) -> bool:
    """
    Flatten a directory by moving all files from nested subdirectories
    into a target directory. 
    
    By default, only files directly inside 'source_dir' are moved.
    If 'recursive' is True, files from all nested subdirectories
    are also moved.

    Parameters
    ----------
    source_dir : str
        Root directory containing files and nested subdirectories to flatten.
    target_dir : str, optional
        Directory where flattened files will be moved. 
        If None, the current working directory is used.
    recursive : bool, optional
        If True, flatten files from all nested subdirectories.
        If False, only flatten files directly under `source_dir`.

    Returns
    -------
    bool
        True if the operation was successful, False otherwise.

    Examples
    --------
    Flatten only top-level files:
    >>> flatten("./assignments", "./")
    True
    
    Flatten all nested files:
    >>> flatten("./images", recursive=True)
    True
    """
    pass
