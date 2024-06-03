from typing import Union
bicycles:list[Union[str, bool, dict]] = ['trek', 'cannondale', 'redline', 'specialized', True, {
    "name":"test"
}]
nums:list[int] = [100, 200, 300,400]

print(bicycles, nums)