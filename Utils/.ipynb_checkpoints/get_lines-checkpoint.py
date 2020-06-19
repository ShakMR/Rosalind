from pathlib import Path


def get_lines(filename):
    path = Path(f'Datasets/{filename}').absolute().resolve()
    with open(path) as f:
        return list(map(lambda l: l.rstrip(), f.readlines()))
