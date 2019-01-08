import chartify
import pandas as pd

cols = ['tweet_mentionne_excuse', 'tweet_mentionne_bon_courage']

df = pd.read_csv('../tweets.csv', parse_dates=['created_at']).set_index('id', drop=False)
data = pd.DataFrame(df.groupby(df.created_at.dt.strftime('%G-%V'))[cols].sum().stack().rename('value'))
data.index.names = ['date', 'type']
data.reset_index(inplace=True)

ch = chartify.Chart(x_axis_type='categorical', y_axis_type='linear')
ch.set_title("Tweets du RER B souhaitant bon courage ou présentant des excuses")
ch.set_source_label('Tweets @rerb')

ch.axes.set_yaxis_label('Nombre de tweets')
ch.axes.set_xaxis_label('Semaines')
ch.axes.set_xaxis_tick_orientation('vertical')

ch.plot.bar(
    data_frame=data,
    categorical_columns=['date', 'type'],
    numeric_column='value',
    color_column='type',
    categorical_order_by='labels',
    categorical_order_ascending=True)

ch.show('html')
