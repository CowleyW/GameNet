import os
from subprocess import call

def git_clone(addr, name):
    if os.path.isdir(f"lib/{name}"):
        print(f"Repository {name} already exists. Skipping it.")
    else:
        call(["git", "clone", addr, f"lib/{name}"])


if __name__ == "__main__":
    git_clone("git@github.com:chriskohlhoff/asio.git", "asio")
    git_clone("git@github.com:fmtlib/fmt.git", "fmt")
