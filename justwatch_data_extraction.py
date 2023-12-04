
import requests
import json

count = 0

list_movies = []

url = 'https://apis.justwatch.com/graphql'

query = {
  "operationName": "GetPopularTitles",
  "variables": {
    "first": 100,
    "platform": "WEB",
    "popularTitlesSortBy": "POPULAR",
    "sortRandomSeed": 0,
    "offset": count,
    "creditsRole": "DIRECTOR",
    "after": None,
    "popularTitlesFilter": {
      "ageCertifications": [],
      "excludeGenres": [],
      "excludeProductionCountries": [],
      "objectTypes": [],
      "productionCountries": [],
      "genres": [],
      "packages": [],
      "excludeIrrelevantTitles": False,
      "presentationTypes": [],
      "monetizationTypes": []
    },
    "watchNowFilter": {
      "packages": [],
      "monetizationTypes": []
    },
    "language": "pt",
    "country": "BR",
    "allowSponsoredRecommendations": {
      "appId": "3.8.2-webapp#9dea184",
      "country": "BR",
      "language": "pt",
      "pageType": "VIEW_POPULAR",
      "placement": "POPULAR_VIEW",
      "platform": "WEB"
    }
  },
  "query": "query GetPopularTitles($allowSponsoredRecommendations: SponsoredRecommendationsInput, $backdropProfile: BackdropProfile, $country: Country!, $first: Int! = 70, $format: ImageFormat, $language: Language!, $platform: Platform! = WEB, $after: String, $popularTitlesFilter: TitleFilter, $popularTitlesSortBy: PopularTitlesSorting! = POPULAR, $profile: PosterProfile, $sortRandomSeed: Int! = 0, $watchNowFilter: WatchNowOfferFilter!, $offset: Int = 0, $creditsRole: CreditRole! = DIRECTOR) {\n  popularTitles(\n    allowSponsoredRecommendations: $allowSponsoredRecommendations\n    country: $country\n    filter: $popularTitlesFilter\n    first: $first\n    sortBy: $popularTitlesSortBy\n    sortRandomSeed: $sortRandomSeed\n    offset: $offset\n    after: $after\n  ) {\n    edges {\n      ...PopularTitleGraphql\n      __typename\n    }\n    pageInfo {\n      startCursor\n      endCursor\n      hasPreviousPage\n      hasNextPage\n      __typename\n    }\n    sponsoredAd {\n      ...SponsoredAdFragment\n      __typename\n    }\n    totalCount\n    __typename\n  }\n}\n\nfragment PopularTitleGraphql on PopularTitlesEdge {\n  cursor\n  node {\n    id\n    objectId\n    objectType\n    content(country: $country, language: $language) {\n      title\n      fullPath\n      scoring {\n        imdbVotes\n        imdbScore\n        tmdbPopularity\n        tmdbScore\n        __typename\n      }\n      dailymotionClips: clips(providers: [DAILYMOTION]) {\n        sourceUrl\n        externalId\n        provider\n        __typename\n      }\n      posterUrl(profile: $profile, format: $format)\n      ... on MovieOrShowOrSeasonContent {\n        backdrops(profile: $backdropProfile, format: $format) {\n          backdropUrl\n          __typename\n        }\n        __typename\n      }\n      isReleased\n      credits(role: $creditsRole) {\n        name\n        personId\n        __typename\n      }\n      scoring {\n        imdbVotes\n        __typename\n      }\n      runtime\n      genres {\n        translation(language: $language)\n        __typename\n      }\n      __typename\n    }\n    likelistEntry {\n      createdAt\n      __typename\n    }\n    dislikelistEntry {\n      createdAt\n      __typename\n    }\n    watchlistEntryV2 {\n      createdAt\n      __typename\n    }\n    customlistEntries {\n      createdAt\n      __typename\n    }\n    freeOffersCount: offerCount(\n      country: $country\n      platform: $platform\n      filter: {monetizationTypes: [FREE]}\n    )\n    watchNowOffer(country: $country, platform: $platform, filter: $watchNowFilter) {\n      id\n      standardWebURL\n      package {\n        id\n        packageId\n        clearName\n        __typename\n      }\n      retailPrice(language: $language)\n      retailPriceValue\n      lastChangeRetailPriceValue\n      currency\n      presentationType\n      monetizationType\n      availableTo\n      __typename\n    }\n    ... on Movie {\n      seenlistEntry {\n        createdAt\n        __typename\n      }\n      __typename\n    }\n    ... on Show {\n      tvShowTrackingEntry {\n        createdAt\n        __typename\n      }\n      seenState(country: $country) {\n        seenEpisodeCount\n        progress\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SponsoredAdFragment on SponsoredRecommendationAd {\n  bidId\n  holdoutGroup\n  campaign {\n    externalTrackers {\n      type\n      data\n      __typename\n    }\n    hideRatings\n    promotionalImageUrl\n    watchNowLabel\n    watchNowOffer {\n      standardWebURL\n      presentationType\n      monetizationType\n      package {\n        id\n        packageId\n        shortName\n        clearName\n        icon\n        __typename\n      }\n      __typename\n    }\n    node {\n      id\n      ... on MovieOrShow {\n        content(country: $country, language: $language) {\n          fullPath\n          posterUrl\n          title\n          originalReleaseYear\n          scoring {\n            imdbScore\n            __typename\n          }\n          externalIds {\n            imdbId\n            __typename\n          }\n          backdrops(format: $format, profile: $backdropProfile) {\n            backdropUrl\n            __typename\n          }\n          isReleased\n          __typename\n        }\n        objectId\n        objectType\n        offers(country: $country, platform: $platform) {\n          monetizationType\n          presentationType\n          package {\n            id\n            packageId\n            __typename\n          }\n          id\n          __typename\n        }\n        watchlistEntryV2 {\n          createdAt\n          __typename\n        }\n        __typename\n      }\n      ... on Show {\n        seenState(country: $country) {\n          seenEpisodeCount\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
}

for data_movie in range(0, 820):

    response = requests.post(url=url, json=query)

    json_response = response.json()

    if response.status_code != 200:
        break

    try:
        if json_response['errors']:
            break
    except Exception:
        pass

    count += 100

    query = {
        "operationName": "GetPopularTitles",
        "variables": {
            "first": 100,
            "platform": "WEB",
            "popularTitlesSortBy": "POPULAR",
            "sortRandomSeed": 0,
            "offset": count,
            "creditsRole": "DIRECTOR",
            "after": None,
            "popularTitlesFilter": {
                "ageCertifications": [],
                "excludeGenres": [],
                "excludeProductionCountries": [],
                "objectTypes": [],
                "productionCountries": [],
                "genres": [],
                "packages": [],
                "excludeIrrelevantTitles": False,
                "presentationTypes": [],
                "monetizationTypes": []
            },
            "watchNowFilter": {
                "packages": [],
                "monetizationTypes": []
            },
            "language": "pt",
            "country": "BR",
            "allowSponsoredRecommendations": {
                "appId": "3.8.2-webapp#9dea184",
                "country": "BR",
                "language": "pt",
                "pageType": "VIEW_POPULAR",
                "placement": "POPULAR_VIEW",
                "platform": "WEB"
            }
        },
        "query": "query GetPopularTitles($allowSponsoredRecommendations: SponsoredRecommendationsInput, $backdropProfile: BackdropProfile, $country: Country!, $first: Int! = 70, $format: ImageFormat, $language: Language!, $platform: Platform! = WEB, $after: String, $popularTitlesFilter: TitleFilter, $popularTitlesSortBy: PopularTitlesSorting! = POPULAR, $profile: PosterProfile, $sortRandomSeed: Int! = 0, $watchNowFilter: WatchNowOfferFilter!, $offset: Int = 0, $creditsRole: CreditRole! = DIRECTOR) {\n  popularTitles(\n    allowSponsoredRecommendations: $allowSponsoredRecommendations\n    country: $country\n    filter: $popularTitlesFilter\n    first: $first\n    sortBy: $popularTitlesSortBy\n    sortRandomSeed: $sortRandomSeed\n    offset: $offset\n    after: $after\n  ) {\n    edges {\n      ...PopularTitleGraphql\n      __typename\n    }\n    pageInfo {\n      startCursor\n      endCursor\n      hasPreviousPage\n      hasNextPage\n      __typename\n    }\n    sponsoredAd {\n      ...SponsoredAdFragment\n      __typename\n    }\n    totalCount\n    __typename\n  }\n}\n\nfragment PopularTitleGraphql on PopularTitlesEdge {\n  cursor\n  node {\n    id\n    objectId\n    objectType\n    content(country: $country, language: $language) {\n      title\n      fullPath\n      scoring {\n        imdbVotes\n        imdbScore\n        tmdbPopularity\n        tmdbScore\n        __typename\n      }\n      dailymotionClips: clips(providers: [DAILYMOTION]) {\n        sourceUrl\n        externalId\n        provider\n        __typename\n      }\n      posterUrl(profile: $profile, format: $format)\n      ... on MovieOrShowOrSeasonContent {\n        backdrops(profile: $backdropProfile, format: $format) {\n          backdropUrl\n          __typename\n        }\n        __typename\n      }\n      isReleased\n      credits(role: $creditsRole) {\n        name\n        personId\n        __typename\n      }\n      scoring {\n        imdbVotes\n        __typename\n      }\n      runtime\n      genres {\n        translation(language: $language)\n        __typename\n      }\n      __typename\n    }\n    likelistEntry {\n      createdAt\n      __typename\n    }\n    dislikelistEntry {\n      createdAt\n      __typename\n    }\n    watchlistEntryV2 {\n      createdAt\n      __typename\n    }\n    customlistEntries {\n      createdAt\n      __typename\n    }\n    freeOffersCount: offerCount(\n      country: $country\n      platform: $platform\n      filter: {monetizationTypes: [FREE]}\n    )\n    watchNowOffer(country: $country, platform: $platform, filter: $watchNowFilter) {\n      id\n      standardWebURL\n      package {\n        id\n        packageId\n        clearName\n        __typename\n      }\n      retailPrice(language: $language)\n      retailPriceValue\n      lastChangeRetailPriceValue\n      currency\n      presentationType\n      monetizationType\n      availableTo\n      __typename\n    }\n    ... on Movie {\n      seenlistEntry {\n        createdAt\n        __typename\n      }\n      __typename\n    }\n    ... on Show {\n      tvShowTrackingEntry {\n        createdAt\n        __typename\n      }\n      seenState(country: $country) {\n        seenEpisodeCount\n        progress\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SponsoredAdFragment on SponsoredRecommendationAd {\n  bidId\n  holdoutGroup\n  campaign {\n    externalTrackers {\n      type\n      data\n      __typename\n    }\n    hideRatings\n    promotionalImageUrl\n    watchNowLabel\n    watchNowOffer {\n      standardWebURL\n      presentationType\n      monetizationType\n      package {\n        id\n        packageId\n        shortName\n        clearName\n        icon\n        __typename\n      }\n      __typename\n    }\n    node {\n      id\n      ... on MovieOrShow {\n        content(country: $country, language: $language) {\n          fullPath\n          posterUrl\n          title\n          originalReleaseYear\n          scoring {\n            imdbScore\n            __typename\n          }\n          externalIds {\n            imdbId\n            __typename\n          }\n          backdrops(format: $format, profile: $backdropProfile) {\n            backdropUrl\n            __typename\n          }\n          isReleased\n          __typename\n        }\n        objectId\n        objectType\n        offers(country: $country, platform: $platform) {\n          monetizationType\n          presentationType\n          package {\n            id\n            packageId\n            __typename\n          }\n          id\n          __typename\n        }\n        watchlistEntryV2 {\n          createdAt\n          __typename\n        }\n        __typename\n      }\n      ... on Show {\n        seenState(country: $country) {\n          seenEpisodeCount\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
    }

    list_movies.append(json_response)

    print(json_response['data']['popularTitles']['edges'][0]['node']['content']['title'])

with open("data_movies.json", "w") as arquivo:
    json.dump(list_movies, arquivo, indent=4)
