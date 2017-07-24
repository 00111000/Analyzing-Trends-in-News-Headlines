import json
import csv
import string


def remove_punctuation(s):
    for c in string.punctuation:
        s = s.replace(c, '')

    s = s.replace('‘', '')
    s = s.replace('–', '')
    s = s.replace('’', '')
    s = s.replace('\n', '')
    s = s.replace('\t', '')

    return s


countries = {}

headline = ''
network = ''
id = 0
trump = 0
putin = 0
trudeau = 0
date = ''
time = ''

date_counter = 0

with open('2.txt', 'r') as fp:

    # Create a CSV file and define the headers
    csv_file = csv.writer(open("test.csv", "w"))
    csv_file.writerow(
        ['ID', 'DATE', 'TIME', 'NETWORK', 'HEADLINE', 'SENTIMENT_LABEL', 'SENTIMENT_SCORE', 'EMOTION_SADNESS', 'EMOTION_FEAR',
         'EMOTION_ANGER', 'EMOTION_DISGUST', 'EMOTION_JOY', 'PUTIN', 'TRUMP', 'TRUDEAU'])

    while True:

        # Read one line at a time
        data = fp.readline()

        if data == '':
            break

        if date_counter == 0:
            date = data[:10]
            time = data[12:].replace('\n', '')
            date_counter += 1

        if data[0] == 'H':
            headline = data[2:].replace('\n', '')

            cleaned_text = remove_punctuation(headline).lower()

            if 'trump' in cleaned_text and 'jr' not in cleaned_text:
                trump += 1

            if 'putin' in cleaned_text:
                putin += 1

            if 'trudeau' in cleaned_text:
                trudeau += 1

        if data[0] == 'N':
            network = remove_punctuation(data[2:])

        if data[0] == 'J':

            # Convert text into JSON
            json_data = json.loads(data[2:])

            # print(json.dumps(json_data, indent = 2))

            if 'entities' in json_data:

                for entity in json_data['entities']:

                    if (entity['type'] == 'Location' and 'Country' in entity['disambiguation']['subtype']):

                        cleaned_text = remove_punctuation(entity['text'])

                        if cleaned_text in countries:
                            countries[cleaned_text] += 1
                        else:
                            countries[cleaned_text] = 1

            # Write row with data and set cursor to next row
            csv_file.writerow([id,
                               date,
                               time,
                               network,
                               headline,
                               json_data['sentiment']['document']['label'] if 'sentiment' in json_data else '',
                               json_data['sentiment']['document']['score'] if 'sentiment' in json_data else '',
                               json_data['emotion']['document']['emotion']['sadness'] if 'emotion' in json_data else '',
                               json_data['emotion']['document']['emotion']['fear'] if 'emotion' in json_data else '',
                               json_data['emotion']['document']['emotion']['anger'] if 'emotion' in json_data else '',
                               json_data['emotion']['document']['emotion']['disgust'] if 'emotion' in json_data else '',
                               json_data['emotion']['document']['emotion']['joy'] if 'emotion' in json_data else '',
                               putin,
                               trump,
                               trudeau])

            id += 1

            # Clear counters
            trump = 0
            putin = 0
            trudeau = 0

date_counter = 0

fp.close()

print(json.dumps(countries, indent=2))
