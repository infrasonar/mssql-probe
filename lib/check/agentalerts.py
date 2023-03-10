from libprobe.asset import Asset
from ..mssql_query import get_data

QUERY = open('lib/query/checkAgentAlerts.sql').read()
INFO_LK = {
    0: 'Informational message',
    1: 'Informational message',
    2: 'Informational message',
    3: 'Informational message',
    4: 'Informational message',
    5: 'Informational message',
    6: 'Informational message',
    7: 'Informational message',
    8: 'Informational message',
    9: 'Informational message',
    10: 'Informational message for compatibility reasons.',
    11: 'Indicates that the given object or entity does not exist.',
    12: ('A special severity for queries that do not use locking because of'
         ' special query hints. In some cases, read operations performed by'
         ' these statements could result in inconsistent data, since locks are'
         ' not taken to guarantee consistency.'),
    13: 'Indicates transaction deadlock errors',
    14: 'Indicates security-related errors, such as permission denied',
    15: 'Indicates syntax errors in the Transact-SQL command',
    16: 'Indicates general errors that can be corrected by the user',
    17: ('Indicates that the statement caused SQL Server to run out of'
         ' resources (such as memory, locks, or disk space for the database)'
         ' or to exceed some limit set by the system administrator'),
    18: ('Indicates a problem in the Database Engine software, but the'
         ' statement completes execution, and the connection to the instance'
         ' of the Database Engine is maintained. The system administrator'
         ' should be informed every time a message with a severity level of 18'
         ' occurs.'),
    19: ('Indicates that a nonconfigurable Database Engine limit has been'
         ' exceeded and the current batch process has been terminated. Error'
         ' messages with a severity level of 19 or higher stop the execution'
         ' of the current batch. Severity level 19 errors are rare and must be'
         ' corrected by the system administrator or your primary support'
         ' provider. Contact your system administrator when a message with a'
         ' severity level 19 is raised. Error messages with a severity level'
         ' from 19 through 25 are written to the error log.'),
    20: ('Indicates that a statement has encountered a problem. Because the'
         ' problem has affected only the current task, it is unlikely that the'
         ' database itself has been damaged.'),
    21: ('Indicates that a problem has been encountered that affects all tasks'
         ' in the current database, but it is unlikely that the database'
         ' itself has been damaged.'),
    22: ('Indicates that the table or index specified in the message has been'
         ' damaged by a software or hardware problem.\n\nSeverity level 22'
         ' errors occur rarely. If one occurs, run DBCC CHECKDB to determine'
         ' whether other objects in the database are also damaged. The'
         ' problem might be in the buffer cache only and not on the disk'
         ' itself. If so, restarting the instance of the Database Engine'
         ' corrects the problem. To continue working, you must reconnect to'
         ' the instance of the Database Engine; otherwise, use DBCC to repair'
         ' the problem. In some cases, you may have to restore the database.\n'
         ' If restarting the instance of the Database Engine does not correct'
         ' the problem, then the problem is on the disk. Sometimes destroying'
         ' the object specified in the error message can solve the problem.'
         ' For example, if the message reports that the instance of the'
         ' Database Engine has found a row with a length of 0 in a'
         ' nonclustered index, delete the index and rebuild it.'),
    23: ('Indicates that the integrity of the entire database is in question'
         ' because of a hardware or software problem\n\nSeverity level 23'
         ' errors occur rarely. If one occurs, run DBCC CHECKDB to determine'
         ' the extent of the damage. The problem might be in the cache only'
         ' and not on the disk itself. If so, restarting the instance of the'
         ' Database Engine corrects the problem. To continue working, you must'
         ' reconnect to the instance of the Database Engine; otherwise, use'
         ' DBCC to repair the problem. In some cases, you may have to restore'
         ' the database.'),
    24: ('Indicates a media failure. The system administrator may have to'
         ' restore the database. You may also have to call your hardware'
         ' vendor.'),
}
SEVERITY_LK = {
    0: 'Informational',
    1: 'Informational',
    2: 'Informational',
    3: 'Informational',
    4: 'Informational',
    5: 'Informational',
    6: 'Informational',
    7: 'Informational',
    8: 'Informational',
    9: 'Informational',
    10: 'Informational',
    11: 'Warning',
    12: 'Warning',
    13: 'Warning',
    14: 'Warning',
    15: 'Warning',
    16: 'Warning',
    17: 'Error',
    18: 'Error',
    19: 'Error',
    20: 'Critical',
    21: 'Critical',
    22: 'Critical',
    23: 'Critical',
    24: 'Emergency',
}


async def check_agentalerts(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:

    res = await get_data(asset, asset_config, config, QUERY)
    for item in res:
        severity = item.get('severity')
        if severity is not None:
            item['alert_info'] = INFO_LK.get(severity)
            item['syslog_severity'] = SEVERITY_LK.get(severity)
    return {
        'agentalerts': res,
    }
