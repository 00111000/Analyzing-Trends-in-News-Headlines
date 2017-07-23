import json
import csv
import string

def remove_punctuation(s):
   for c in string.punctuation:
      s = s.replace(c, '')

   return s

countries = {}

headline = ''
network = ''
id = 1
trump = 0
putin = 0
trudeau = 0

with open('1.txt', 'r') as fp:

   # Create a CSV file and define the headers
   csv_file = csv.writer(open("test.csv", "w"))
   csv_file.writerow(['ID', 'NETWORK', 'HEADLINE','SENTIMENT-LABEL', 'SENTIMENT-SCORE', 'EMOTION-SADNESS', 'EMOTION-FEAR', 'EMOTION-ANGER', 'EMOTION-DISGUST', 'EMOTION-JOY', 'PUTIN', 'TRUMP', 'TRUDEAU'])

   while True:

      # Read one line at a time
      data = fp.readline()

      if data == '':
         break

      if data[0] == 'H':
          headline = data[2:]

      if data[0] == 'N':
         network = data[2:]

      if data[0] == 'J':

         # Convert text into JSON
         json_data = json.loads(data[2:])

         # print(json.dumps(json_data, indent = 2))
         # print(json_data['entities'])

         for entity in json_data['entities']:

            if(entity['type'] == 'Location' and 'Country' in entity['disambiguation']['subtype']):

               cleaned_text = remove_punctuation(entity['text'])

               if cleaned_text in countries:
                  countries[cleaned_text] += 1
               else:
                  countries[cleaned_text] = 1

            if (entity['type'] == 'Person'):

               cleaned_text = remove_punctuation(entity['text']).lower()

               if 'trump' in cleaned_text and 'jr' not in cleaned_text:
                  trump += 1
               elif 'putin' in cleaned_text:
                  putin += 1
               elif 'trudeau' in cleaned_text:
                  trudeau += 1

         # Write row with data and set cursor to next row
         csv_file.writerow([id,
                            network,
                            headline,
                            json_data['sentiment']['document']['label'],
                            json_data['sentiment']['document']['score'],
                            json_data['emotion']['document']['emotion']['sadness'],
                            json_data['emotion']['document']['emotion']['fear'],
                            json_data['emotion']['document']['emotion']['anger'],
                            json_data['emotion']['document']['emotion']['disgust'],
                            json_data['emotion']['document']['emotion']['joy'],
                            putin,
                            trump,
                            trudeau])

         id += 1

         # Clear counters
         trump = 0
         putin = 0
         trudeau = 0

fp.close()

print(json.dumps(countries, indent = 2))