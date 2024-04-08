if not exist "MySQL Server" (
	mkdir "MySQL Server"
	tar -xf "MySQL Server.zip" -C "./MySQL Server"
)

cd MySQL Server/bin

mysqld --defaults-file="../my.ini"
