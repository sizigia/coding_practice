def maskify(str):
    print(str.replace(str[0], '#'))
    pass

print(maskify("4556364607935616") == "############5616")
print(maskify(     "64607935616") ==      "#######5616")
print(maskify(               "1") ==                "1")
print(maskify("") == "")
print(maskify("Skippy")                                   == "##ippy")
print(maskify("Nananananananananananananananana Batman!") == "####################################man!")