# SPEC — ArtGraph / fake GitHub contribution graph painter

§G
Script Python pinta patrón random en contribution graph via commits backdated en repo anidado `random-contribuciones/`.

§C
- stack: Python 3 + Git CLI
- ! `main.py` setea **global** `user.name`/`user.email` — revisar antes en máquina compartida
- remote GitHub: `YukaC/ArtGraph` (local dir `patternGithubGraph`)
- ⊥ Dependabot github-actions hasta existir workflows

§I
```
cmd: python main.py → init random-contribuciones/ + commits ~52 semanas
file: main.py
file: random-contribuciones/README.md (append target)
```

§V
```
V1: commits solo dentro random-contribuciones/ (⊥ tocar otros paths del host repo)
V2: ! documentar side-effect git config global en README
```

§T
```
id|status|task|cites
T1|x|script + README warning global git config|V2
T2|.|opcional: local git config en vez de global|V2
T3|.|CI smoke (python -m py_compile) si se quiere Dependabot GHA|§C
```

§B
```
id|date|cause|fix
```
