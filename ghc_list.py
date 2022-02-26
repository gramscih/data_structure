class GHCList:
    def __init__(self) -> None:
        self.__node = None
        self.__next_ghc_list = None

    def is_empty(self):
        return not self.__node

    def add(self, item):
        if not self.__node:
            self.__node = item
            self.__next_ghc_list = GHCList()
        else:
            self.__next_ghc_list.add(item)

    def find(self, item):
        index = -1
        if not self.__node:
            return index
        else:
            index = self.__find(item, index)
        return index

    def __find(self, item, index):
        if self.__node == item:
            return index + 1
        else:
            return self.__next_ghc_list.__find(item, index + 1)

    def size(self):
        s = 0
        if not self.__node:
            return s
        else:
            s = self.__size(s)
        return s

    def __size(self, size):
        if self.__node:
            return size + 1
        else:
            return self.__next_ghc_list.__size(size + 1)
        
    def __getitem__(self, index):
        if index == 0:
            return self.__node
        else:
            return self.__next_ghc_list[index - 1]
    
    def __setitem__(self, index, new_value):
        if index == 0:
            self.__node = new_value
        else:
            self.__next_ghc_list[index - 1] = new_value

    def __str__(self):
        if not self.__node:
            return ""
        else:
            return "{} {}".format(self.__node, str(self.__next_ghc_list))
