from dateutil.parser import parse


class Video:

    def __init__(self, video_dict):
        """
        Parses the json data given by Google Takeout into a Video
        object.

        :param video_dict: The dict for a watched video
        """
        self.title = video_dict.get("title")
        self.url = video_dict.get("titleUrl")
        time_str = video_dict.get("time")
        self.time = parse(time_str) if time_str else None
        sub_info = video_dict.get("subtitles")
        self.channel_name = sub_info[0].get("name") if sub_info else "Unknown"
        self.channel_url = sub_info[0].get("url") if sub_info else "Unknown"

    def __repr__(self):
        return f'{self.title} by @{self.channel_name}'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.url == other.url
    
    def __hash__(self):
        return hash(self.url)


class VideoByChannel(Video):
    def __eq__(self, other):
        return self.channel_url == other.channel_url

    def __hash__(self):
        return hash(self.channel_url if self.channel_url is not "Unknown" else self.url)