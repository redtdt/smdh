md dist
setup.py py2exe >salida.txt
psetup2.py py2exe
pause
copy dist\psetup.exe 
del dist\psetup.exe 
copy dist\MSVCR71.dll
del dist\MSVCR71.dll
del dist\w9xpopen.exe


copy bin\*.gif dist\bin
md dist\archivos
md dist\utils
md dist\config
copy tesauro\tesauro.csv dist\archivos
copy tesauro\tesauro.sql dist\utils
copy utils\*.* dist\utils
copy MSVCP71.DLL dist\bin
del dist\bin\SHFOLDER.dll
"%PROGRAMFILES%\NSIS\makensis.exe" instala
pause

