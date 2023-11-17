# Get the base path of the script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$basePath = (Get-Item $scriptPath).FullName

# Define the path to the .gitignore file
$gitIgnorePath = Join-Path $basePath ".gitignore"

# Check if the PSTree module is installed
if (-not (Get-Module -ListAvailable -Name PSTree)) {
  # Install the PSTree module if it's not installed
  Install-Module -Name PSTree -Scope CurrentUser -Force -AllowClobber
}

# Check if the .gitignore file exists
if (Test-Path $gitIgnorePath -PathType Leaf) {
  # Read the patterns from the .gitignore file and split into an array
  $excludePatterns = Get-Content $gitIgnorePath -ErrorAction SilentlyContinue | ForEach-Object { "$basePath\$_" }

  # Import the PSTree module
  Import-Module PSTree

  (Get-PSTree -Recurse -Exclude $excludePatterns).Hierarchy

}
else {
  Write-Host "No .gitignore file found."

  # Import the PSTree module without exclusion
  Import-Module PSTree
  Get-PSTree
}
