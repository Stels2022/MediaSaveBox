from enum import Enum


class DownloadStatus(Enum):
    RECEIVED = "received"
    DETECTING = "detecting"
    DOWNLOADING = "downloading"
    SENDING = "sending"
    DONE = "done"
    ERROR = "error"