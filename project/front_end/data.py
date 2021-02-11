from django.urls import reverse

# class


class Menu:
    def __init__(self, name: str,
                 icon: str,
                 active: bool, url: str = ''):
        self.name = name
        self.icon = icon
        self.active = active
        self.url = reverse(url)

    def active_str(self) -> str:
        return 'active' if self.active else ''


# function
