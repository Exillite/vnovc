# Models

## User
- nickname str
- email str
- password str
- description str
- novels list[Novel]

## Novel
- title str
- description str
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
- type str
