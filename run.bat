@ECHO OFF
setlocal
set PYTHONPATH="signal-processor/winenv/Scripts"
pip install -r "./signal-processor/requirements.txt"
start "" call API.bat
start "" call Extractor.bat
start "" call Analyzer.bat
endlocal