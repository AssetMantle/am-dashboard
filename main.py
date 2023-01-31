import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data\data_2301.csv")

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

df = df.drop(['id', 'totalMinted', 'totalTraded', 'floorPrice', 'salePrice', 'bestOffer', 'owners',
             'uniqueOwners', 'createdBy', 'createdOnMillisEpoch', 'updatedBy', 'updatedOnMillisEpoch'], axis=1)

df2 = df.rename(columns={'collectionName': 'Collection', 'totalNFTs': 'Supply', 'totalSold': 'Sold',
                'totalVolumeTraded': 'Volume', 'listed': 'Listings', 'publicListingPrice': 'Price'})

df3 = pd.read_csv("data/data_3001.csv")

collectionName = []

for x in range(len(df3)):

    if df3.id[x] == "B86375904A635FB3":
        collectionName.append("Mantle Warriors")
        continue

    if df3.id[x] == "C984F63CDBB8BB0C":
        collectionName.append("SneakerLabz OG")
        continue

    if df3.id[x] == "883C86FC2E5D21D1":
        collectionName.append("DopeSkulls")
        continue

    if df3.id[x] == "BD3B7129B39506F0":
        collectionName.append("CyberAgents")
        continue

    if df3.id[x] == "C395A2ECE13B3B03":
        collectionName.append("Cosmo Zombie")
        continue

    if df3.id[x] == "A07FAEF74B59B7F7":
        collectionName.append("CDGS AssetMantle Metaverse Warriors")
        continue

    if df3.id[x] == "803C8C529D4C79B6":
        collectionName.append("Stone Punks")
        continue

    if df3.id[x] == "90059167EFA307A5":
        collectionName.append("Mantle Monkeys")
        continue

    if df3.id[x] == "AF3759D04DD81F27":
        collectionName.append("How Rare Is Your Cosmos")
        continue

    if df3.id[x] == "E691345678D3D476":
        collectionName.append("Squid Waves")
        continue

    if df3.id[x] == "FA643042634AD34B":
        collectionName.append("Neon Corp")
        continue

    if df3.id[x] == "8034E1D7A0B83DAB":
        collectionName.append("ChainOps Art")
        continue

    if df3.id[x] == "D73691D95C7250CD":
        collectionName.append("Alpha Citizens")
        continue

    if df3.id[x] == "D4C3FD5554AEDB64":
        collectionName.append("MintE Memoirs")
        continue

    collectionName.append("Random Collection")

df3.insert(1, "collectionName", collectionName, True)

for x in range(len(df3)):
    if df3.collectionName[x] == "Random Collection":
        df3 = df3.drop(x)

df3 = df3.drop(['id', 'totalMinted', 'totalTraded', 'floorPrice', 'salePrice', 'bestOffer', 'owners',
               'uniqueOwners', 'createdBy', 'createdOnMillisEpoch', 'updatedBy', 'updatedOnMillisEpoch'], axis=1)

totalVolume = 0
totalSales = 0
totalListings = 0

totalVolume = df3.totalVolumeTraded.sum()
totalSales = df3.totalSold.sum()
totalListings = df3.listed.sum()

df.reset_index(inplace=True, drop=True)
df3.reset_index(inplace=True, drop=True)

newSales = []

for x in range(len(df3)):
    for y in range(len(df)):
        if df.collectionName[y] == df3.collectionName[x]:
            newSales.append(df3.totalSold[x]-df.totalSold[y])

df3.insert(3, "newSales", newSales, True)

df4 = df3.rename(columns={'collectionName': 'Collection', 'totalNFTs': 'Supply', 'totalSold': 'Sold',
                 'newSales': 'New Sales', 'totalVolumeTraded': 'Volume', 'listed': 'Listings', 'publicListingPrice': 'Price'})

print(df4.to_string(index=False))
print("\nTotal MNTL Volume = " + str(totalVolume))
print("Total USD Volume = " + str(totalVolume/100))
print("Total NFTs Sold = " + str(totalSales))
print("Active Listings = " + str(totalListings))
