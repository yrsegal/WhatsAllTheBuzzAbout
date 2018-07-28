
import git
import os

self_path = os.path.dirname(os.path.realpath(__file__))

barry = open(os.path.join(self_path, "barry.txt"))

lines = []

line_pointer = ""

for line in barry.readlines():
    if line.isspace():
        line_pointer = line_pointer.strip()
        if not line_pointer.isspace() and line_pointer:
            lines.append(line_pointer)
        line_pointer = ""
    line_pointer += "\n" + line.lstrip("-").strip()

line_pointer = line_pointer.strip()
if not line_pointer.isspace() and line_pointer:
    lines.append(line_pointer)


repo = git.Repo(self_path)

for line in lines:
    aviation_location = os.path.join(self_path, "aviation.txt")
    with open(aviation_location, 'a') as aviation:
        aviation.write(line + "\n")
    repo.index.add([aviation_location])

    author = git.Actor("Jerry Seinfeld", "jerryseinfeld@jerryseinfeld.com")
    committer = git.Actor("Barry the Bee", "bee@busy.com")
    repo.index.commit(line, author=author, committer=committer)

