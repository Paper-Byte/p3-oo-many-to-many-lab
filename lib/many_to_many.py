class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        total_royalties = 0
        for contract in self.contracts():
            total_royalties += contract.royalties
        return total_royalties


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if (not isinstance(author, Author)):
            raise TypeError("author must be of class Author")
        else:
            self.author = author
        if (not isinstance(book, Book)):
            raise TypeError("book must be of class Book")
        else:
            self.book = book
        if (not type(date) == str):
            raise TypeError("date must be of type string")
        else:
            self.date = date
        if (not type(royalties) == int):
            raise TypeError("royalties must be of type integer")
        else:
            self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda x: x.date)
