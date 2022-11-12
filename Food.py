class Food:
    def __init__(self, name):
        self.name = name
        self.bio = "Default Bio"
        self.categories = set()
    
    # ---- GETTERS ----
    def get_name(self):
        return self.name
    
    def get_bio(self):
        return self.bio
    
    def get_categories(self):
        return self.categories
    
    # ---- SETTERS ----
    def set_name(self, name):
        self.name = name
    
    def set_bio(self, bio):
        self.bio = bio
    
    def set_categories(self, categories):
        self.categories = categories
    
    # ---- Other Methods ----
    def add_categories(self, categories):
        for category in categories:
            self.categories.add(category\