names = ["vivek","vishwa","pritika","vinod","aman"]

list_withO = [item for item in names if "v" in item]
print(list_withO)  #items which have v character present

list_with_characters = [item for item in names if(len(item)<6)]
print(list_with_characters)