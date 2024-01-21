import json
import random
from typing import Dict, List, Literal, TypedDict

type NetworkNodesNames = Literal["Chair", "Sport", "Ache", "Back"]
type NetworkData = List[NetworkNodeData]


class Probability(TypedDict):
    parentsValues: List[bool]
    value: float


class NetworkNodeData(TypedDict):
    name: NetworkNodesNames
    parents: List[NetworkNodesNames]
    probabilities: List[Probability]


class NetworkNode:
    name: str
    parents_names: List[NetworkNodesNames]
    probabilities: dict[tuple[bool, ...], float]

    def __init__(
        self,
        name: str,
        parents_names: List[NetworkNodesNames],
        probabilities: dict[tuple[bool, ...], float],
    ) -> None:
        self.name = name
        self.parents_names = parents_names
        self.probabilities = probabilities

    def generate_data(self, conditions: tuple[bool, ...]) -> bool:
        return self.probabilities[conditions] > random.random()


class BayesNetwork:
    node_map: Dict[NetworkNodesNames, NetworkNode]
    nodes_sequence: List[NetworkNodesNames]

    def __init__(self, network_data_path: str) -> None:
        self.node_map = {}
        self.nodes_sequence = []
        self._load_network_data(network_data_path)

    def _load_network_data(self, network_data_path: str) -> None:
        with open(network_data_path, "r") as f:
            network_data: NetworkData = json.load(f)

        for node_data in network_data:
            node_probabilites = {
                tuple(probability["parentsValues"]): probability["value"]
                for probability in node_data["probabilities"]
            }
            self.node_map[node_data["name"]] = NetworkNode(
                name=node_data["name"],
                parents_names=node_data["parents"],
                probabilities=node_probabilites,
            )
            self.nodes_sequence.append(node_data["name"])

    def generate_data(self) -> tuple[bool, ...]:
        data_results: Dict[NetworkNodesNames, bool] = {
            name: False for name in self.nodes_sequence
        }

        for node_name in self.nodes_sequence:
            node = self.node_map[node_name]

            conditions = tuple(
                [data_results[parent_name] for parent_name in node.parents_names]
            )
            generated_data = node.generate_data(conditions)
            data_results[node_name] = generated_data

        return tuple([data_results[node_name] for node_name in self.nodes_sequence])
