def getRandom(wiki):
    pages = wiki.random()
    print(f"The random page is {list(pages.keys())[0]}")
    return list(pages.keys())[0]

def getStartPage(wiki):
    exists = False
    while not exists:
        start = input("Which page to start on (--rand for random page): ")

        if start == "--rand":
            start = getRandom(wiki)
        
        page = wiki.page(start)
        if page.exists():
            exists = True
        else:
            print("This page did not exist, please enter a valid name")
    return page

def getEndPage(wiki):
    exists = False
    while not exists:
        end = input("Which page to end on (--rand for random page): ")

        if end == "--rand":
            end = getRandom(wiki)

        page = wiki.page(end)
        if page.exists():
            exists = True
        else:
            print("This page did not exist, please enter a valid name")
    return page

def getLinks(page):
    links = page.links
    return list(links.keys())
