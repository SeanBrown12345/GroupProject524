def index_files(path: str, order: list[str], unlisted: str = "remove"):
    """
    Sort and order files in a directory by renaming them with numerical prefixes 
    or custom sequence identifiers according to a user-defined order.
    
    It rearranges files in folders where ordering is crucial (reports, 
    theses, documentation, data pipelines). 
    
    This function does not modify any file content.
    
    Parameters
    ----------
    path : str
        Path to the target directory containing the files that need to be indexed.
        Can be absolute or relative path.
    order : list[str]
        List of filenames defining the desired order. Files will be renamed
        with prefixes matching their position in this list.
        Examples: ["intro.pdf", "methods.pdf", "results.pdf"]
                  ["01_introduction.py", "02_eda.py", "03_cleaning.py"]
    unlisted : str, optional, default="hide"
        How to handle files not in `order`:
        - "hide": Move to a subdirectory named "_unlisted"
        - "keep": Leave at the end with sequential numbering after ordered files
    
    Returns
    -------
    None
        Modifies the directory in place by renaming files with numerical prefixes.
    
    Raises
    ------
    FileNotFoundError
        If the specified path does not exist.
    NotADirectoryError
        If path points to a file instead of a directory.
    PermissionError
        If insufficient permissions to rename or delete files.
    ValueError
        If order list is empty or contains duplicate filenames.
    
    Examples
    --------
    **Example 1: Numerical ordering for thesis chapters**
    
    >>> # Before
    >>> # my_thesis/
    >>> #   ├── discussion.pdf
    >>> #   ├── intro.pdf
    >>> #   ├── conclusions.pdf
    >>> #   └── analysis.pdf
    
    >>> order = [
    ...     "intro.pdf",
    ...     "analysis.pdf", 
    ...     "discussion.pdf",
    ...     "conclusions.pdf"
    ... ]
    >>> index_files("my_thesis", order)
    
    >>> # After
    >>> # my_thesis/
    >>> #   ├── 01_intro.pdf
    >>> #   ├── 02_analysis.pdf
    >>> #   ├── 03_discussion.pdf
    >>> #   └── 04_conclusions.pdf
    
    **Example 2: Semantic ordering for data pipeline scripts**
    
    >>> order = [
    ...     "introduction.py",
    ...     "eda.py",
    ...     "cleaning.py",
    ...     "analysis.py",
    ...     "model.py",
    ...     "discussion.py",
    ...     "conclusion.py"
    ... ]
    >>> index_files("scripts/", order)
    
    >>> # Files renamed with semantic prefixes matching the order list
    
    Notes
    -----
    - Files are renamed with zero-padded numerical prefixes (01_, 02_, ..., 10_)
    - If a file in `order` doesn't exist in the directory, it is skipped silently
    - Duplicate filenames in `order` raise ValueError before any modifications
    - Original file extensions are always preserved
    - Hidden files (starting with .) are ignored unless explicitly listed in `order`
    
       """