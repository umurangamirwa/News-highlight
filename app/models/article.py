class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,author,url,description,content,urlToImage,publishedAt):
        self.id =id
        self.title = title
        self.author = author
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt= publishedAt 
        self.description = description
        self.content = content