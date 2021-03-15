@REM venv.cmd
@echo off
pushd “%~dp0”
set DJANGO_SETTINGS_MODULE=config.settings.local
.\venv\Scripts\activate
popd
@echo on