import csv

# add twitter account id here
republican_list = ['braun4indiana', 'SenDeanHeller', 'DeanHeller',
                    'RepKevinCramer', 'kevincramer', 'MorriseyWV',
                    'itspatmorrisey', 'HawleyMO', 'AGJoshHawley',
                    'marshablackburn', 'VoteMarsha', 'RepMcSally',
                    'MarthaMcSally', 'FLGovScott', 'scottforflorida']

democrat_list = ['JoeforIndiana', 'SenDonnelly', 'RosenforNevada', 
                    'RepJackyRosen', 'SenatorHeitkamp', 'HeidiHeitkamp',
                    'JoeManchinWV', 'Sen_JoeManchin', 'clairecmc', 
                    'McCaskillOffice', 'PhilBredesen', 'kyrstensinema', 
                    'RepSinema', 'SenBillNelson', 'nelsonforsenate']

def load_data_from_csv(file_name):
    """
    Reads csv file and returns a list of tuples.
    (tweet full text, label - rep or dem)
    """
    with open(file_name) as f:
        reader = csv.reader(f)
        # skip header
        next(reader)
        data = [r for r in reader]
    labeled_data = []
    label = label_tweet_by_file(file_name)
    csv_file_name = file_name.split('csv_files\\')
    screen_name = csv_file_name[0].split('_tweets.csv')
    for i in range(len(data)):
        tweet_text = data[i][2].lstrip("b'").rstrip("'").lower()
        labeled_data.append((tweet_text, screen_name[0], label))
    return labeled_data

def label_tweet_by_file(file_name):
    csv_file_name = file_name.split('csv_files\\')
    print(csv_file_name)
    screen_name = csv_file_name[0].split('_tweets.csv')
    if screen_name[0] in republican_list:
        return 'rep'
    else:
        return 'dem'

def main():
    labeled_data = load_data_from_csv('braun4indiana_tweets.csv')
    print(labeled_data)

if __name__ == "__main__":
    main()
