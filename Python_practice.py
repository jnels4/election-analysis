votingdata  = []
votingdata.append({"county":"Arapahoe","registered_voters":422829})
votingdata.append({"county":"Denver","registered_voters":463353})
votingdata.append({"county":"Jefferson","registered_voters":432438})
print(votingdata)
votingdata.insert(1,{"county":"El Paso","registered_voters":461149})
print(votingdata)
votingdata.remove({"county":"Arapahoe","registered_voters":422829})
print(votingdata)
votingdata.insert(3,({"county":"Denver","registered_voters":463353}))
print(votingdata)
votingdata.remove({"county":"Denver","registered_voters":463353})
print(votingdata)
votingdata.append({"county":"Arapahoe","registered_voters":422829})
print(votingdata)

for countydict in votingdata:
    #print(county + " county has " + str(voters) + " registered voters")
    print (countydict)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county,voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for countydict in voting_data:
        print(f"{countydict['county']} county has {countydict['registered_voters']:,} registered voters")
