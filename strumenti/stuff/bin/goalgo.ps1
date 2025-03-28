# Launch Google Chrome with specified URLs
Start-Process "chrome.exe" -ArgumentList "--new-window","https://univr.zoom.us/j/94457731757"
Start-Process "chrome.exe" -ArgumentList "https://rizzi.olinfo.it/algo"
Start-Process "chrome.exe" -ArgumentList "https://wbo.ophir.dev/boards/LavagnaALGO$((Get-Date).ToString('yyyy-MM-dd'))_1"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/Algoritmi$((Get-Date).ToString('yyyy'))_indice_incontri"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/Algoritmi$((Get-Date).ToString('yyyy-MM-dd'))"

# Display URLs
Write-Host "Zoom Room ALGO URL: https://univr.zoom.us/j/94457731757"
Write-Host "CMS algo URL: https://rizzi.olinfo.it/algo"
Write-Host "Collaborative WhiteBoard(easy) URL: https://wbo.ophir.dev/boards/LavagnaALGO$((Get-Date).ToString('yyyy-MM-dd'))"
Write-Host "Collaborative URL: https://etherpad.wikimedia.org/p/Algoritmi$((Get-Date).ToString('yyyy-MM-dd'))"
