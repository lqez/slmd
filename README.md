## slmd
[![Build Status](https://travis-ci.org/lqez/slmd.svg?branch=master)](https://travis-ci.org/lqez/slmd)
[![codecov](https://codecov.io/gh/lqez/slmd/branch/master/graph/badge.svg)](https://codecov.io/gh/lqez/slmd)

Sort lists in Markdown

### WHAT

Yes, it simply sorts 

```
- This
    - Gonna
    - Be
- Like
    - That
```

into

```
- Like
    - That
- This
    - Be
    - Gonna
```

P R O F I T .


### Installation

```
$ pip install slmd
```

### Usage

```
$ slmd <infile> [outfile] [-s ORDER_BY ...]

- Simply
$ slmd some.md

- To file
$ slmd src.md out.md

- Sort case-insensitive
$ slmd some.md -i

- Sort the first depth by ascending order
$ slmd some.md -s 1

- Do not sort the first depth and sort the second depth by descending order
$ slmd some.md -s 0 -1

- I'd like to shuffle the second depth only
$ slmd some.md -s 0 2

- Just shuffle all randomly
$ slmd somd.md -r

- Overwrite
$ slmd somd.md -o

- Help?
$ slmd -h
```

or use it in Python code

```
from slmd import sort_string

result = sort_string(some_markdown_string)
```


### Exit code

 - 0
     - Nothing to sort.
 - 1
     - I sorted something.


### Why do I have to use this?

I made it for managing `awesome-blahblah` list. And you can use it when you want to check list items are ordered properly.


### License

MIT (See LICENSE file)
