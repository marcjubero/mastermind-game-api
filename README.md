# mastermind-game-api



### TODOS
- [x] Game algorithm
- [x] Define HTTP Rest API
- [ ] Implement HTTP Rest API
- [ ] Define DB schema
- [ ] Create game (given a user request)
- [ ] Return feedback given a code guess
- [ ] Check game historic


#### Define HTTP Rest API
*All responses are json formatted*

*All resources, in case of server side error, return HTTP 500: Something went terribly wrong on server side 

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
  
* @GET /board/games/{id}/guesses - Return guesses
  * 200 - OK
  * 204 - Empty
  * 404 - Game not found

* @GET /board/games/{id}/guesses/{id} - Return guess
  * 200 - OK
  * 404 - Game or guess not found


