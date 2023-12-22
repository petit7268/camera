from filestack import Client


class FileSharer:
    """
    used for sharing files from the result of the report class
    return url of the file
    """

    def __init__(self, filepath, api_key='AgPcHHKYQRx2tuJtmSypnz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
