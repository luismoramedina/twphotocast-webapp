from birdy.twitter import AppClient
import myconfig

__author__ = 'mora'

#SAVED_ACCESS_TOKEN = None
#access_token = client.get_access_token()
#client = AppClient(CONSUMER_KEY, CONSUMER_SECRET)
#SAVED_ACCESS_TOKEN = access_token
#print access_token

def get_media_links(username):
    global client, response, twit
    client = AppClient(myconfig.CONSUMER_KEY, myconfig.CONSUMER_SECRET, myconfig.SAVED_ACCESS_TOKEN)
    #response = client.api.users.show.get(screen_name='luismoramedina')
    #print json.dumps(response.data)
    #response = client.api.statuses.user_timeline.get(screen_name='luismoramedina')
    # Action: get timeline
    response = client.api.statuses.user_timeline.get(screen_name=username, count=200)
    #response = client.api.statuses.user_timeline.get(screen_name='luismoramedina')
    #response = client.api.statuses.user_timeline.get(screen_name='pilibohi')
    #print response.data[0]['text']
    # Action: parse timeline
    data = []
    for twit in response.data:
        if 'entities' in twit and 'media' in twit['entities']:
            data.append(twit['entities']['media'][0]['media_url'])
    # for twit in response.data:
    #     if 'entities' in twit and 'urls' in twit['entities']:
    #         for url in twit['entities']['urls']:
    #             expanded_url = url['expanded_url']
    #             if 'instagram' in expanded_url:
    #                 data.append(expanded_url + 'media/')
    #             else:
    #                 data.append(expanded_url)

    return data


#get_media_links()#do_get('http://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name' : 'juaenima'}, {'a' : 'a'})
#parse_data(data)

