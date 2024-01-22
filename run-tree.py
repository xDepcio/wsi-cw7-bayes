import numpy as np

from tree.tree import Tree


def main():
    ALGO_RUNS = 20

    total_acc = 0
    all_confs = []
    for _ in range(ALGO_RUNS):
        tree = Tree("data.csv")
        acc1 = tree.accuracy
        conf1 = tree.calculate_confusion_matrix(
            test_data=tree.test_data,
            positive_class="Ache=False",
            negative_class="Ache=True",
        )
        total_acc += acc1
        all_confs.append(conf1)

    avg_acc = total_acc / ALGO_RUNS
    avg_conf = np.mean(all_confs, axis=0)
    print(f"Accuracy: {avg_acc}, Confusion Matrix: {avg_conf}")

    TP, TN, FP, FN = avg_conf
    czulosc = TP / (TP + FN)
    swoistosc = TN / (TN + FP)
    precyzja = TP / (TP + FP)
    dokladnosc = (TP + TN) / (TP + TN + FP + FN)
    print(f"czulosc: {czulosc}")
    print(f"swoistosc: {swoistosc}")
    print(f"precyzja: {precyzja}")
    print(f"dokladnosc: {dokladnosc}")


if __name__ == "__main__":
    main()
