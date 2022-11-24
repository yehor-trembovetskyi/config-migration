game_fragment = """
fragment DGEFragment on DGE {
    approvedByDGE
}

fragment DGAFragment on DGA {
    softwareId
    rngId
}

fragment ADMFragment on ADM {
    aamsGameType
    aamsGameId
    aamsJackpotEnabled
    aamsAdditionalJackpotEnabled
    aamsBonusEnabled
}

fragment KSAFragment on KSA {
    riskScore
    riskLevel
}

fragment BetFragment on Bet {
    betConfiguration {
        ...BetConfigurationFragment
    }
    payMechanic
    minWaysToPay
    maxWaysToPay
    volatility
}

fragment LauncherFragment on Launcher {
    id
    name
    device
    externalId
}

fragment BetConfigurationFragment on BetConfiguration {
    id
    country
    minRtp
    maxRtp
    minBet
    maxBet
    operator
    jackpot {
        ...JackpotFragment
    }
}

fragment ProviderFragment on Provider {
    id
}

fragment SlotMetadataFragment on SlotMetadata {
    id
    tags {
        ...TagsFragment
    }
    content {
        ...ContentFragment
    }
    bet {
        ...BetFragment
    }
    releaseDate
    layoutType
    layout
    expandableLayout
    branded
}

fragment JackpotFragment on Jackpot {
    jackpotType
    numberOfJackpots
}

fragment ContentFragment on Content {
    url
    usp
    prio
    exclusive
}

fragment TagsFragment on Tags {
    gameCategory
    gameFeature
    gameSubCategory
}

fragment ConfigFragment on Config {
    id
    country
    launcher {
        ...LauncherFragment
    }
    transaction {
        ...TransactionFragment
    }
    operator
}

fragment TransactionFragment on Transaction {
    id
    externalId
}

fragment RegulatoryGameFragment on RegulatoryGame {
    dge {
        ...DGEFragment
    }
    dga {
        ...DGAFragment
    }
    adm {
        ...ADMFragment
    }
    ksa {
        ...KSAFragment
    }
}

fragment GameFragment on Game {
    id
    uid
    slug
    expectedDate
    gameVariant
    gameType
    provider {
        ...ProviderFragment
    }
    live
    liveInDk
    configs {
        ...ConfigFragment
    }
    slotMetadata {
        ...SlotMetadataFragment
    }
    vertical
    noBonus
    rngMechanic
    regulatoryGame {
        ...RegulatoryGameFragment
    }
    bonusFactor
    tableId
}
"""

game_fragment_v2 = """
fragment DGEFragment on DGE {
    approvedByDGE
}

fragment DGAFragment on DGA {
    softwareId
    rngId
}

fragment ADMFragment on ADM {
    aamsGameType
    aamsGameId
    aamsJackpotEnabled
    aamsAdditionalJackpotEnabled
    aamsBonusEnabled
}

fragment KSAFragment on KSA {
    riskScore
    riskLevel
}

fragment RegulatoryGameFragment on RegulatoryGame {
    dge {
        ...DGEFragment
    }
    dga {
        ...DGAFragment
    }
    adm {
        ...ADMFragment
    }
    ksa {
        ...KSAFragment
    }
}

fragment ProviderFragment on Provider {
    id
}

fragment GameFragment on Game {
    id
    live
    liveInDk
    noBonus
    rngMechanic
    bonusFactor
    tableId
    provider {
        ...ProviderFragment
    }
    regulatoryGame {
        ...RegulatoryGameFragment
    }
}
"""

get_game_query = game_fragment_v2 + """
query getGame($uniqueId: Int) {
  gameInformation {
    game: getGame(input: {id: $uniqueId}) {
      ...GameFragment
    }
  }
}
"""

update_game_mutation = """
mutation updateAdmConfig($game: CreateOrUpdateGameInput!) {
  game: updateGame(input: $game) {
    id
  }
}
"""