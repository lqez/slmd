## mdls
[![Build Status](https://travis-ci.org/lqez/mdls.svg?branch=master)](https://travis-ci.org/lqez/mdls)
[![codecov](https://codecov.io/gh/lqez/mdls/branch/master/graph/badge.svg)](https://codecov.io/gh/lqez/mdls)

Markdown list sorter

### Installation

```
$ pip install mdls
```

### Usage

```
$ mdls <infile> [outfile] [-s ORDER_BY ...]

- If you want to sort only the first depth by ascending order,
$ mdls some.md -s 1

- If you want to sort only the second depth by descending order,
$ mdls some.md -s 0 -1

- Save the result as a file
$ mdls src.md out.md
```

### Exit code

 - 0
     - Nothing to sort.
 - 1
     - I sorted something.


### Why do I have to use this?

I made it for managing `awesome-blahblah` list. And you can use it when you want to check list items are ordered properly.

### License
MIT
