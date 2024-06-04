nums_list:list[int] = list(range(1,11,3))
# print(nums_list)


table:range =range(1,11)

for num in table:
    print(f"\n========={num}=========")
    for num2 in table:
        print(f"{num} x {num2} = {num*num2}")
    print(f"========= {num} =========")

