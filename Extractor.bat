@ECHO OFF
setlocal
set PYTHONPATH="signal-processor/winenv/Scripts"
pip install -r "./signal-processor/requirements.txt"
call python "data-extractor/crawler.py"
endlocal