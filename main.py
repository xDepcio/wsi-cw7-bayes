import argparse
from ast import arg
from network import BayesNetwork


def save_to_csv(path: str, rows: list, col_names: list[str] = []) -> None:
    with open(path, "w") as f:
        if len(col_names) != 0:
            f.write(",".join(col_names) + "\n")
        for row in rows:
            f.write(",".join(row) + "\n")


def generate_csv_file(
    network_data_path: str, count: int, output: str, save_headers: bool
) -> None:
    net = BayesNetwork(network_data_path)
    data = [net.generate_data() for _ in range(count)]
    col_names = [name for name in net.nodes_sequence]
    rows = [list(map(str, row)) for row in data]
    save_to_csv(output, rows, col_names if save_headers else [])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("network_data_path", type=str)
    parser.add_argument("--count", "-c", type=int, default=100)
    parser.add_argument("--output", "-o", type=str, default="data.csv")
    parser.add_argument("--col-headers", "-ch", default=False, action="store_true")
    args = parser.parse_args()
    print(args)

    generate_csv_file(args.network_data_path, args.count, args.output, args.col_headers)


if __name__ == "__main__":
    main()
