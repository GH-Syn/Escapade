import pygame


class ItemContainer(pygame.sprite.Sprite):
    """ Item container holds the player items """

    def __init__(self, image=None):
        """
        :param image: Path to Image sprite, container added automagically
        :type image: str

        Image should be transparent as convert_alpha() is default mask.
        """

        super().__init__()

        # assumes that pygame screen is already loaded
        screen_size = pygame.display.get_surface()

        # Load the image for the inventory item
        self.image = pygame.image.load('res/ui/container.png').convert_alpha()
        if image:
            self.image_size = image.get_size()
            image = pygame.image.load(image).convert_alpha()
            self.image.blit(image, 
                            (int(self.image_size.width() / 2 - self.image.get_width() / 2),
                             int(self.image_size.height() / 2 - self.image.get_height() / 2)))

        # Set the position of the inventory item
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def draw(self, surface, x, y):
        surface.blit(self.image, (x, y))

    @classmethod
    def create_inventory(cls, num_items=5, item_width=16, item_height=16, padding=3) -> pygame.sprite.Group:
        """Creates inventory with specified number of items, width and height of the items, and padding between the items.

        :param `num_items`: The number of items to create in the inventory.
        :param `item_width`: The width of each inventory item.
        :param `item_height`: The height of each inventory item.
        :param `padding`: The amount of space to leave between each inventory item.

        Others vars:
        :`total_width`: Calculates the total width of all the inventory items, including padding.
        :`start_x`: Calculates the starting x position for the inventory items so that they are centered on the screen.
        :`item`: Creates an inventory item using the cls parameter (which is the InventoryItem class in this case), and sets its position based on the current index and the starting x position. The y position is set so that the items are centered vertically on the screen.
        :`inventory_group`: Adds each inventory item to a sprite group and returns the group.

        :returns: sprite group containing all of the inventory items.
        :rtype: `pygame.sprite.Group`
        """

        # Create a group for the inventory items
        inventory_group = pygame.sprite.Group()

        # Calculate the total width of the inventory items
        total_width = num_items * (item_width + padding)

        # Calculate the starting x position for the inventory items
        start_x = (screen_size.width - total_width) // 2

        # Create the inventory items and add them to the group
        for i in range(num_items):
            item = cls()
            item.rect.x = start_x + i * (item_width + padding)  # pyright: ignore
            item.rect.y = (screen_height - item_height) // 2    # pyright: ignore
            inventory_group.add(item)

        return inventory_group
