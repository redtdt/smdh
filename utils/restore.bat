
c:
cd "%~3"
cd bin
set PGPASSWORD=%2
psql -Uadmin  postgres < %1
