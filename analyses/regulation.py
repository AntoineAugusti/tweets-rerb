import pandas as pd

df = pd.read_csv('tweets.csv', parse_dates=['created_at']).set_index('id', drop=False)
df['numero_semaine'] = df.apply(lambda row: row['created_at'].strftime('%G-%V'), axis=1)
df['est_en_reponse'] = df.apply(lambda row: row['text'].startswith('@'), axis=1)
df[['numero_semaine', 'est_en_reponse', 'tweet_mentionne_regulation']].to_csv('/tmp/data.csv', index=False)
