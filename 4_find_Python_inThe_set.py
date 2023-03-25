# write a python script to find if "Python" is present  in  the set thisset={"Java","Python","Django"}
thisset={"Java","Python","Django"}
'''
if "Python" in thisset:
    print("Python")
'''
result={i for i in  thisset if "Python"==i}
print(result)