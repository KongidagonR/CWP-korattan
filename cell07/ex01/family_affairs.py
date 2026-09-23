def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family.keys()))


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))

#family.key() คือ เอาชื่อเเต่ละคนมา
#lambda name คือ ไล่ทีละชื่อ เอาไปตรวจสอบ