# Advent of Code 2022 Python Solutions

To run the code in this directory, you need one of the following setups
below installed:

* Docker

_or_

* `pyenv`
* `direnv`
* Python 3.10.8 (`pyenv install 3.10.8`)
* `poetry`
* GNU `make` and `sed` (_not the POSIX variants that are default on
  macOS_)

Installation support is beyond the scope of this repo. Please refer to
the links for guidance.


## Running code using docker

TODO: Build, publish, then document using docker container to mount
current dir to run poetry + examples.


## Running code using local system requirements

Assuming you've already cloned this repo locally, and are in the root
directory of it:

```bash
# Get into this directory:
cd 2022/advent-of-code/python

# Enable the venv management via direnv:
direnv allow

# Build the project:
make

# Run all days:
run-all-days
```

If you are just interested in running a particular day, you can invoke
it directly via `dayXX`, like so:

```bash
day1

# ====== day01 ======
# Part 1: The elf with the most calories totals 70613.
# Part 2: The top three elves with most calories totals 205805.
```
