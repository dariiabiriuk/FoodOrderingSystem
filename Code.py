from datetime import datetime

class MenuItem:
    """
    Class MenuItem is designed to represent an individual item or dish on a menu, responsible for both storing
    and validating its detailed attributes.

    Within the MenuItem class, the parameters are internal variables that store the values
    of a specific dish. These are defined in the __init__ constructor.
    """
    def __init__(self, name: str, description: str, price: float, calories: int, weight_gram: float,
                 allergens: list, is_available: bool, preparation_time_minutes: int):
        """
        The __init__ method initializes a dish object, checking the validity
        of the input values for the name, description, price, calories,
        weight in grams, allergens, availability, and cooking time in minutes.

        :param name: the name of the dish. Must be a non-empty string.
        :param description: a detailed description of the dish. Must be a non-empty string.
        :param price: the price of the dish. Must be a positive float.
        :param calories: the caloric content of the dish. Must be a positive integer.
        :param weight_gram: the weight of the dish in grams. Must be a positive float.
        :param allergens: a list of allergens present in the dish. Must be a non-empty list.
        :param is_available: a boolean indicating if the dish is currently available. Must be True if available.
        :param preparation_time_minutes: the estimated preparation time in minutes. Must be a positive integer.
        :raises TypeError: if any parameter is not of the expected type.
        :raises ValueError: if any parameter fails validation (for example empty string, non-positive number, empty list).
        """
        if not isinstance(name, str):
            raise TypeError("The dish name cannot be non-string.")
        if not isinstance(description, str):
            raise TypeError("The dish description must be a string.")
        if not description:
            raise ValueError("The description name cannot be empty.")
        if not isinstance(price, float):
            raise TypeError("The dish price must be of type float.")
        if price <= 0:
            raise ValueError("The price of the dish needs to be a positive value.")
        if not isinstance(calories, int):
            raise TypeError("Calories must be a type integer.")
        if calories <= 0:
            raise ValueError("Calories must be a positive integer.")
        if not isinstance(weight_gram, float):
            raise TypeError("Weight must be a type float.")
        if weight_gram <= 0:
            raise ValueError("Weight must be a positive number in grams.")
        if not isinstance(allergens, list):
            raise TypeError("Allergens must be provided as a list.")
        if not allergens:
            raise ValueError("Allergens list cannot be empty.")
        if not isinstance(is_available, bool):
            raise TypeError("Availability must be a boolean value.")
        if not is_available:
            raise ValueError("Availability cannot be empty.")
        if not isinstance(preparation_time_minutes, int):
            raise TypeError("Preparation time must be an integer.")
        if preparation_time_minutes <= 0:
            raise ValueError("Preparation time must be a positive integer.")
        self._name = name
        self._description = description
        self._price = price
        self._calories = calories
        self._weight_gram = weight_gram
        self._allergens = allergens
        self._is_available = is_available
        self._preparation_time_minutes = preparation_time_minutes

    def get_name(self) -> str:
        """
        Retrieves the name of the menu item.

        :return: the name of the dish as a string.
        :rtype: str
        """
        return self._name
    def get_description(self) -> str:
        """
        Retrieves the detailed description of the menu item.

        :return: the description of the dish as a string.
        :rtype: str
        """
        return self._description
    def get_price(self) -> float:
        """
        Retrieves the price of the menu item.

        :return: the price of the dish as a float.
        :rtype: float
        """
        return self._price
    def get_calories(self) -> int:
        """
        Retrieves the caloric content of the menu item.

        :return: the calories of the dish as an integer.
        :rtype: int
        """
        return self._calories
    def get_weight_gram(self) -> float:
        """
        Retrieves the weight of the menu item in grams.

        :return: the weight of the dish in grams as a float.
        :rtype: float
        """
        return self._weight_gram
    def get_allergens(self) -> list:
        """
        Retrieves the list of allergens present in the menu item.

        :return: a list of allergens as strings.
        :rtype: list
        """
        return self._allergens
    def get_is_available(self) -> bool:
        """
        Checks the current availability status of the menu item.

        :return: true if the dish is available, False otherwise.
        :rtype: bool
        """
        return self._is_available
    def get_preparation_time_minutes(self) -> int:
        """
        Retrieves the estimated preparation time for the menu item in minutes.

        :return: the preparation time in minutes as an integer.
        :rtype: int
        """
        return self._preparation_time_minutes

    def __str__(self):
        """
        Returns a string representation of the MenuItem object, including all its key attributes
        in a readable and formatted manner.

        This method allows for easy output of dish information, for example, for printing a menu
        or for logging purposes.

        :return: a formatted string representation of the MenuItem object.
        :rtype: str
        """
        availability_status = "Available" if self._is_available else "Not Available"
        return (f"Dish Name: {self._name}\n"
                f"Description: {self._description}\n"
                f"Price: ${self._price:.2f}\n"
                f"Calories: {self._calories} kcal\n"
                f"Weight: {self._weight_gram:.2f} grams\n"
                f"Allergens: {', '.join(self._allergens)}\n"
                f"Availability: {availability_status}\n"
                f"Preparation time: {self._preparation_time_minutes} minutes")

class Menu:
    """
    This class represents a restaurant's menu, holding a collection of menu items (dishes).

    It allows for the creation, management, and display of the dishes available on a specific menu.
    It provides functionality for adding, removing, and searching for individual menu items.
    """
    def __init__(self, name: str):
        """
        Initializes a new Menu object.

        Sets the name of the menu and creates an empty list to store MenuItem objects.

        :param name: the name of the menu (for example, "Breakfasts", "Lunch Menu").
        :type name: str
        :raises TypeError: if name is not a string.
        :raises ValueError: if name is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError("Menu name must be a string.")
        if not name:
            raise ValueError("Menu name cannot be empty.")
        self._name = name
        self._items: list[MenuItem] = []

    def get_name(self) -> str:
        """
        Retrieves the name of the menu.

        :return: the name of the menu as a string.
        :rtype: str
        """
        return self._name

    def add_item(self, item: MenuItem):
        """
        Adds a MenuItem object to the menu.

        This method appends the provided MenuItem to the internal list of items.
        It ensures that only valid MenuItem objects can be added.

        :param item: the MenuItem object to be added to the menu.
        :type item: MenuItem
        :raises TypeError: if the provided item is not an instance of MenuItem.
        """
        if not isinstance(item, MenuItem):
            raise TypeError("Can only add MenuItem objects to the menu.")
        self._items.append(item)

    def remove_item(self, item_name: str):
        """
        Removes a MenuItem from the menu by its name.

        This method iterates through the current list of menu items and
        creates a new list excluding the item with the matching name.
        If multiple items have the same name, all will be removed.

        :param item_name: the name of the menu item to be removed.
        :type item_name: str
        """
        new_items_list = []
        for item in self._items:
            if item.get_name() != item_name:
                new_items_list.append(item)
        self._items = new_items_list

    def get_item(self, item_name: str) -> MenuItem | None:
        """
        Retrieves a MenuItem from the menu by its name.

        This method searches for an item with the specified name within the menu.
        It returns the first matching MenuItem object found.

        :param item_name: the name of the menu item to retrieve.
        :type item_name: str
        :return: the MenuItem object if found, otherwise None.
        :rtype: MenuItem | None
        """
        for item in self._items:
            if item.get_name() == item_name:
                return item
        return None

    def display_menu(self):
        """
        Prints a formatted display of the entire menu to the console.

        This method first prints the menu's name, then lists all the items it contains.
        If the menu is empty, it indicates that no items are available.
        Each item's details are displayed using its __str__ method.
        """
        print(f"{self.get_name()} Menu")
        if not self._items:
            print("No items in this menu yet.")
        for item in self._items:
            print(item)

class Restaurant:
    """
    Represents a restaurant with its core details and manages its menu.
    """
    def __init__(self, name: str, address: str, phone: int, opening_hours: dict,
                 cuisine_type: str, rating: float):
        """
        Initializes a new Restaurant object with comprehensive details.

        This method validates all input parameters to ensure data integrity
        for the restaurant's information.

        :param name: the name of the restaurant. Must be a non-empty string.
        :param address: the physical address of the restaurant. Must be a non-empty string.
        :param phone: the contact phone number of the restaurant. Must be a positive integer.
        :param opening_hours: a dictionary specifying the restaurant's opening hours
        (for example, 'Monday': '9:00-22:00', 'Weekend': '10:00-23:00'). Must be a non-empty dictionary.
        :param cuisine_type: the type of cuisine the restaurant specializes in (for example, "Italian", "Japanese").
        Must be a non-empty string.
        param rating: the average customer rating of the restaurant on a scale of 0 to 5.
        Must be a float between 0 and 5 (inclusive).
        :raises TypeError: if any parameter is not of the expected type.
        :raises ValueError: if any parameter fails validation (e.g., empty string, non-positive phone, empty dict,
        rating out of range).
        """
        if not isinstance(name, str):
            raise TypeError("Restaurant name must be a string.")
        if not name:
            raise ValueError("Restaurant name cannot be empty.")
        if not isinstance(address, str):
            raise TypeError("Restaurant address must be a string.")
        if not address:
            raise ValueError("Restaurant address cannot be empty.")
        if not isinstance(phone, int):
            raise TypeError("Restaurant phone must be a integer.")
        if phone <= 0:
            raise ValueError("Restaurant phone must be a positive integer.")
        if not isinstance(opening_hours, dict):
            raise TypeError("Restaurant opening_hours must be a dict.")
        if not opening_hours:
            raise ValueError("Restaurant opening_hours cannot be empty.")
        if not isinstance(cuisine_type, str):
            raise TypeError("Restaurant cuisine_type must be a string.")
        if not cuisine_type:
            raise ValueError("Restaurant cuisine_type cannot be empty.")
        if not isinstance(rating, float):
            raise TypeError("Restaurant rating must be a float.")
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5.")
        self._name = name
        self._address = address
        self._phone = phone
        self._opening_hours = opening_hours
        self._cuisine_type = cuisine_type
        self._rating = rating
        self._menu: Menu | None = None

    def get_name(self) -> str:
        """
        Retrieves the name of the restaurant.

        :return: the name of the restaurant as a string.
        :rtype: str
        """
        return self._name
    def get_address(self) -> str:
        """
        Retrieves the address of the restaurant.

        :return: the address of the restaurant as a string.
        :rtype: str
        """
        return self._address
    def get_phone(self) -> int:
        """
        Retrieves the phone number of the restaurant.

        :return: the phone number of the restaurant as an integer.
        :rtype: int
        """
        return self._phone
    def get_opening_hours(self) -> dict:
        """
        Retrieves the opening hours of the restaurant.

        :return: a dictionary representing the restaurant's opening hours.
        :rtype: dict
        """
        return self._opening_hours
    def get_cuisine_type(self) -> str:
        """
        Retrieves the cuisine type of the restaurant.

        :return: the cuisine type of the restaurant as a string.
        :rtype: str
        """
        return self._cuisine_type
    def get_rating(self) -> float:
        """
        Retrieves the average rating of the restaurant.

        :return: the rating of the restaurant as a float (between 0 and 5).
        :rtype: float
        """
        return self._rating
    def get_menu(self) -> Menu | None:
        """
        Retrieves the current menu assigned to the restaurant.

        :return: the Menu object assigned to the restaurant, or None if no menu is set.
        :rtype: Menu | None
        """
        return self._menu

    def set_menu(self, menu: Menu):
        """
        Assigns a Menu object to the restaurant.

        This method links a specific menu to the restaurant, allowing it to offer
        those menu items. It validates that the provided object is indeed a Menu instance.

        :param menu: the Menu object to be assigned to the restaurant.
        :type menu: Menu
        :raises TypeError: if the provided 'menu' is not an instance of the Menu class.
        """
        if not isinstance(menu, Menu):
            raise TypeError("Menu must be an instance of the Menu class.")
        self._menu = menu
        print(f"Menu '{menu.get_name()}' has been set for {self.get_name()}.")

    def __str__(self):
        """
        Returns a human-readable string representation of the Restaurant object.

        This representation includes the restaurant's name, address, phone number,
        cuisine type, opening hours, rating, and the name of its currently assigned menu.

        :return: a formatted string detailing the restaurant's information.
        :rtype: str
        """
        menu_status = self._menu.get_name() if self._menu else "No menu set"
        return (f"Restaurant Name: {self._name}\n"
                f"Address: {self._address}\n"
                f"Phone: {self._phone}\n"
                f"Cuisine: {self._cuisine_type}\n"
                f"Opening hours: {self._opening_hours}\n"
                f"Rating: {self._rating}/5 stars\n"
                f"Current menu: {menu_status}")

class Client:
    """
    Represents a client of the restaurant, storing their personal and contact information.
    """
    def __init__(self, name: str, surname: str,  email: str, phone: str):
        """
        Initializes a new Client object.

        This method validates the name, surname, email, and phone number
        to ensure all contact details are valid and present.

        :param name: the first name of the client. Must be a non-empty string.
        :param surname: the last name (surname) of the client. Must be a non-empty string.
        :param email: the email address of the client. Must be a non-empty string and contain '@'.
        :param phone: the phone number of the client. Must be a non-empty string.
        :raises TypeError: if any parameter is not of the expected string type.
        :raises ValueError: if 'name', 'surname', 'email', or 'phone' are empty,
        or if 'email' does not contain '@'.
        """
        if not isinstance(name, str):
            raise TypeError("Client name must be a string.")
        if not name:
            raise ValueError("Client name cannot be empty.")
        if not isinstance(surname, str):
            raise TypeError("Client surname must be a string.")
        if not surname:
            raise ValueError("Client surname cannot be empty.")
        if not isinstance(email, str):
            raise TypeError("Client email must be a string.")
        if not email or "@" not in email:
            raise ValueError("Invalid client email.")
        if not isinstance(phone, str):
            raise TypeError("Client phone must be a string.")
        if not phone:
            raise ValueError("Client phone cannot be empty.")
        self._name = name
        self._surname = surname
        self._email = email
        self._phone = phone

    def get_name(self) -> str:
        """
        Retrieves the first name of the client.

        :return: the client's first name as a string.
        :rtype: str
        """
        return self._name
    def get_surname(self) -> str:
        """
        Retrieves the surname (last name) of the client.

        :return: The client's surname as a string.
        :rtype: str
        """
        return self._surname
    def get_email(self) -> str:
        """
        Retrieves the email address of the client.

        :return: the client's email address as a string.
        :rtype: str
        """
        return self._email
    def get_phone(self) -> str:
        """
        Retrieves the phone number of the client.

        :return: the client's phone number as a string.
        :rtype: str
        """
        return self._phone

    def __str__(self):
        """
        Returns a formatted string representation of the Client object.

        This includes the client's full name (first name and surname),
        email address, and phone number, making it easy to display client details.

        :return: a comprehensive string detailing the client's information.
        :rtype: str
        """
        full_name = f"{self._name} {self._surname}".strip()
        return (f"Client: {full_name}\n"
                f"Email: {self._email}\n"
                f"Phone: {self._phone}")

class Order:
    """
    Represents a customer order within the restaurant system.
    Manages order details including items, total price, status, and associated client and restaurant.
    """
    next_order_number = 0
    def __init__(self, client: Client, restaurant: Restaurant):
        """
        Initializes a new Order object.

        Assigns a unique order number, associates the order with a specific client and restaurant,
        sets the initial status to Pending, and records the current time as the order time.

        :param client: the Client object placing the order. Must be an instance of the Client class.
        :param restaurant: the Restaurant object from which the order is placed. Must be an instance of the Restaurant class.
        :type client: Client
        :type restaurant: Restaurant
        :raises TypeError: if client is not a Client object or restaurant is not a Restaurant object.
        """
        if not isinstance(client, Client):
            raise TypeError("Order must be associated with a valid Client.")
        if not isinstance(restaurant, Restaurant):
            raise TypeError("Order must be associated with a valid Restaurant.")
        self._order_number = Order.next_order_number
        Order.next_order_number += 1
        self._client = client
        self._restaurant = restaurant
        self._items: dict[MenuItem, int] = {}
        self._order_time = datetime.now()
        self._status = "Pending"

    def get_order_number(self) -> int:
        """
        Retrieves the unique order number.

        :return: the integer order number.
        :rtype: int
        """
        return self._order_number
    def get_client(self) -> Client:
        """
        Retrieves the Client object associated with this order.

        :return: the Client object who placed the order.
        :rtype: Client
        """
        return self._client
    def get_restaurant(self) -> Restaurant:
        """
        Retrieves the Restaurant object from which this order was placed.

        :return: the Restaurant object serving the order.
        :rtype: Restaurant
        """
        return self._restaurant
    def get_order_time(self) -> datetime:
        """
        Retrieves the exact date and time when the order was created.

        :return: a datetime object representing the order creation time.
        :rtype: datetime
        """
        return self._order_time
    def get_status(self) -> str:
        """
        Retrieves the current status of the order.

        :return: the order's status (for example, "Pending", "Confirmed", "Delivered") as a string.
        :rtype: str
        """
        return self._status

    def add_item(self, menu_item: MenuItem, quantity: int):
        """
        Adds a specified quantity of a MenuItem to the order.

        If the item is already in the order, its quantity will be updated.
        Otherwise, the item will be added with the given quantity.

        :param menu_item: the MenuItem object to add.
        :type menu_item: MenuItem
        :param quantity: the number of units of the MenuItem to add. Must be a positive integer.
        :type quantity: int
        :raises TypeError: if menu_item is not a MenuItem object or quantity is not an integer.
        :raises ValueError: if quantity is not a positive integer.
        """
        if not isinstance(menu_item, MenuItem):
            raise TypeError("Can only add MenuItem objects to an order.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if menu_item in self._items:
            self._items[menu_item] += quantity
        else:
            self._items[menu_item] = quantity
        print(f"Added {quantity} x {menu_item.get_name()} to order {self.get_order_number()}.")

    def remove_item(self, menu_item: MenuItem):
        """
        Removes a specific MenuItem entirely from the order.

        If the item is not found in the order, a message indicating this is printed.

        :param menu_item: the MenuItem object to remove from the order.
        :type menu_item: MenuItem
        """
        if menu_item in self._items:
            del self._items[menu_item]
            print(f"Removed {menu_item.get_name()} from order {self.get_order_number()}.")
        else:
            print(f"{menu_item.get_name()} not found in order {self.get_order_number()}.")

    def get_total_price(self) -> float:
        """
        Calculates and returns the total price of all items in the order.

        :return: the total price of the order as a float.
        :rtype: float
        """
        total = 0.0
        for item, quantity in self._items.items():
            total += item.get_price() * quantity
        return total

    def update_status(self, new_status: str):
        """
        Updates the status of the order.

        The new status must be one of the predefined valid statuses.

        :param new_status: the new status for the order (for example, "Confirmed", "Delivered").
        Valid statuses: "Pending", "Confirmed", "Preparing", "Out for Delivery", "Delivered", "Cancelled".
        :type new_status: str
        :raises ValueError: if the new_status is not one of the allowed values.
        """
        valid_statuses = ["Pending", "Confirmed", "Preparing", "Out for Delivery", "Delivered", "Cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
        self._status = new_status
        print(f"Order {self.get_order_number()} status updated to: {self.get_status()}")

    def display_order_details(self):
        """
        Returns a detailed, formatted summary of the order as a string.

        This includes the order number, client and restaurant names, order time, current status,
        a list of all items with their quantities and individual prices, and the total order price.
        """
        details = [
            f"Order Details (Order #{self.get_order_number()})",
            f"Client: {self.get_client().get_name()}",
            f"Restaurant: {self.get_restaurant().get_name()}",
            f"Order Time: {self.get_order_time().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Status: {self.get_status()}",
            "Items:"
        ]
        if not self._items:
            details.append("No items in this order.")
        for item, quantity in self._items.items():
            details.append(f"{item.get_name()} x {quantity} (${item.get_price():.2f} each)")
        details.append(f"Total: ${self.get_total_price():.2f}")
        return "\n".join(details)

class Notification:
    """
    Represents a notification to be sent, typically for order updates or promotional messages.
    Manages the message content, recipient, type, and tracks when it was sent.
    """
    def __init__(self, message: str, recipient_email: str, notification_type: str = "Email"):
        """
        Initializes a new Notification object.

        Validates the message content, recipient email, and notification type
        to ensure proper delivery.

        :param message: the content of the notification.
        :param recipient_email: the email address to which the notification will be sent.
        Must contain @.
        :param notification_type: the type of notification (for example, "Email", "SMS"). Defaults to "Email".
        :type message: str
        :type recipient_email: str
        :type notification_type: str
        :raises TypeError: if 'message', 'recipient_email', or 'notification_type' are not strings.
        :raises ValueError: if 'message' or 'recipient_email' are empty, or if 'recipient_email' is not a valid email format.
        """
        if not isinstance(message, str):
            raise TypeError("Notification message must be a string.")
        if not message:
            raise ValueError("Notification message cannot be empty.")
        if not isinstance(recipient_email, str):
            raise TypeError("Recipient email must be a string.")
        if "@" not in recipient_email:
            raise ValueError("Recipient email must be a valid email string.")
        if not isinstance(notification_type, str):
            raise TypeError("Notification type must be a string.")
        self._message = message
        self._recipient_email = recipient_email
        self._notification_type = notification_type
        self._sent_time = None

    def get_message(self) -> str:
        """
        Retrieves the content of the notification message.

        :return: the notification message as a string.
        :rtype: str
        """
        return self._message
    def get_recipient_email(self) -> str:
        """
        Retrieves the email address of the notification's recipient.

        :return: the recipient's email address as a string.
        :rtype: str
        """
        return self._recipient_email
    def get_notification_type(self) -> str:
        """
        Retrieves the type of the notification (for example, "Email", "SMS").

        :return: the notification type as a string.
        :rtype: str
        """
        return self._notification_type
    def get_sent_time(self) -> datetime | None:
        """
        Retrieves the timestamp when the notification was sent.

        :return: a datetime object if the notification has been sent, otherwise None.
        :rtype: datetime | None
        """
        return self._sent_time

    def send(self):
        """
        Simulates sending the notification and records time.

        This method updates the internal '_sent_time' attribute to the current datetime
        and returns a formatted string detailing the notification and its sending time.

        :return: a multi-line string confirming the notification details and send time.
        :rtype: str
        """
        self._sent_time = datetime.now()
        return (f"Sending {self.get_notification_type()} Notification\n"
                f"To: {self.get_recipient_email()}\n"
                f"Message: {self.get_message()}\n"
                f"Sent at: {self.get_sent_time().strftime('%Y-%m-%d %H:%M:%S')}\n")