-- was unable to test
IF OBJECT_ID('tempdb..#IOWarningResults') IS NOT NULL
    DROP TABLE #IOWarningResults;
CREATE TABLE #IOWarningResults(LogDate datetime, ProcessInfo sysname, LogText nvarchar(1000));

	INSERT INTO #IOWarningResults
	EXEC xp_readerrorlog 0, 1, N'taking longer than 15 seconds';

	INSERT INTO #IOWarningResults
	EXEC xp_readerrorlog 1, 1, N'taking longer than 15 seconds';

	INSERT INTO #IOWarningResults
	EXEC xp_readerrorlog 2, 1, N'taking longer than 15 seconds';

	INSERT INTO #IOWarningResults
	EXEC xp_readerrorlog 3, 1, N'taking longer than 15 seconds';

	INSERT INTO #IOWarningResults
	EXEC xp_readerrorlog 4, 1, N'taking longer than 15 seconds';

SELECT top(100) LogDate, ProcessInfo, LogText
FROM #IOWarningResults;

DROP TABLE #IOWarningResults;