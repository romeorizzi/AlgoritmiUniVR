# Launch Google Chrome with specified URLs
Start-Process "chrome.exe" -ArgumentList "--new-window","https://wbo.ophir.dev/boards/algo$((Get-Date).ToString('yyyy-MM-dd'))_1"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/algo_meetings$((Get-Date).ToString('yyyy'))"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/algo$((Get-Date).ToString('yyyy-MM-dd'))"
Start-Process "chrome.exe" -ArgumentList "https://univr.zoom.us/j/94457731757"

# Display URLs
Write-Host "URLs:"
Write-Host " - Zoom algo Room: https://univr.zoom.us/j/94457731757"
Write-Host "Etherpad algo index page: https://etherpad.wikimedia.org/p/algo_meetings$((Get-Date).ToString('yyyy'))"
Write-Host " - Etherpad meeting report: https://etherpad.wikimedia.org/p/algo$((Get-Date).ToString('yyyy-MM-dd'))"
Write-Host " - Collaborative WhiteBoard: https://wbo.ophir.dev/boards/algo$((Get-Date).ToString('yyyy-MM-dd'))_1"
