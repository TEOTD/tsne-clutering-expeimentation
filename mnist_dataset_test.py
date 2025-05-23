import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

from src.tsne import TSNE

if __name__ == "__main__":
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    X, y = mnist["data"], mnist["target"].astype(int)

    X = X / 255.0

    X_small = X[:500]
    y_small = y[:500]
    color_y = []
    colors = ["blue", "red", "orange", "yellow", "green", "black", "cyan", "pink", "grey", "purple"]
    for i in range(len(y_small)):
        temp = y_small[i]
        color_y.append(colors[temp])
    tsne = TSNE(data=X, n_components=2, perplexity=50, learning_rate=200, n_iter=20000)
    X_embedded = tsne.fit_transform(X_small, class_Y=color_y)
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y, cmap='viridis')
    plt.title("t-SNE visualization of Iris dataset")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.colorbar(scatter)
    plt.grid(True)
    plt.show()
