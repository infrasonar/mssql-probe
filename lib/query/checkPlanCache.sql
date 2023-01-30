SET NOCOUNT ON;
DECLARE @TOTAL_PLAN_CACHE BIGINT, @SINGLE_USE_PLAN_CACHE BIGINT;
SELECT @TOTAL_PLAN_CACHE = SUM(CAST(cp_tot.size_in_bytes AS BIGINT))
FROM sys.dm_exec_cached_plans AS cp_tot
WHERE cp_tot.cacheobjtype = N'Compiled Plan';

SELECT @SINGLE_USE_PLAN_CACHE = SUM(CAST(cp_single.size_in_bytes AS BIGINT))
FROM sys.dm_exec_cached_plans AS cp_single
WHERE
    cp_single.cacheobjtype = N'Compiled Plan'
    AND cp_single.objtype IN (N'Adhoc', N'Prepared')
    AND cp_single.usecounts = 1;

SELECT
    'system' AS [name],
    @TOTAL_PLAN_CACHE AS total_plan_cache,
    @SINGLE_USE_PLAN_CACHE AS single_use_plan_cache,
    100.0 * CAST(@SINGLE_USE_PLAN_CACHE AS float) /
        CAST(@TOTAL_PLAN_CACHE AS float) AS plan_bloat