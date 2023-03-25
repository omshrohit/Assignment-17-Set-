# write a python  script to add items from another set to the current ser.thisset={"Java","Python","SQL"}
# SECONTDSET={"C","Cpp","NoSQL"}
thisset={"Java","Python","SQL"}
secondset={"C","Cpp","NoSQL"}

for i in secondset:
    # add() always takes hash value
    thisset.add(i)
print(thisset)
