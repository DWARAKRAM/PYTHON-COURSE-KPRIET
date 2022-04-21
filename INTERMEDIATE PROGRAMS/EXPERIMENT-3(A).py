a=[25,24,17,54,7,96,85,79]
b=len(a)
min_value=min(a)
min_index=a.index(min_value)
max_value=max(a)
max_index=a.index(max_value)
print("THE INDEX OF MINIMUM VALUE IS : ",min_index)
print("THE INDEX OF MAXIMUM VALUE IS : ",max_index)
nminindex=min_index-b
nmaxindex=max_index-b
print("NEGATIVE INDEX OF MINIMUM VALUE IS :",nminindex)
print("NEGATIVE INDEX OF MAXIMUM VALUE IS :",nmaxindex)
