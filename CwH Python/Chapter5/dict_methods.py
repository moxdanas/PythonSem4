marks = {
    "anas":100,
    "cyborg":99,
    "firewalker":90,
    0:"Harry",
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"anas":99,"johndoe":93,})
print(marks)

print(marks.get("anas2")) #return None
print(marks["anas2"])#return an error  