#This is a program to get all of the relationships of an ontology
#Important! This program was written for python3.6.8. 
#the pronto version MUST be 2.4.7 !!!!

"""
Things to address:
"""
import pronto
from pronto.relationship import Relationship, RelationshipData
def prontoRelations(ontoLibrary):
    ontoL = pronto.Ontology.from_obo_library(ontoLibrary) #get ontology
    print(len(ontoL.terms())) #number of terms in ontology
    with open('test-pronto.txt', 'w', encoding='utf-8') as file:
        for term in sorted(ontoL.terms()):
            #print(term)
            file.write(f'{term}\n') #write the term id & name
            try:
                relationshipkeys = sorted(term.relationships.keys())
            except KeyError as e:
                pass
            #^this gets the relationships itself,but not the term connected to it
            file.write(f'Relationships:\n')
            for key in relationshipkeys:
                keyID = key.id
                keyName= key.name
                try:
                    relations = term.relationships[ontoL.get_relationship(keyID)]
                    file.write(f"{keyName}: {relations}\n")
                except KeyError as e:
                    pass
            children: pronto.TermSet = term.subclasses(with_self=True).to_set() #gets subclasses
            file.write(f'subclasses: {children}\n')
            parents: pronto.TermSet = term.superclasses(with_self=True).to_set()
            file.write(f'superclasses: {parents}\n')
"""
    with open('test-pronto-relationships.txt', 'w', encoding='utf-8') as file2:
        for relation in ontoL.relationships():
            file2.write(f'{relation}\n')
"""
prontoRelations("lepao.obo")