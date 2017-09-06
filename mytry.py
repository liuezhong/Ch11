import apriori
dataSet = apriori.loadDataSet()
# print(dataSet)
# c1 = apriori.createC1(dataSet)
# print(c1)
# D = list(map(set,dataSet))
# print(D)
# L1,suppData0 = apriori.scanD(D,c1,0.5)
# print(L1)
# print(suppData0)

# L,suppData = apriori.apriori(dataSet)
# print(L)

L,suppData = apriori.apriori(dataSet,minSupport=0.5)
rules = apriori.generateRules(L,suppData,minConf=0.7)
print(rules)

rules = apriori.generateRules(L,suppData,minConf=0.5)
print(rules)