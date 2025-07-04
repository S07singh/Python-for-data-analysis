# Magic methods = Dunder methods (double underscores) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define ro customize the behavior of objects
'''
class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa


student1 = Student("Sudhir", 9.8)
student2 = Student("Divya", 9.6)

print(student1)
print(student1 == student2)
print(student1 > student2)
'''

class Book:
    def __init__(self, title, author, num_page):
        self.title = title
        self.author = author
        self.num_page = num_page

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_page < other.num_page

    def __gt__(self, other):
        return self.num_page > other.num_page

    def __add__(self, other):
        return f"{self.num_page + other.num_page} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, item):
        if item == 'title':
            return self.title
        elif item == 'author':
            return self.author
        elif item == 'num_page':
            return self.num_page
        else:
            return f"Key '{item}' was not found"


book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis ", 172)

# print(book1)
# print(book3)
# print(book2)

# print(book3 < book1)
# print(book1 > book3)
# print(book1 + book2)
# print(book1 == book3)
# print("Lion" in book3)
# print("Rowling" in book2)

print(book3['title'])
print(book3['author'])
print(book3['num_page'])
print(book3['audio'])