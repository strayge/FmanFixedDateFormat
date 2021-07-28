from PyQt5.QtCore import QDateTime
import core


def get_str(self, url):
    try:
        mtime = self._get_mtime(url)
    except OSError:
        return ''
    if mtime is None:
        return ''
    try:
        timestamp = mtime.timestamp()
    except OSError:
        return ''
    mtime_qt = QDateTime.fromMSecsSinceEpoch(int(timestamp * 1000))
    time_format = 'yyyy-MM-dd HH:mm'
    return mtime_qt.toString(time_format)


core.Modified.get_str = get_str
