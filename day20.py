#dictionary
dic={
    1:"max", 11:"perez",16:"charles", 55:"carlos",4:"lando",81:"oscar", 44:"lewis"
}
dri={10:"gasly",33:"ocon",99:"yuki"}
dic.update(dri)
dic.pop(11)
del dic[4]
for key in dic.keys():
    print(dic[key])