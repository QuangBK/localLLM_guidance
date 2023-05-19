from langchain.utilities import GoogleSerperAPIWrapper

def load_tools():
    search = GoogleSerperAPIWrapper()

    def searchGoogle(key_word):        
        res = search.run(key_word)
        # print ('key_word',key_word)
        # print ('res',res)
        return res
    
    dict_tools = {
        'Google Search': searchGoogle
    }
    return dict_tools
