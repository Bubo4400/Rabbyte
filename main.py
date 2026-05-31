from sentence_transformers import SentenceTransformer
from src import compare, wiki 

import wikipediaapi
import time

model      = SentenceTransformer('all-MiniLM-L6-v2') 
email      = input("Please enter your email: ") 
wikipedia  = wikipediaapi.Wikipedia(user_agent=f"Rabbyte {email}", language='en', extract_format=wikipediaapi.ExtractFormat.HTML)
print()

startPage = wiki.getStartPage(wikipedia)
endPage   = wiki.getEndPage(wikipedia) 
print()

beforePage = None
endTitle   = endPage.title

startTime  = time.time()
viewedPages = set()

def search(page, before = None, timeLast = startTime, path = []):
    repeat = True 
    while repeat:
        if page.title == endTitle:
             return False, path

        timeSpent = time.time()
        print(f"Rabbyte spent {round(timeSpent-timeLast, 2)}sec on the last site.")
        print(f"Currently on page: {page.title} and this is page number {len(viewedPages)} that has been visited")
        viewedPages.add(page.title)

        links = wiki.getLinks(page)
        for link in links:
            for pg in viewedPages:
                if pg == link.title:
                    print(pg, link)
                    links.remove(pg)
                    break

        nbLinks = len(links)
        if nbLinks < 1:
            print("Going back a page")
            return True, path
        if nbLinks == 1:
            if links[0] not in viewedPages:
                print("Going back a page")
                return True, path
        if endTitle in links:
            return False, path + [page.title]

        winner = links[0]
        maxSim = compare.similarity(links[0], endTitle, model)
        for i in range(1, nbLinks):
            curr = compare.similarity(links[i], endTitle, model)
            if maxSim < curr and links[i] not in viewedPages:
                maxSim = curr
                winner = links[i]

        repeat, path = search(wikipedia.page(winner), before=page, timeLast=timeSpent)

    if repeat:
        print("Going back a page")
        return repeat, path
    return repeat, path + [page.title]

_, path = search(startPage)
path.remove(startPage.title)
path.reverse()

if len(path) == 0:
    print("Got Stuck ?")
else:
    print(f"\nSuccessfully found path in {len(viewedPages)} links by viewing {viewedPages} in {round(time.time()-startTime, 2)}sec")

    print(f"The path from {startPage.title} to {endTitle} is: ")
    print(f"{startPage.title} -> ", end="")
    for pg in path:
        print(f"{pg}\n{pg} -> ", end="")
    print(f"{endTitle}")
