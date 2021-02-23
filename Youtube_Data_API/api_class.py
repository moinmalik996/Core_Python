class YTStatistics:
    
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        
    def channel_statistics(self):
        url = f"https://developers.google.com/youtube/v3/guides/implementation/channels#channels-list"
        