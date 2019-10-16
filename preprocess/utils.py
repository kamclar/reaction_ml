def count_reactions(data):
    reaction_count = []
    for item in data:
		print(item)
        reaction_count.append(item.count(':')/2)
    
    return reaction_count