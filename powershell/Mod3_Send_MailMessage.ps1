function getIP {
(Get-NetIPAddress).ipv4address | Select-String "192*"
}

function hostName {
$HOST.Version.Major
}

function getDate {
Get-Date -UFormat "%A, %B %d, %Y"
}

$getIP = getIP
$hostName = hostName
$getDate = getDate

$BODY = "This machine's IP is $getIP. User is $env:USERNAME. Host-name is $env:COMPUTERNAME. Powershell Version $hostName. Today's date is $getDate."

echo $BODY > mod3_output.txt