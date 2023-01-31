WITH grouped AS (
	SELECT
		machine_name,
		server_name,
		database_name,
		MAX(backup_finish_date) AS finish_date
	FROM
		msdb.dbo.backupset
	WHERE
		[type] = 'D'
	GROUP BY
		machine_name,
		server_name,
		database_name
)
SELECT
	bs.machine_name,
	bs.server_name,
	bs.database_name,
	bs.recovery_model,
	bs.backup_size,
	bs.compressed_backup_size,
	CONVERT(NUMERIC (20,2), (CONVERT(FLOAT, bs.backup_size) / CONVERT(FLOAT, bs.compressed_backup_size))) AS [compression_ratio],
	bs.has_backup_checksums,
	bs.is_copy_only,
	bs.backup_start_date,
	bs.backup_finish_date,
	DATEDIFF(SECOND, bs.backup_start_date, bs.backup_finish_date) AS [backup_elapsed_time_sec],
	DATEDIFF(SECOND, bs.backup_finish_date, CURRENT_TIMESTAMP) AS [last_backup_age],
	DATEDIFF(SECOND, '1970-01-01 00:00:00', bs.backup_finish_date) AS [last_backup_date]
FROM
	grouped
INNER JOIN
	msdb.dbo.backupset as bs
ON grouped.finish_date = bs.backup_finish_date