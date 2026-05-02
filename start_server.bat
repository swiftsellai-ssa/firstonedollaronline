@echo off
echo Starting Local Server for First$1online...
echo.
echo Open your browser to: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server.
echo.
python -m http.server 8000
pause
