import argparse
import json
from functools import reduce
from operator import add
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

def extract_inbound(d):
    return [(int(d['paper_id']), int(inbound)) for inbound in d['inbound_citations']]

def extract_outbound(d):
    return [(int(outbound), int(d['paper_id'])) for outbound in d['outbound_citations']]

with open(args.input) as fp:
    dicts = list(map(json.loads, fp.readlines()))
inbounds = reduce(add, map(extract_inbound, dicts))
outbounds = reduce(add, map(extract_outbound, dicts))
connections = set(inbounds + outbounds)
connections = map(lambda c: {'origin': c[0], 'destination': c[1]}, connections)
df = pd.DataFrame(connections)
df.to_csv(args.output)
