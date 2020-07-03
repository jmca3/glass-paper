import json
import sys


def process(data):
    data['format'] = 'sankey-v2'

    for link in data['links']:
        if 'data' not in link:
            link['data'] = {'value': link['value']}
            del link['value']


    if 'order' in data:
        data.setdefault('metadata', {})
        data['metadata']['layers'] = data['order']
        del data['order']

if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as f:
        data = json.load(f)

    process(data)

    with open(sys.argv[2], 'wt') as f:
        json.dump(data, f)
