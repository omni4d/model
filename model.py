import networkx as nx
import yaml
from pathlib import Path

tuple_types = [
    'whole_part_tuple',
    'class_member_tuple',
    'ordinary_tuple'
]

file = Path('omni4d.core.yaml').open('r')
model = yaml.load(file)
graph = nx.Graph()

for sign, attributes in model.items():
    graph.add_node(sign, type=attributes['type'])
    if attributes['type'] in tuple_types:
        for object, details in attributes['objects'].items():
            graph.add_edge(sign, object, role=details['role'])


nx.write_graphml(graph, 'omni4d.core.graphml')
