"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
# Create an empty list of salespeople 
melons_sold = []
# Create an emplty list of the number of melons sold
# Would be more efficient to make a dictionary with salespeople as the keys & the melons they've sold as values

f = open('sales-report.txt')
# Open the sales-report file and assign it to "f"
for line in f:
# for each line of the file...
    line = line.rstrip()
    # remove whitespace at the end of the line, as well as \n
    entries = line.split('|')
    # Each file line contains 3 pieces of information, which can be separated out by a pipe

    salesperson = entries[0]
    # The first piece of info in each line is the salesperson
    melons = int(entries[2])
    # The third piece of info in each line is the number of melons sold

    if salesperson in salespeople:
    # Searching for each name that's in the list of salespeople
        position = salespeople.index(salesperson)
        # Assigning the index of that salesperson to "position" so that we can map their melons sold to them

        melons_sold[position] += melons
        # Filling the melons_sold list with the number of melons sold by a salesperson with the corresponding index from the salespeople list

        # This comparison of indices is error-prone and inefficient; it could be circumvented by using a dictionary with key-value pairs, instead
         
    else:
        salespeople.append(salesperson)
        # if the salesperson isn't yet in the salespeople list, add them to the end
        melons_sold.append(melons)
        # and then add the number of melons that person has sold to the end of the melons_sold list

        # Simply adding a key-value pair to a dictionary would achieve this same effect


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    # Loop through the salespeople list and print the name of each salesperson and the number of melons they sold, which lives in the separate melons_sold list
