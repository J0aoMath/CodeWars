# TODO: complete this class

class PaginationHelper:
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        book_ = []
        page_ = []
        y = 0
        for z in collection:
            y += 1
            page_.append(z)
            if y % items_per_page == 0:
                book_.append(page_.copy())
                page_.clear()
        if page_ != [] and len(book_) > 0:
            book_.append(page_.copy())
        self.book_ = book_
            
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return len(self.book_)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0:
            return -1
        try:
            return len(self.book_[page_index])
        except:
            return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0:
            return -1
        i_pages = 0
        i_item = -1
        if self.items_per_page != 1:
            for z in range(0, item_index+1):
                if z % self.items_per_page == 1 and z > 1:
                    i_pages += 1
                    i_item = -1
                i_item += 1
        else:
            for z in range(0, item_index):
                    i_pages += 1
        try:
            if self.book_[i_pages][i_item] == self.book_[i_pages][i_item]:
                return i_pages
        except:
            return -1
