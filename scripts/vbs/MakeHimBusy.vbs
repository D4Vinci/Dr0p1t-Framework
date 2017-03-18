Set WshShell = WScript.CreateObject("WScript.Shell")
Do While 1 < 100
	WshShell.SendKeys "abc"
	WshShell.SendKeys "{ENTER}"
	WshShell.SendKeys "dfg"
Loop