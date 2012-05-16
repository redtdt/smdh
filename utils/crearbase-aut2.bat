c:
cd \smdh2\utils
set PGPASSWORD=%1
"%~3/bin/createdb" -Uadmin  -E=UTF8 %2
"%~3/bin/psql" -Uadmin  %2 <redtdtschema.sql
"%~3/bin/psql" -Uadmin  %2 <tesauro.sql



