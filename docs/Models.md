# Models

## User
- nickname str
- email str
- password str
- bio str
- role str

## Novel
- title str
- description str
- author User
- is_public bool
- persons list[Person]
- chapters list[Chapter]
- data BaseData

## Person
- name str
- description str
- data BaseData
- sprites list[Sprite]

## Sprite
- title str
- image img

## Chapter
- title
- scenes list[Scene]

## Scene
- title
- nodes list[Node]
- data BaseData

## Node
- node_type str
