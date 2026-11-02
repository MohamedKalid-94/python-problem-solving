# Python Problem Solving

A structured, beginner-to-expert collection of Python problem-solving practice.
Every problem has a clean solution, pseudocode, a step-by-step explanation,
complexity analysis, and automated tests.

**Author:** Mohamed Kalid

## Why this repo

- Learn to turn logic into Python code using a repeatable routine
- Every solution is documented, tested, and easy to read
- Organized in phases, from basics to advanced patterns

## Project structure

| Folder | Purpose |
|---|---|
| `phase_0_basics/` | Solutions (one file per problem) |
| `docs/phase_0/` | Problem statement, pseudocode, how it works, complexity |
| `tests/` | Automated tests |
| `docs/how_to_solve.md` | The routine used for every problem |

## Getting started

```bash
git clone https://github.com/<your-username>/python-problem-solving.git
cd python-problem-solving
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Use a solution

```python
from phase_0_basics.is_prime import is_prime

print(is_prime(17))   # True
```

## Run the tests

```bash
python -m pytest -v
```

## Phase 0: Python basics

| # | Problem | Pattern | Docs |
|---|---|---|---|
| 001 | Sum of list | Accumulator | [docs](docs/phase_0/001_sum_of_list.md) |
| 002 | Max of list | Best so far | [docs](docs/phase_0/002_max_of_list.md) |
| 003 | Even or odd | Modulo | [docs](docs/phase_0/003_even_or_odd.md) |
| 004 | Is prime | Divisor loop | [docs](docs/phase_0/004_is_prime.md) |
| 005 | Factorial | Accumulator | [docs](docs/phase_0/005_factorial.md) |
| 006 | Fibonacci | Two variables | [docs](docs/phase_0/006_fibonacci.md) |
| 007 | Reverse string | Build a new string | [docs](docs/phase_0/007_reverse_string.md) |
| 008 | Palindrome | Compare with reverse | [docs](docs/phase_0/008_palindrome.md) |
| 009 | Count vowels | Counting with `in` | [docs](docs/phase_0/009_count_vowels.md) |
| 010 | Word frequency | Dictionary counting | [docs](docs/phase_0/010_word_frequency.md) |

## Roadmap

- [x] Phase 0: Python basics
- [ ] Phase 1: Basic logic and patterns
- [ ] Phase 2: Arrays, strings, and hashing
- [ ] Phase 3: Core patterns (two pointers, sliding window, binary search, stack)
- [ ] Phase 4: Recursion and backtracking
- [ ] Phase 5: Linked lists, trees, and heaps
- [ ] Phase 6: Graphs
- [ ] Phase 7: Dynamic programming
- [ ] Phase 8: Advanced and interview polish

## Contributing

Found a bug or a cleaner solution? Open an issue or a pull request.
Please include a test for any change.

## License

MIT. See [LICENSE](LICENSE).