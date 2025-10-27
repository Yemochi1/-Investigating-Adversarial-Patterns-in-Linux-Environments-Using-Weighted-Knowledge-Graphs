# Authors: Jurema & Yemi

from datetime import timedelta

# format of our timestamp based on the audit_logs.csv
CUSTOM_DATE_FORMAT = "%b %d, %Y @ %H:%M:%S.%f"

# technique map
TECHNIQUE_MAP = {
    '/usr/bin/w': 'T1087',
    '/usr/bin/who': 'T1087',
    '/usr/bin/last': 'T1087',
    '/usr/bin/whoami': 'T1082',
    '/usr/bin/id': 'T1082',
    '/usr/bin/uname': 'T1082',
    '/usr/bin/pwd': 'T1082',
    '/usr/sbin/route': 'T1016',
    '/usr/bin/netstat': 'T1016',
    '/usr/sbin/arp': 'T1016',
    '/usr/bin/resolvectl': 'T1016',
    '/usr/bin/tar': 'T1074',
    '/usr/bin/zip': 'T1074',
    '/usr/bin/gzip': 'T1074'
}

# analysis time window
TIME_WINDOW = timedelta(minutes=10)
