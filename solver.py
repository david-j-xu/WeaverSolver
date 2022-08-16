from words import words
from collections import deque
from string import ascii_lowercase


def get_path(w, parents):
    p = [w]
    while w in parents:
        p.append(parents[w])
        w = parents[w]
    return p


def solve(start: str, target: str):
    curr_words = words.copy()

    if start not in curr_words or target not in curr_words:
        raise ValueError("Starting or target word was not valid")

    if start == target:
        return [target]

    d = deque([start])
    parents = {}

    while d:
        curr = d.popleft()
        if curr not in curr_words:
            continue
        curr_words.remove(curr)
        for idx in range(4):
            for letter in ascii_lowercase:
                candidate = curr[:idx] + letter + curr[idx + 1:]
                if candidate == target:
                    parents[candidate] = curr
                    return get_path(target, parents)[::-1]
                elif candidate in curr_words and candidate not in d:
                    d.append(candidate)
                    parents[candidate] = curr

    raise ValueError("No valid path was found between the two words")


if __name__ == "__main__":
    start = input("Starting word: ")
    target = input("Target word: ")
    path = solve(start, target)
    print(f"The optimal path length is {len(path) - 1} for path {path}")
