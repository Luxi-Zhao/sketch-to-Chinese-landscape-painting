@echo off

python fid_score.py "./A" "./B" ^
    --batch-size 1 ^
    --dims 2048

pause
