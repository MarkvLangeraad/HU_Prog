def ticker():
    # creating the function for reading the file and looking put it into the dictionary
    Comp = {}
    with open('company.txt') as file:
        for line in file:
            key, value = line.split(":")
            Comp[key] = value

    jaja= input('Enter a symbol:')
    for company, symbol in Comp.items():
        if jaja in symbol:
            print('Company name:', company)


    neenee = input('Enter a company:')
    for company, symbol in Comp.items():
        if neenee in company:
            print('Ticker symbol:', symbol)




ticker()
