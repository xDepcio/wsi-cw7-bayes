from network import BayesNetwork


def main():
    net = BayesNetwork("network_data.json")
    net.generate_data()


main()
