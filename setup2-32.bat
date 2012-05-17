net user postgres /delete

postgresql-9.0.1-1-windows --mode unattended --superaccount admin --servicepassword xyz   --serverport 5432 --datadir %2:\smdh_datos --superpassword %1 