import fitz

class toolbox_PDF:
    def __init__(self, path):
        self.path = path
        self.doc = fitz.open(path)
        
    def count_page(self):
        return self.doc.page_count
    
    def delete_page(self, page:list, new_path):
        page_after_del = []
        for p in range(self.doc.page_count):
            if p not in page:
                page_after_del.append(p)
        self.doc.select(page_after_del)
        self.doc.save(new_path)
        self.doc.close()
        self.doc = fitz.open(self.path)
        return True
    
    def add_page(self, other_path, page:list, new_path):
        other_dec = fitz.open(other_path)
        other_dec.select(page[0:len(page)-1])
        self.doc.insert_pdf(other_dec)
        self.doc.save(new_path)
        self.doc.close()
        self.doc = fitz.open(self.path)
        return True
                
    def merge_pdf(self, other_path, new_path):
        self.doc.insert_pdf(fitz.open(other_path))
        self.doc.save(new_path)
        self.doc.close()
        self.doc = fitz.open(self.path)
        return True

    
        
    