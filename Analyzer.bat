if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
@ECHO OFF
setlocal
cd "signal-processor"
pip install -r "./requirements.txt"
cd "analyzer"
python -c "import os, sys; print(os.path.dirname(sys.executable))"
call python "../api/main.py"
endlocal