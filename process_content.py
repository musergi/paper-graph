import argparse
import json
from functools import reduce
from operator import add
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

def extract_features(d):
    return {
        "id": int(d["paper_id"]),
        "title": d["title"],
        "year": int(d["year"])
    }

with open(args.input) as fp:
    dicts = map(json.loads, fp.readlines())
    df = pd.DataFrame(map(extract_features, dicts))
df.to_csv(args.output)
