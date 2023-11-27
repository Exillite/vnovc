# Structure

- User
  - Novel 1
    - Chapter 1
      - Scene 1
        - node 1
        - node 2
        - node 3
      - Scene 2
        - node 1
        - ...
      - Scene ...
    - Chapter 2
      - Scene1
        - ...
    - Chapter ...
  - Novel 2
    - ...


# Node's types

## Start node
стартовая нода

## Set background node
**Params:**
- bacround uploaded file
- next node

## Speech Node
**Params:**
- person
- peson's sprite
- text
- next node

## Choose node
**Params:**
- question text
- answers
  - answer text
  - next node

## Logic node
**Params:**
- data derictory [global, scene, person]
- optinal perosn
- variable
- condition
- if node
- else node

## Edit variable edit
**Params:**
- data derictory [global, scene, person]
- optinal perosn
- variable
- update

## Goto scene node
**Params:**
- scene