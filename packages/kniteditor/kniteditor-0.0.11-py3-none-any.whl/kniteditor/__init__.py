"""An editor for knitting projects."""

__version__ = "0.0.11"


def main(*args, **kw):
    """Open the kniteditor window."""
    from .EditorWindow import main
    main()
