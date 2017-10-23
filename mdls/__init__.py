# mdls - Markdown list sorter

version_info = (0, 1, 0)

__version__ = VERSION = '.'.join(map(str, version_info))
__project__ = PROJECT = 'mdls'
__author__ = AUTHOR = "Park Hyunwoo <ez.amiryo@gmail.com>"


from .mdls import sort, sort_string
