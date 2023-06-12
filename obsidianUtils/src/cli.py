import sys
from outline import outline_to_heading

def main() -> int:
    """ Entry point for the lib
    
    CLI interface for the obsiutil package. Features available are
    - outline conversion to heading
    
    Args:
    
    Returns:
            
    Raises
        AnyError: Default error
    
    Examples:
    
    To-do:
        - implement parser
    """
    outline_to_heading
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())