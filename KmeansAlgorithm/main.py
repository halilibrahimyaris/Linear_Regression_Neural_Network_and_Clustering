import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from Point import Point


def K_means():
    points = [Point(*line.strip().split('\t')).to_tuple() for line in open("points.txt")]
    print(points)

    df = pd.DataFrame(points, columns=['X-Axis', 'Y-Axis'])
    k_means = KMeans(n_clusters=5, init='k-means++', random_state=100).fit(df)

    sns.scatterplot(data=df, x="X-Axis", y="Y-Axis", palette="dark:salmon_r", hue=k_means.labels_, legend=True)

    plt.show()


if __name__ == '__main__':
    K_means()
