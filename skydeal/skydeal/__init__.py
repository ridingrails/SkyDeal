#!/usr/bin/env python3

import os
from flask import Flask
from flask.ext.neo4j import Neo4j
from py2neo import Graph, authenticate, Node, Relationship

# Configuration
GRAPH_DATABASE="http://localhost:7474/db/data/"

app = Flask(__name__)
app.config.from_object(__name__)

authenticate("localhost:7474", os.environ['NEO_UN'], os.environ['NEO_PW'])

flask4j = Graph()

#nosferatu = Node('species',full_name='Dracula nosferatu',species_name='nosferatu')
#genus = Node('genus',name='Dracula')
#nosferatu_memberof_genus = Relationship(nosferatu,'Member-of',genus)
#flask4j.create(nosferatu_memberof_genus)



# which all results in a graph that looks like:
#  (species)-[:MEMBER_OF]->(genus)
