"""Define what a Pokemon is."""

class Pokemon:
    """Pokmon class.
    
    Has an id, a name, a height and a weight, and one or two type(s)
    """

    def __init__(self, id, name, height, weight, type1, type2=""):
        """Init all the main information about the Pokemon."""
        self.id = id
        self.name = name
        # A Pokemon can have up to 2 types, so we check it at initialization
        self.types = type1
        self.types += ("/" + type2) if type2 != "" else ""
        self.height = height
        self.weight = weight
    
    def __str__(self) -> str:
        """Used in print."""
        return (f"{self.name} is the {self.id}th Pokemon of 1st Gen.\n"
                f"It's a {self.types} Pokemon, that has a height of "
                f"{self.height}dm and a weight of {self.weight}dg.")