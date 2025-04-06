# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.book_ = []
        self.page_ = []
        y = 0
        for z in collection:
            y += 1
            self.page_.append(z)
            if y % items_per_page == 0:
                self.book_.append(self.page_)
                self.page_.clear()
        if self.page_ != self.page_.clear() and len(self.book_) > 0:
            self.book_.append(self.page_)
            
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return len(self.book_)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        try:
            return len(self.book_[page_index])
        except:
            return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        try:
            i_items = 0
            i_pages = 0
            for z in item_index:
                i_items += 1
                if i_items % self.items_per_page == 1:
                    i_pages += 1
            return self.book_[i_pages]
        except:
            return -1
