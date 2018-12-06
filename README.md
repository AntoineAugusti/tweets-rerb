[![CircleCI build status](https://img.shields.io/circleci/project/github/AntoineAugusti/tweets-rerb.svg?style=flat-square)](https://circleci.com/gh/AntoineAugusti/tweets-rerb)
[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/AntoineAugusti/tweets-rerb/blob/master/LICENSE.md)

# Tweets RER B
Ce projet permet de récupérer les tweets du compte Twitter de la ligne RER B de Paris [@rerb](https://twitter.com/rerb) et de les archiver en CSV.

La récupération se fait automatiquement toutes les heures et les tweets sont disponibles dans le fichier `tweets.csv`.

## Description des colonnes
- `id` : Identifiant unique du tweet
- `created_at` : Date, heure, minute, secondes du tweet au fuseau horaire UTC
- `text` : Texte du tweet
- `retweet_count` : Nombre de RT du tweet
- `favorite_count` : Nombre de fois où le tweet a été ajouté dans les favoris
- `tweet_mentionne_excuse` : Est-ce que le tweet mentionne le mot "excuse" (0 ou 1)
- `tweet_mentionne_regulation` : Est-ce que le tweet mentionne le mot "régulation" (0 ou 1)
- `tweet_mentionne_bon_courage` : Est-ce que le tweet mentionne le mot "bon courage" (0 ou 1)

## Notice
This software is available under the MIT license.
