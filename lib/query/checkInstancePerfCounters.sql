SELECT [counter_name], [cntr_value]
FROM sys.dm_os_performance_counters
WHERE
    (counter_name = 'Batch Requests/sec' AND object_name
        LIKE '%SQL Statistics%') OR
    (counter_name = 'SQL Compilations/sec' AND object_name
        LIKE '%SQL Statistics%') OR
    (counter_name = 'SQL Re-Compilations/sec' AND object_name
        LIKE '%SQL Statistics%') OR
    (counter_name = 'Lock Waits/sec' AND instance_name = '_Total'
        AND object_name LIKE '%Locks%') OR
    (counter_name = 'Page Splits/sec' AND object_name
        LIKE '%Access Methods%') OR
    (counter_name = 'Processes blocked' AND object_name
        LIKE '%General Statistics%') OR
    (counter_name = 'Query optimizations/sec' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Workload Group Stats%') OR
    (counter_name = 'Suboptimal plans/sec' AND object_name
        LIKE '%SQLServer:Workload Group Stats%') OR
    (counter_name = 'Stored Procedures Invoked/sec'
        AND instance_name = '_Total' AND object_name
        LIKE '%SQLServer:Broker Activation%') OR
    (counter_name = 'Full Scans/sec' AND object_name
        LIKE '%SQLServer:Access Methods%') OR
    (counter_name = 'Range Scans/sec' AND object_name
        LIKE '%SQLServer:Access Methods%') OR
    (counter_name = 'Probe Scans/sec' AND object_name
        LIKE '%SQLServer:Access Methods%') OR
    (counter_name = 'Index Searches/sec' AND object_name
        LIKE '%SQLServer:Access Methods%') OR
    (counter_name = 'Pages Allocated/sec' AND object_name
        LIKE '%SQLServer:Access Methods%') OR
    (counter_name = 'Page Deallocations/sec' AND object_name
        LIKE '%SQLServer:Access Methods%') OR
    (counter_name = 'Table Lock Escalations/sec' AND object_name
        LIKE '%SQLServer:Access Methods%') OR
    (counter_name = 'Lock Requests/sec' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Lock Timeouts/sec' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Number of Deadlocks/sec' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Lock Waits/sec' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Lock Wait Time (ms)' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Average Wait Time (ms)' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Average Wait Time Base' AND instance_name = '_Total'
        AND object_name LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Lock Timeouts (timeout > 0)/sec'
        AND instance_name = '_Total' AND object_name
        LIKE '%SQLServer:Locks%') OR
    (counter_name = 'Active Temp Tables' AND object_name
        LIKE '%SQLServer:General Statistics%') OR
    (counter_name = 'Temp Tables Creation Rate' AND object_name
        LIKE '%SQLServer:General Statistics%') OR
    (counter_name = 'Logins/sec' AND object_name
        LIKE '%SQLServer:General Statistics%') OR
    (counter_name = 'Connection Reset/sec' AND object_name
        LIKE '%SQLServer:General Statistics%') OR
    (counter_name = 'Logouts/sec' AND object_name
        LIKE '%SQLServer:General Statistics%') OR
    (counter_name = 'Update conflict ratio' AND object_name
        LIKE '%SQLServer:Transactions%') OR
    (counter_name = 'Update conflict ratio base' AND object_name
        LIKE '%SQLServer:Transactions%') OR
    (counter_name = 'Checkpoint Pages/sec' AND object_name
        LIKE '%Buffer Manager%') OR
    (counter_name = 'Buffer cache hit ratio' AND object_name
        LIKE '%Buffer Manager%') OR
    (counter_name = 'Buffer cache hit ratio base' AND object_name
        LIKE '%Buffer Manager%') OR
    (counter_name = 'Page writes/sec' AND object_name
        LIKE '%Buffer Manager%') OR
    (counter_name = 'Page reads/sec' AND object_name
        LIKE '%Buffer Manager%') OR
    (counter_name = 'Readahead pages/sec' AND object_name
        LIKE '%Buffer Manager%')