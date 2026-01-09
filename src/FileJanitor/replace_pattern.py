def replace_pattern(dir: str, pattern: str, replacement: str) -> list[tuple]:
    """
    Replace specific patterns in filenames within a directory.
    
    This function iterates over all files in the specified directory and 
    renames them by substituting a target string or character with a new one. 
    This is useful for targeted batch updates, such as swapping delimiters 
    or correcting specific naming errors.
    
    The following transformations are applied:
    1. All occurrences of the input pattern within the filename root are 
       replaced by the replacement string.
    2. File extensions are preserved and excluded from the replacement logic.
    3. Directory structure remains unchanged; only the filenames are modified.
    
    Parameters
    ----------
    dir : str
        Path to the directory containing files to be modified.
    pattern : str
        The substring or character pattern to search for in filenames.
    replacement : str
        The string or character to insert in place of the found pattern.
    
    Returns
    -------
    list of tuple(Path, Path)
        A list of (old_path, new_path) pairs for each file that was renamed.
        Files whose names were unchanged are not included.

    Raises
    ------
    FileNotFoundError
        If the specified directory path does not exist.
    NotADirectoryError
        If the path points to a file instead of a directory.
    PermissionError
        If insufficient permissions to rename files in the directory.

    Examples
    --------
    >>> replace_pattern("docs/", pattern="_", replacement=" & ")
    Renames files like:
    "file_janitors.txt" -> "file & janitors.txt"
    "report_v1_final.pdf" -> "report & v1 & final.pdf"

    Notes
    -----
    - Only the filename root is modified; file extensions are always preserved
    - All occurrences of the pattern within each filename are replaced
    - Directory structure remains unchanged
    - Files without the pattern in their name are left unchanged
    - Hidden files (starting with .) are processed unless explicitly excluded
    """
    pass