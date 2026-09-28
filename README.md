# ArtGraph

Small Python utility that backdates Git commits in a nested repo to paint a random [GitHub contribution graph](https://github.com/YukaC/ArtGraph) pattern. Commits are appended to `random-contribuciones/README.md` according to a generated weekly intensity matrix.

**Note:** The script sets **global** Git `user.name` / `user.email` and creates or uses the `random-contribuciones/` folder. Review `main.py` before running on a machine you share with other Git work.

## Requirements

- Python 3
- Git

## Run

From the repository root:

```bash
python main.py
```

This initializes `random-contribuciones/` if missing, then creates dated commits for the last ~52 weeks. Push that folder’s remote separately if you want the graph on GitHub.

## Repository

[YukaC/ArtGraph](https://github.com/YukaC/ArtGraph)
