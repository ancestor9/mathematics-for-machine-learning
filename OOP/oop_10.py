# This code builds a library management system reviewing OOP concepts.
# Uses inheritance and abstraction for an Item base.
# Applies composition with a Library component.
# Implements encapsulation with private availability.
# Incorporates polymorphism with Magazine.
# Follows SOLID principles for robust design.
# The example ties together all Masterclass lessons.

from abc import ABC, abstractmethod

# 1. ABSTRACTION: The 'Item' base class cannot be instantiated.
class Item(ABC):
    def __init__(self, title, identifier):
        self.title = title
        # 2. ENCAPSULATION: Using '__' for private availability
        self.__identifier = identifier
        self._is_available = True

    @property
    def identifier(self):
        return self.__identifier

    @abstractmethod
    def get_details(self):
        """Must be implemented by subclasses."""
        pass

# 3. INHERITANCE: Book and Magazine inherit from Item
class Book(Item):
    def __init__(self, title, identifier, author):
        super().__init__(title, identifier)
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author} [{self.identifier}]"

# 4. POLYMORPHISM: Magazine implements get_details differently
class Magazine(Item):
    def __init__(self, title, identifier, issue_number):
        super().__init__(title, identifier)
        self.issue_number = issue_number

    def get_details(self):
        return f"Magazine: {self.title} - Issue #{self.issue_number} [{self.identifier}]"

# 5. COMPOSITION: The Library *has* Items (it doesn't *is* an Item)
class Library:
    def __init__(self):
        self.__catalog = []

    def add_item(self, item: Item):
        self.__catalog.append(item)

    def show_inventory(self):
        print("--- Library Inventory ---")
        for item in self.__catalog:
            # Polymorphism in action: calling the same method on different types
            print(item.get_details())

# --- Execution ---
if __name__ == "__main__":
    my_library = Library()
    
    # Adding different types of items
    my_library.add_item(Book("The Great Gatsby", "B001", "F. Scott Fitzgerald"))
    my_library.add_item(Magazine("National Geographic", "M202", 542))
    
    my_library.show_inventory()
    
    
## source = https://www.youtube.com/watch?v=M-r8pMrdfUU 