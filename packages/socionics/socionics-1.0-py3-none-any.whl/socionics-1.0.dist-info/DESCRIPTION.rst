[EN] Python3 socionics module

[RUS] Соционический модуль для python3

Usage:

	db = Sociodb()

	a = Stype("INTP")

	b = Stype("INFJ")

	print(a.quad())

	print(a.name(1))

	print(db.otn[a+b])

	a.set("INFJ")

	print(db.otn[a+"ISFJ"])


