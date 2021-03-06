### FUNCTION 1: Metric Dictionary ###

from module import dictionary_of_metrics
items = [39660.0,
         36024.0,
         32127.0,
         39488.0,
         18422.0,
         23532.0,
         8842.0,
         37416.0,
         16156.0,
         18730.0,
         19261.0,
         25275.0]
dictionary_of_metrics(items) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'variance': 108160153.17,
                                   'standard deviation': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}

### FUNCTION 2: Five Number Summary ###

from module import five_num_summ
# Do some tests here

### FUNCTION 3: Date Parser ###

from module import date_parser
# Do some tests here

### FUNCTION 4: Hashtag & Municipality Extractor ###

from module import extract_municipality_hashtags
# Do some tests here

### FUNCTION 5: Number Of Tweets Per Day ###

from module import number_of_tweets_per_day
# Do some tests here

### FUNCTION 6: Word Splitter ###

from module import word_spliter
# Do some tests here

### FUNCTION 7: Stop Word Remover ###

from module import stop_words_http_remover
# Do some tests here
