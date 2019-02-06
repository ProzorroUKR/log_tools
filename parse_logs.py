#! /usr/bin/python
import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--filters", nargs='*', default="")
    parser.add_argument("--fields", nargs='*', default="")

    args = parser.parse_args()

    filters = []
    for f in args.filters:
        parts = f.split(":", 1)
        if len(parts) == 2:
            filters.append(parts)

    with open(args.file) as f:
        data = json.load(f)

    if "hits" in data:
        data = (e["_source"] for e in data["hits"]["hits"])

    data = sorted(data, key=lambda e: e["@timestamp"])

    for source in data:
        for k, v in filters:
            if k not in source or source[k] != v:
                break
        else:
            if args.fields:
                resp = " ".join(str(source.get(f)) for f in args.fields)
            else:
                resp = source

            print(resp)


if __name__ == "__main__":
    main()
