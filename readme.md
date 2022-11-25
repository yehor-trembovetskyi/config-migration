# AAMS
### Fields that game should have to be migrated
- uniqueId
- aamsGameId

### Fields mapping

| LeoAdmin (games.json)    | Lemur                        |
|--------------------------|------------------------------|
| aamsGameId               | aamsGameId                   |
| regulatoryGameType       | aamsGameType                 |
| jackpotEnabled           | aamsJackpotEnabled           |
| bonusEnabled             | aamsBonusEnabled             |
| additionalJackpotEnabled | aamsAdditionalJackpotEnabled |

# DGA
Current branch adds new data migration. 
`rngSoftwareIds` are imported to Lemur from CouchDB JSON dump.
If the game has these fields, non-empty, a Lemur game found by `uniqueId` then data is appended and game is updated.