SELECT
    counter_name,
    cntr_value,
    LTRIM(RTRIM(instance_name)) AS instance_name
FROM
    sys.dm_os_performance_counters
WHERE
    (counter_name = 'Cache Hit Ratio' AND object_name
        LIKE '%:Catalog Metadata%') OR
    (counter_name = 'Cache Hit Ratio Base' AND object_name
        LIKE '%:Catalog Metadata%') OR
    (counter_name = 'Cache Entries Count' AND object_name
        LIKE '%:Catalog Metadata%') OR
    (counter_name = 'Cache Entries Pinned Count' AND object_name
        LIKE '%:Catalog Metadata%') OR
    (counter_name = 'Write Transactions/sec' AND object_name
        LIKE '%:Databases%') OR
    (counter_name = 'Log Flushes/sec' AND object_name
        LIKE '%:Databases%') OR
    (counter_name = 'Log Bytes Flushed/sec' AND object_name
        LIKE '%:Databases%') OR
    (counter_name = 'Log Flush Waits/sec' AND object_name
        LIKE '%:Databases%') OR
    (counter_name = 'Transactions/sec' AND object_name
        LIKE '%:Databases%')