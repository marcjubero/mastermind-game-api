# mastermind-game-api

### Installation
Use the Dockerfile provided in order to the API without use any virtual environments nor dependency management.

### Before start playing, some considerations:
* A game finishes when:
  *  A user finds out the secret color combination
  * Reached the maximum number of retries: **12**
* Allowed input colors: ``RED``, ``ORANGE``, ``YELLOW``, ``GREEN``, ``BLUE``,``INDIGO`` and ``VIOLET`` 
* No blanks allowed, guesses or secrets **must** be 4 lenght combinations og the colors above

### Usage
#### Game creation (@POST /board/games)
New game is created with an HTTP/POST call to */v1/board/games* specifying the secret color combination. **i.e**
```json
{
  "secret": ["RED", "YELLOW", "RED", "BLUE"]
}
```

#### Turns (@POST /board/games/*{game_id}*/guess)
Each turn is played by doing an HTTP/POST call to */v1/board/games/{game_id}/guess* specifying the guess color combination. **i.e**
```json
{
  "guess": ["INDIGO", "YELLOW", "BLUE", "RED"]
}
```
The server will answer with the proper combination of *WHITEs* and *BLACKs*. **i.e**
For the previous guess, the server response should be the following:
```json
{
	"result": ["BLACK", "WHITE", "WHITE"]
}
```

#### Game information (@ GET /board/games/*{id_game}*)
Game information
```json
{
	"id": 2,
	"secret": ["RED", "GREEN", "GREEN", "BLUE"],
	"guesses": [
		{
			"id": 1,
			"value": ["YELLOW", "GREEN", "YELLOW", "RED"],
			"result": ["BLACK", "WHITE"]
		},
		...
		{
			"id": n,
			"value": ["RED", "GREEN", "GREEN", "BLUE"],
			"result": ["BLACK", "BLACK", "BLACK", "BLACK"]
		}
	]
}
```

#### Game historic (@GET /board)
Games list  **i.e**
```json
[
	{
  	"id": 1,
    "secret": ["RED", "GREEN", "BLUE", "YELLOW"],
    "guesses": []
  },
  {
  	"id": 2,
    "secret": ["RED", "GREEN", "GREEN", "BLUE"],
    "guesses": [
    	{
      	"id": 1,
        "value": ["YELLOW", "GREEN", "YELLOW", "RED"],
        "result": ["BLACK", "WHITE"]
      },
      ...
      {
      	"id": n,
        "value": ["RED", "GREEN", "GREEN", "BLUE"],
        "result": ["BLACK", "BLACK", "BLACK", "BLACK"]
			}
    ]
  }
]
```
### Future
- [ ] Improve environment management
- [ ] Allow game variations
	- [ ] Game duration (turns)
	- [ ] Secret & Guess lenght
	- [ ] Define more colors

###TODOS
- [x] Game algorithm
- [x] Define HTTP Rest API
- [x] Implement HTTP Rest API
- [x] Define DB schema
- [x] Create game (given a user request)
- [x] Return feedback given a code guess
- [x] Check game historic
- [x] Game algorithm improvements (types, checks, ...)


#### Define HTTP Rest API
**All responses are json formatted**

**All resources, in case of server side error, return HTTP 500: Something went terribly wrong on server side **

* @GET /board - Games historic 
  * 200 - OK
  * 204 - No games played yet

* @POST /board/games - Create new game
  * 201 - OK created (return Location header)
  * 400 - Invalid input
  
* @GET /board/games/{id} - Return game info (secret and guesses)
  * 200 - OK (return game info)
  * 404 - Game not found
  
* @POST /board/games/{id}/guesses - Create new guess
  * 201 - OK created
  * 404 - Game not found
  * 400 - Invalid input
  
* ~~@GET /board/games/{id}/guesses - Return guesses~~
  * ~~200 - OK~~
  * ~~204 - Empty~~
  * ~~404 - Game not found~~

* ~~@GET /board/games/{id}/guesses/{id} - Return guess~~
  * ~~200 - OK~~
  * ~~404 - Game or guess not found~~


