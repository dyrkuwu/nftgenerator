import nftgenerator

NFTS = int(input("How many NFT's you want to generate? (int): "))

for i in range(NFTS):
    response = nftgenerator.generate_nft()
    image = response[0]
    hash = response[1]

    print(hash)
    image.save(f'output/nft{i+1}.png', 'PNG')