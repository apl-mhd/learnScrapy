urls = [
    'https://www.goodreads.com/quotes?page=1',
    'http://quotes.toscrape.com/page/2',
    'https://www.goodreads.com/quotes?page=2',
]



def createGent():


    for i in  range(3):

        yield i*i



def cal(a,b,c):


    return c(a,b)




def add(a,b):
    return  a+b






print(cal(10,20,add))
