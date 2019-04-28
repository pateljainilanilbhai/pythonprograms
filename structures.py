thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
thislist[1] = "blackcurrant"
print(thislist)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print(len(thislist))
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
# The values will remain the same:
print(thistuple)
for x in thistuple:
  print(x)
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
print(len(thistuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
  print(x)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes"])
print(thisset)
print(len(thisset))
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
thisset.clear()
print(thisset)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
thisdict["year"] = 2018
for x in thisdict:
  print(x)
for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x)
for x, y in thisdict.items():
  print(x, y)
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("model")
print(thisdict)