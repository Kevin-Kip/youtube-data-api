import urllib.request
import json


def get_data(user_name):
    api_key = "AIzaSyBT7PXSCy-RdsLhWyN8itRaqVCTfeOL7Fc"  # YOUR API KEY HERE
    user_name = replace(user_name)
    base_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+user_name+"&key="+api_key

    CRED = '\033[91m'
    CEND = '\033[0m'

    response = urllib.request.urlopen(base_url).read()
    parsed_response = json.loads(response)

    if parsed_response["pageInfo"]["totalResults"] == 0:
        print("No data found")
    else:
        data = parsed_response["items"][0]["statistics"]
        views = data["viewCount"]
        subscribers = data["subscriberCount"]
        videos = data["videoCount"]
        print(CRED + "{} channel has: \n{:,d} subscribers \n{:,d} videos \nand {:,d} total video views.".format(user_name,int(subscribers),int(videos),int(views)) + CEND)


def replace(x):
    final_string = ""
    for c in x:
        if c == " ":
            final_string += "%20"
        else:
            final_string += c
    return final_string

if __name__ == "__main__":
    name = input("Enter channel name: ")
    get_data(name)
