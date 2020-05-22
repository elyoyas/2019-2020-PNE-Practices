import termcolor
GENES = {'FRAT1':'ENSG00000165879', 'ADA':'ENSG00000196839',
         'FXN':'ENSG00000165060', 'RNU6_269P':'ENSG00000212379',
         'MIR633':'ENSG00000207552', 'TTTY4C':'ENSG00000228296',
         'RBMY2YP': 'ENSG00000227633', 'FGFR3':'ENSG00000068078',
         'KDR':'ENSG00000128052', 'ANK2':'ENSG00000145362'}
termcolor.cprint("\nGENE DICTIONARY:",'magenta')
print(f'There are {len(GENES)} genes in the list.')
for gene in GENES:
    termcolor.cprint(f"{gene}: ","green", end="")
    print(GENES[gene])

