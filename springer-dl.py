import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from tqdm import tqdm
import sys

global PAGES

##########ONLY CHANGE THE LINK ######
LINK="https://link.springer.com/search?query=malware&search-within=Journal&facet-journal-id=11416"
#################
def prepareTheLink(LINK):
    result = requests.get(LINK)
    # print (result.status_code)
    c= result.content
    soup = BeautifulSoup(c,"html.parser")
    return soup

def downloadArticle(URL,Title):
    #Downloading the Article
    print("Downloading : "+Title+"...")
    response = requests.get(URL)
    with open(Title+".pdf", "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

def downloadFirstArticleOnly(soup):
    samples = soup.findAll("ol","content-item-list")
    # <h2>
    #       <a class="title" href="/article/10.1007/s11416-017-0300-z">Vigenre scores for malware detection</a>
    # </h2>
    # print (samples[0].contents[1].contents[5])

    # print (samples[0].contents[1].contents[5].contents[1].string) # Title
    title  =samples[0].contents[1].contents[5].contents[1].string

    # print (samples[0].contents[1].contents[11].contents[1].contents[1].attrs['href'])
    file = samples[0].contents[1].contents[11].contents[1].contents[1].attrs['href']

    #creating file URL
    url = "https://link.springer.com"+file

    #Downloading the Article
    downloadArticle(url,title)

def downloadAllArticles(soup):
    TotalArticles = 0
    DownloadedArticles = 0
    titles=[]
    links=[]
    #No of pages
    samples = soup.findAll("span","number-of-pages")
    NoOfPages= int(samples[0].string)
    print "No Of Search Pages:  "+str(NoOfPages)

    # No of TotalArticles
    samples = soup.findAll("h1","number-of-search-results-and-search-terms")
    TotalArticles= int(samples[0].contents[1].string)
    print "No Of Articles:      "+str(TotalArticles)

    for page in range(NoOfPages):
        result = requests.get(PAGES[page])
        # print (result.status_code)
        c= result.content
        soup = BeautifulSoup(c,"html.parser")
        samples = soup.findAll("ol","content-item-list")

        #downloading the 20 articles in page
        for i in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]:
            ## first is i=1 , 2nd is i=3 and so on
            # print (samples[0].contents[i].contents[5].contents[1].string) # Title
            title  =samples[0].contents[i].contents[5].contents[1].string
            # print (samples[0].contents[i].contents[11].contents[1].contents[1].attrs['href'])
            file = samples[0].contents[i].contents[11].contents[1].contents[1].attrs['href']

            #creating file URL
            url = "https://link.springer.com"+file

            DownloadedArticles = DownloadedArticles +1 # Congratz :P
            #Downloading the Article
            downloadArticle(url,title)
            if DownloadedArticles == TotalArticles:
                break

def generateReport(titles,links):
    df = DataFrame({'Article Title': titles ,'link':links})
    df.to_excel('SpringerArticles.xlsx', sheet_name='sheet1', index=False)


def getNoOfPages(soup):
    #No of pages
    samples = soup.findAll("span","number-of-pages")
    NoOfPages= int(samples[0].string)
    return NoOfPages


def downloadReportOnly(soup):
    TotalArticles = 0
    DownloadedArticles = 0
    titles=[]
    links=[]
    #No of pages
    samples = soup.findAll("span","number-of-pages")
    NoOfPages= int(samples[0].string)
    print "No Of Search Pages:  "+str(NoOfPages)

    # No of TotalArticles
    samples = soup.findAll("h1","number-of-search-results-and-search-terms")
    TotalArticles= int(samples[0].contents[1].string)
    print "No Of Articles:      "+str(TotalArticles)
    for page in range(NoOfPages):
        result = requests.get(PAGES[page])
        # print (result.status_code)
        c= result.content
        soup = BeautifulSoup(c,"html.parser")
        samples = soup.findAll("ol","content-item-list")

        #downloading the 20 articles in page
        for i in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]:
            ## first is i=1 , 2nd is i=3 and so on
            # print (samples[0].contents[i].contents[5].contents[1].string) # Title
            title  =samples[0].contents[i].contents[5].contents[1].string
            titles.append(title)#to export to_excel
            # print (samples[0].contents[i].contents[11].contents[1].contents[1].attrs['href'])
            file = samples[0].contents[i].contents[11].contents[1].contents[1].attrs['href']

            #creating file URL
            url = "https://link.springer.com"+file
            # print (url)
            links.append(url) #to export to_excel

            DownloadedArticles = DownloadedArticles +1 # Congratz :P

            if DownloadedArticles == TotalArticles:
                break
    generateReport(titles,links)


def downloadAllArticlesPlusReport(soup):
    TotalArticles = 0
    DownloadedArticles = 0
    titles=[]
    links=[]
    #No of pages
    samples = soup.findAll("span","number-of-pages")
    NoOfPages= int(samples[0].string)
    print "No Of Search Pages:  "+str(NoOfPages)

    # No of TotalArticles
    samples = soup.findAll("h1","number-of-search-results-and-search-terms")
    TotalArticles= int(samples[0].contents[1].string)
    print "No Of Articles:      "+str(TotalArticles)

    for page in range(NoOfPages):
        result = requests.get(PAGES[page])
        # print (result.status_code)
        c= result.content
        soup = BeautifulSoup(c,"html.parser")
        samples = soup.findAll("ol","content-item-list")

        #downloading the 20 articles in page
        for i in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]:
            ## first is i=1 , 2nd is i=3 and so on
            # print (samples[0].contents[i].contents[5].contents[1].string) # Title
            title  =samples[0].contents[i].contents[5].contents[1].string
            titles.append(title)#to export to_excel
            # print (samples[0].contents[i].contents[11].contents[1].contents[1].attrs['href'])
            file = samples[0].contents[i].contents[11].contents[1].contents[1].attrs['href']

            #creating file URL
            url = "https://link.springer.com"+file
            # print (url)
            links.append(url) #to export to_excel
            print "Article No."+str(DownloadedArticles)+"out of "+str(TotalArticles)+" .."
            DownloadedArticles = DownloadedArticles +1 # Congratz :P

            #Downloading the Article
            downloadArticle(url,title)
            if DownloadedArticles == TotalArticles:
                break
    generateReport(titles,links)

def generatePagesLinks(LINK):
    pages=[]
    # https://www.springer.com/gp/search?facet-type=type__journal&query=malware&submit=Submit+Query
    if LINK[32:38] == "/page/":#ready for searching
        i = LINK.index("search/page/")
        s0 = LINK[:i+12]
        j= LINK[i+12:].index("?")
        s1=LINK[i+j+12:]
    else:
        s0="https://link.springer.com/search/page/"
        s1=LINK[32:]
    for p in range(NoOfPages):
        pageLink = s0+str(p+1)+s1
        pages.append(pageLink)
    return pages




soup = prepareTheLink(LINK)
NoOfPages =getNoOfPages(soup)
PAGES = generatePagesLinks(LINK)
downloadAllArticlesPlusReport(soup)

