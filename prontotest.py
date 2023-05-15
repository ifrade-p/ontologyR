import itertools
import os
import unittest
import warnings

import pronto
from pronto.relationship import Relationship, RelationshipData
def prontoRelations(ontoLibrary):
    ontoL = pronto.Ontology.from_obo_library(ontoLibrary)
    print(len(ontoL.terms()))
    with open('test-pronto.txt', 'w', encoding='utf-8') as file:
        for term in sorted(ontoL.terms()):
            #print(term)
            file.write(f'{term}\n')
            relationshipkeys = sorted(term.relationships.keys())
            file.write(f'Relationships:\n')
            for key in relationshipkeys:
                keyID = key.id
                keyName= key.name
                relations = term.relationships[ontoL.get_relationship(keyID)]
                file.write(f"{keyName}:  {relations}\n")
            children: pronto.TermSet = term.subclasses(with_self=True).to_set()
            file.write(f'children: {children}\n')
            parents: pronto.TermSet = term.superclasses(with_self=True).to_set()
            file.write(f'parents: {parents}\n')
    with open('test-pronto-relationships.txt', 'w', encoding='utf-8') as file2:
        for relation in ontoL.relationships():
            file2.write(f'{relation}\n')
prontoRelations("lepao.owl")