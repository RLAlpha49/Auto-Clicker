# Auto-Clicker

This is an auto-clicker I coded for myself to use for those classic idle/clicker games. You are able to set the auto-clicker's cps to anything between 1 and 1000.

DISCLAIMER: If you choose to set the CPS to a higher value than
my 1000 limit, then you need to get rid of the "cps = cps_speed()"
function in the main program. As well as take out the "cps"
parameter from the 'custom_event_loop' function. Lastly, you would 
need to switch the 'cps' variable in "time.sleep(cps)" to your
desired cps. Note that it needs to be in seconds. For example,
"0.001" for 1000 CPS and "0.0001" for 10000 CPS.

I Chose the limit of 1000 because, at some point, programs just
don't accept more clicks. Websites especially, lag or freeze a lot.
when going fast.
