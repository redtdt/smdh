c:
cd \smdh2\utils
set PGPASSWORD=%1
"%PROGRAMFILES%/PostgreSQL/8.3/bin/createdb" -Uadmin  -E=UTF8 redtdt
"%PROGRAMFILES%/PostgreSQL/8.3/bin/psql" -Uadmin  redtdt <redtdtschema.sql
"%PROGRAMFILES%/PostgreSQL/8.3/bin/psql" -Uadmin  redtdt <tesauro.sql


