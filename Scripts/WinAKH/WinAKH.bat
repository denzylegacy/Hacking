@echo off
for /f "tokens=2 delims==" %%a in ('wmic path softwarelicensingservice get OA3xOriginalProductKey /value ^| find "="') do set "chave=%%a"
echo %chave% > key.txt
