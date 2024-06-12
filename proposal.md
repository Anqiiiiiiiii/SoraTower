# Proposal
## summary
***
This is a puzzle Tower climbing game, in this game, the player will be selected as the Sora child to start their adventure in the Sora Tower. They will discover their identity step by step through each level of puzzles. This game tentatively has five layers of towers for players to play, in each layer of towers, players will meet NPCS to tell the story of the sky, will also encounter difficult puzzles, solve the puzzles can get the key to this layer, open the next layer.
***
## Require features
***
There will be basic maps showing where the player is right now.
There will be different puzzles for each layer.
There will have a rich plot guide.
There will have a basic menu Will allow players to diy their own name.
There will be basic actions for the player to choose from, such as walking, picking up, etc.
There will be functions to save and load the game.
***
## desired features
***
The puzzles will no longer be basic text, the system will detect if the player has a key item to solve the puzzle.
You have NPCS that you can talk to.
The player has a log book to view conversations with previous NPCS. 
Search capabilities will be developed.
The first tier of the map will have different partitions/gameplay.
Special rooms that will give 
***
## Target user
***
This game is aimed at anyone who likes to watch the plot, and likes to solve puzzles, and thinks that they have rich knowledge of chemistry and mathematics!
***

## Structure
### files:
       - main.py
       - character.py
       - map.py (including multiple layers)
       - room.py
       - items.py
       - puzzle.py (random puzzles for layers)

### objects:
      - Parent Class: character: position(x, y)
        - player: position(x, y), backpack, chatting history
        - npc: position(x, y), chat

      - Class: Map

      - Parent Class: room: name, description
        - normal room: name, description, item
        - puzzle room: name, description, puzzle, required item, (bool)passed

      - Class: Items: name, description

      - Puzzle: question, answer

      Room templates:
          Room 1: Name: Chemistry Room
                Description: This is a Chemistry Room

          Room 2: Name: Gym 
                  Description: This is a Gym 

          Map:  [[Start Point][2][1][1],
                [1][2][2][1],
                [1][2][2][1],
                [1][1][1][Puzzle Room]]

### functions:
      - main menu (display descriptions and control character movements)
        - print descriptions
        - ask player wanna walk or explore
          - if in puzzle room
            - if not passed:
              - check required item
              - give the puzzle
              - meet NPC after solving the puzzle
              - passed
            - else if passed:
              - add "next level" option inton main menu
              
      - map creator (randomly creates the map)
      
      - item placer (random place the item in the currenly layer, base on the required item)
      
      - Create random puzzles in puzzle rooms
      
      
     