#!/usr/bin/env python
import sys
import json


def main():
    sys.stdout.write(json.dumps(json.loads(sys.stdin.read()), sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
