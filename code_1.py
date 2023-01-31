import pandas as pd
import numpy as np

df = pd.read_csv("C:\Coding\AM Dashboard\data\data_2301.csv")

collectionName = []

for x in range(len(df)):

    if df.id[x] == "B86375904A635FB3":
        collectionName.append("Mantle Warriors")
        continue

    if df.id[x] == "C984F63CDBB8BB0C":
        collectionName.append("SneakerLabz OG")
        continue

    if df.id[x] == "883C86FC2E5D21D1":
        collectionName.append("DopeSkulls")
        continue

    if df.id[x] == "BD3B7129B39506F0":
        collectionName.append("CyberAgents")
        continue

    if df.id[x] == "C395A2ECE13B3B03":
        collectionName.append("Cosmo Zombie")
        continue

    if df.id[x] == "A07FAEF74B59B7F7":
        collectionName.append("CDGS AssetMantle Metaverse Warriors")
        continue

    if df.id[x] == "803C8C529D4C79B6":
        collectionName.append("Stone Punks")
        continue

    if df.id[x] == "90059167EFA307A5":
        collectionName.append("Mantle Monkeys")
        continue

    if df.id[x] == "AF3759D04DD81F27":
        collectionName.append("How Rare Is Your Cosmos")
        continue

    if df.id[x] == "E691345678D3D476":
        collectionName.append("Squid Waves")
        continue

    if df.id[x] == "FA643042634AD34B":
        collectionName.append("Neon Corp")
        continue

    if df.id[x] == "8034E1D7A0B83DAB":
        collectionName.append("ChainOps Art")
        continue

    if df.id[x] == "D73691D95C7250CD":
        collectionName.append("Alpha Citizens")
        continue

    if df.id[x] == "D4C3FD5554AEDB64":
        collectionName.append("MintE Memoirs")
        continue

    collectionName.append("Random Collection")

df.insert(1, "collectionName", collectionName, True)

for x in range(len(df)):
    if df.collectionName[x] == "Random Collection":
        df = df.drop(x)
