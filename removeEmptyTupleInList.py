#Python | Remove empty tuples from a list
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (','),()]
for tuple in tuples:
    if len(tuple)==0:
        tuples.remove(tuple)
print(tuples)