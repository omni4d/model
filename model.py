import networkx as nx
import yaml
from pathlib import Path

file = Path('omni4d.core.yaml').open('r')
model = yaml.load(file)
graph = nx.Graph()

for sign, attributes in model.items():
    graph.add_node(sign, type=attributes['type'])
    if attributes['type'] in [
        'whole_part_tuple',
        'class_member_tuple',
        'ordinary_tuple'
    ]:
        for object, details in attributes['objects'].items():
            graph.add_edge(sign, object, role=details['role'])


print(graph.nodes(data=True))
print(graph.edges(data=True))
