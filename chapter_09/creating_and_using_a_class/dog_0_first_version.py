# # class Dog:
# #     def __init__(self) -> None:
# #         self.name:str = "Aslam"
# #         self.age:int = 40

# # dog:Dog = Dog()
# # print(dog.name)

# class User:
#     name:str = "Aslam Khan"
#     def __init__(self, username:str, email:str) -> None:
#         self.username:str = username
#         self.email:str = email
    

#     def print_username(self)->str:
#         user = self.username
#         return user
    
#     def update_usename(self,new_name:str)->None:
#         self.username = new_name


# user_1:User = User("aslamkhan", "aslam@gmail.com")
# user_2:User = User("asadkahn", "asad@gmail.com")

# print(user_1.username," === ", user_1.email)
# print(user_2.username," === ", user_2.email)
# print(user_2.username," === ", user_2.name)

# print(user_1.print_username())
# user_1.update_usename("khan_aslam")
# print(user_1.print_username())



class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")