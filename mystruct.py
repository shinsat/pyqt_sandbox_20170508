# http://hiro-itasuto7.hatenadiary.jp/entry/2011/03/23/184607
# http://www.yoheim.net/blog.php?q=20160610

DATA = {'ID1':'10', 'ID2':'20', 'ID3':['30','100','200']}

class mine:
    def __init__(self, **info):
        self.myinfo = info
        print(self.myinfo)

        for param in info.keys():
            print('key:', param, 'value:', info[param])

a = mine(**DATA)