import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

def getWebPageContentBrowser(url):
    browser.open(url)
    links = browser.page.find_all("a")
    print(len(links))
    pgTitle = browser.page.find("h1", class_="firstHeading").text
    pgTitle = browser.page.title.text
    pgText = browser.page.find("div", class_="mw-body-content").text
    newPgText = [x for x in pgText.split("\n") if x != '']

    print("Title:", pgTitle)
    #for l in newPgText:
        #print(l)

    return links, url, pgTitle

def getWebPageContentRecursive(seedURL, currentLevel, maxLevel):
    url = seedURL
    while currentLevel < maxLevel:
        links, url, content = getWebPageContentBrowser(url)
        currentLevel = currentLevel + 1

        for link in links[:5]:
            #get href valueu of link
            targetURL = link['href']
            if not targetURL.startswith("#"):
                url = targetURL
                break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Matrix_(mathematics)'
    #getWebPageContentBrowser(url)
    getWebPageContentRecursive(url, 0, 2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
