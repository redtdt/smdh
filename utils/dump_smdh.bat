
c:
cd "%~4"
cd bin
set PGPASSWORD=%3
pg_dump -Uadmin  --create -i --no-privileges -E=UTF8 %2 > %1


