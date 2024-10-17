@echo off
REM Delete all CSV files in the current directory (where this script is located)
del /q "*.csv"
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to clear CSV files in the current directory.
    exit /b %ERRORLEVEL%
)

REM Run Bashk.py and wait for it to complete
python Bashk.py >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Bashk.py failed to run.
    exit /b %ERRORLEVEL%
)

REM Wait for 1 second
timeout /t 1 /nobreak >nul

REM Run AclearAndOrganize.py and wait for it to complete
python AclearAndOrganize.py >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo AclearAndOrganize.py failed to run.
    exit /b %ERRORLEVEL%
)

REM Wait for 1 second
timeout /t 1 /nobreak >nul

REM Run BclearAndOrganize.py and wait for it to complete
python BclearAndOrganize.py >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo BclearAndOrganize.py failed to run.
    exit /b %ERRORLEVEL%
)

REM Wait for 1 second
timeout /t 1 /nobreak >nul

REM Run Merge.py and wait for it to complete
python Merge.py >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Merge.py failed to run.
    exit /b %ERRORLEVEL%
)

REM If everything ran successfully, exit with code 0
exit /b 0
