import os

class BookIngestNode:
    def __init__(self, books_dir):
        self.books_dir = books_dir
        self.books = self.load_books()

    def load_books(self):
        book_texts = []
        for fname in os.listdir(self.books_dir):
            if fname.endswith(".txt") or fname.endswith(".md"):
                with open(os.path.join(self.books_dir, fname), "r", encoding="utf-8") as f:
                    book_texts.append(f.read())
        return book_texts

    def get_knowledge(self, query):
        results = []
        for text in self.books:
            if query.lower() in text.lower():
                results.append(text)
        return results