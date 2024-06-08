# squares:list[int] = [value**2 for value in range(1, 11)]
# print(squares)


# squares:list[int] = [value for value in range(1, 11)]
# # print(squares)


users:list[dict[str, str]] = [
    {
        "name":"username 1",
        "email":"email_1@gmail.com",
    },
    {
        "name":"username 1",
        "email":"email_1@gmail.com",
    },
    {
        "name":"username 1",
        "email":"email_1@gmail.com",
    },
    {
        "name":"username 1",
        "email":"email_1@gmail.com",
    },{
        "name":"username 1",
        "email":"email_1@gmail.com",
    }

]

mails:list[dict[str,str]] = [{"email":usr["email"]} for usr in users]
# nams:list[str] = [usr["name"] for usr in users]
print(mails)
# print(nams)



# def sqr(num:int):
#     return num**2


# squares =  [sqr(v) for v in range(1,11)]

# print(squares)