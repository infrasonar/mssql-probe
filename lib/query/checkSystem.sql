SELECT
    SERVERPROPERTY('MachineName') AS [machine_name],
    SERVERPROPERTY('ServerName') AS [server_name],
    SERVERPROPERTY('ServerName') AS [name],
    SERVERPROPERTY('InstanceName') AS [instance_name],
    SERVERPROPERTY('IsClustered') AS [is_clustered],
    SERVERPROPERTY('ComputerNamePhysicalNetBIOS') AS [computer_name_physical_netbios],
    SERVERPROPERTY('Edition') AS [edition],
    SERVERPROPERTY('ProductLevel') AS [product_level],				-- What servicing branch (RTM/SP/CU)
    SERVERPROPERTY('ProductUpdateLevel') AS [product_update_level],	-- Within a servicing branch, what CU# is applied
    SERVERPROPERTY('ProductVersion') AS [product_version],
    SERVERPROPERTY('ProductMajorVersion') AS [product_major_version],
    SERVERPROPERTY('ProductMinorVersion') AS [product_minor_version],
    SERVERPROPERTY('ProductBuild') AS [product_build],
    SERVERPROPERTY('ProductBuildType') AS [product_build_type],		      -- Is this a GDR or OD hotfix (NULL if on a CU build)
    SERVERPROPERTY('ProductUpdateReference') AS [product_update_reference], -- KB article number that is applicable for this build
    SERVERPROPERTY('ProcessID') AS [process_id],
    SERVERPROPERTY('Collation') AS [collation],
    SERVERPROPERTY('IsFullTextInstalled') AS [is_full_text_installed],
    SERVERPROPERTY('IsIntegratedSecurityOnly') AS [is_integrated_security_only],
    SERVERPROPERTY('FilestreamConfiguredLevel') AS [filestream_configured_level],
    SERVERPROPERTY('IsHadrEnabled') AS [is_hadr_enabled],
    SERVERPROPERTY('HadrManagerStatus') AS [hadr_manager_status],
    SERVERPROPERTY('InstanceDefaultDataPath') AS [instance_default_data_path],
    SERVERPROPERTY('InstanceDefaultLogPath') AS [instance_default_log_path],
    SERVERPROPERTY('BuildClrVersion') AS [build_clr_version],
    windows_release,
    windows_service_pack_level,
    windows_sku,
    os_language_version
FROM sys.dm_os_windows_info WITH (NOLOCK) OPTION (RECOMPILE);