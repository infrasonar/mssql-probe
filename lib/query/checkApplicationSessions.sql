SET NOCOUNT ON;
IF OBJECT_ID('tempdb..#tmpwho2') IS NOT NULL
    DROP TABLE #tmpwho2;
CREATE TABLE #tmpwho2 (
    SPID INT,
    Status VARCHAR(MAX),
    login VARCHAR(MAX),
    HostName VARCHAR(MAX),
    BlkBy VARCHAR(MAX),
    database_name VARCHAR(MAX),
    command VARCHAR(MAX),
    cpu_time INT,
    disk_io INT,
    last_batch VARCHAR(MAX),
    ProgramName VARCHAR(MAX),
    spid_1 INT,
    request_id INT
)
INSERT INTO #tmpwho2 EXEC sp_who2;

SELECT
    SPID AS [name],
    RTRIM(Status) AS [status],
    login,
    RTRIM(HostName) AS [host_name],
    LTRIM(RTRIM(BlkBy)) AS [blk_by],
    database_name AS [database_name],
    command as [command],
    CONVERT(FLOAT, cpu_time / 1000000.0) AS [cpu_time],
    disk_io,
    last_batch,
    LTRIM(RTRIM(ProgramName)) AS program_name,
    spid_1,
    request_id
FROM
    #tmpwho2
WHERE
    ProgramName is not NULL
    AND len(rtrim(ltrim(ProgramName))) > 0;

DROP TABLE #tmpwho2;