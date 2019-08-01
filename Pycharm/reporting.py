def download_csv(df):
    return df.to_csv("BBDD.csv")


def download_graph(graph):
    return graph.figure.savefig("BBDD.png") #Revisar