from pymetalapi.archives import MetalArchives


if __name__ == "__main__":
    m = MetalArchives()
    for l in m.search_lyrics("inquisition"):
        print(l)
