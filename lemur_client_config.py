prod_common = {
    "api_url": "https://lemur.leo-prod-common.lvg-tech.net/lemur/graphql",
    "headers": {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMjMiLCJyb2xlcyI6WyJST0xFX0dBTUVfV1JJVEUiXSwiaXNzIjoibGVtdXIiLCJleHAiOjE2NjgxNTgwMzksImlhdCI6MTY2ODA3MTYzOX0.ENINgc7mmY-rCqTWGmSl57jg7ORWoIE621QCqDLYcOxlWTXALBn_aitw_ezYpGD8dI0lI1xyy7k3ytCPpU76xQ",
        "Proxy-Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMjMiLCJyb2xlcyI6WyJST0xFX0dBTUVfV1JJVEUiXSwiaXNzIjoibGVtdXIiLCJleHAiOjE2NjgxNTgwMzksImlhdCI6MTY2ODA3MTYzOX0.ENINgc7mmY-rCqTWGmSl57jg7ORWoIE621QCqDLYcOxlWTXALBn_aitw_ezYpGD8dI0lI1xyy7k3ytCPpU76xQ",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "GCP_IAP_UID=105229053741336723510; _gcl_au=1.1.1457061543.1663932426; afUserId=ff1c59bf-1272-4174-bd37-09f65a769e4c-p; _hjSessionUser_380080=eyJpZCI6IjFjNTk5NTJlLTM5MjEtNTM4NS1iY2VkLTRlZDYxYmUxYjgxZiIsImNyZWF0ZWQiOjE2NjM5MzI0MjY0MDYsImV4aXN0aW5nIjp0cnVlfQ==; _clck=1w01bo5|1|f5a|0; __qca=P0-1933123741-1666080562800; _uetvid=aed505e0c79f11ec9e5ee3a058e8fd60; _ga=GA1.1.8b1cd8f0-5859-42c9-9b9f-f9dcd3bb9fc0; _ga_D9DRTT8FSJ=GS1.1.1667480683.18.0.1667480813.0.0.0; GCP_IAAP_AUTH_TOKEN_B3F1670B054BDB22=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY0NTEzNDVmYWQwODEwMWJmYjM0NWNmNjQyYTJkYTkyNjdiOWViZWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3NzA5Njc0NTUzNTItdDlyNzY1anVmMmtla2RqdWtuNnE4YWc0NzBvb3NoajIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI3NzA5Njc0NTUzNTItdDlyNzY1anVmMmtla2RqdWtuNnE4YWc0NzBvb3NoajIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDUyMjkwNTM3NDEzMzY3MjM1MTAiLCJoZCI6Imxlb3ZlZ2FzLmNvbSIsImVtYWlsIjoiZWR1YXJkLnJvbWFuaXVrQGxlb3ZlZ2FzLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiajZtVVhOV3Q1SXdHT3d0NnluMXZQUSIsImdvb2dsZSI6eyJnaWMiOiJBTG9PR0dBUVQ0TG40WmhwUDBXaktlYnZ6WjdjWjdkeFFhNTFsOFktRFpSVXQtUEN5LVpOLVpUcEpBejRlUTNhZk9PWHN5ZjRHSHFSaHVSOEhvSk05ZzlLa21nYlV0R0plQWlPemtLUWNqRmQ1bkZIZndrWkM1bUtpdVJaeU1vaXBjdWdoelF5Qk9naUI3X3JLTThPM2tRY2FYWWY3c0VrTy14SUxRZWY0eGd4TmlLa21jd2RwVW1yTkFNcE9NNXBjY285RkRSUUZqd1NScWk3VndVS2VkTm5RV2FxM3FhRy11ZzIifSwiaWF0IjoxNjY4MDY5NDI2LCJleHAiOjE2NjgwNzMwMjZ9.Jbox8H9jryfPsTHKUUGv8yvZdXmXHXmFOjkMaNBx3C7MWT-zm4qpYuGzwyxYYdYE9eNDOAfLOrbu33jZu9CFtABZ1YF148qtpUndhIMXNPr33vzAxP-8TE5TbC4jU7NLlQp9pf72-v2bX4dRoxsrtHOKxt79kdG20e8xCroWWF1x0JsGGr3o9DLqKXlbP0igs2Po1ViiGyxDHkjgoi5yurItgcJgEfqeKRxyeGWrEMRMCwFk5WrPOFK7gnXMzrer_JIrm0ZjJpv6g4mNT0GDPKHaah6xG1lqeMaWnrB2mJYWIt-3ZvBlWUZn3FVu2qAWahY7ApM_jHjSG3Ffx7OwLA; __Host-GCP_IAP_AUTH_TOKEN_B3F1670B054BDB22=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY0NTEzNDVmYWQwODEwMWJmYjM0NWNmNjQyYTJkYTkyNjdiOWViZWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3NzA5Njc0NTUzNTItdDlyNzY1anVmMmtla2RqdWtuNnE4YWc0NzBvb3NoajIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI3NzA5Njc0NTUzNTItdDlyNzY1anVmMmtla2RqdWtuNnE4YWc0NzBvb3NoajIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDUyMjkwNTM3NDEzMzY3MjM1MTAiLCJoZCI6Imxlb3ZlZ2FzLmNvbSIsImVtYWlsIjoiZWR1YXJkLnJvbWFuaXVrQGxlb3ZlZ2FzLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiajZtVVhOV3Q1SXdHT3d0NnluMXZQUSIsImdvb2dsZSI6eyJnaWMiOiJBTG9PR0dBUVQ0TG40WmhwUDBXaktlYnZ6WjdjWjdkeFFhNTFsOFktRFpSVXQtUEN5LVpOLVpUcEpBejRlUTNhZk9PWHN5ZjRHSHFSaHVSOEhvSk05ZzlLa21nYlV0R0plQWlPemtLUWNqRmQ1bkZIZndrWkM1bUtpdVJaeU1vaXBjdWdoelF5Qk9naUI3X3JLTThPM2tRY2FYWWY3c0VrTy14SUxRZWY0eGd4TmlLa21jd2RwVW1yTkFNcE9NNXBjY285RkRSUUZqd1NScWk3VndVS2VkTm5RV2FxM3FhRy11ZzIifSwiaWF0IjoxNjY4MDY5NDI2LCJleHAiOjE2NjgwNzMwMjZ9.Jbox8H9jryfPsTHKUUGv8yvZdXmXHXmFOjkMaNBx3C7MWT-zm4qpYuGzwyxYYdYE9eNDOAfLOrbu33jZu9CFtABZ1YF148qtpUndhIMXNPr33vzAxP-8TE5TbC4jU7NLlQp9pf72-v2bX4dRoxsrtHOKxt79kdG20e8xCroWWF1x0JsGGr3o9DLqKXlbP0igs2Po1ViiGyxDHkjgoi5yurItgcJgEfqeKRxyeGWrEMRMCwFk5WrPOFK7gnXMzrer_JIrm0ZjJpv6g4mNT0GDPKHaah6xG1lqeMaWnrB2mJYWIt-3ZvBlWUZn3FVu2qAWahY7ApM_jHjSG3Ffx7OwLA"
    }
}

dev_casino = {
    "api_url": "https://external-1.leo-dev-casino.lvg-tech.net/lemur/graphql",
    "headers": {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNyIsInJvbGVzIjpbIlJPTEVfQURNSU4iXSwiaXNzIjoibGVtdXIiLCJleHAiOjE2NjgxNTUxMzUsImlhdCI6MTY2ODA2ODczNX0.x3Gp4-t608njLbZdI8dDJ6Dl8sJCFRKwDTuTRvDSuLuZ2d8_J5HspYyRfY_gXthKQ_QyKl8EQy7zUtTg7p7Fdw"
    }
}

localhost = {
    "api_url": "http://localhost:8080/lemur/graphql",
    "headers": dev_casino["headers"]
}
