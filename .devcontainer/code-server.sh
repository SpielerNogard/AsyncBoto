#######################################################
#! /bin/sh
# . /etc/rc.d/init.d/functions  # uncomment/modify for your killproc
case "$1" in
start)
echo "Starting code-server."
sudo nohup bash -c '/bin/code-server --auth none --port 8080 --bind-addr 0.0.0.0 --ignore-last-opened /workspaces/AsyncBoto &'
echo "code-server started."
;;
stop)
echo -n "Shutting down code-server."
killproc -TERM /bin/code-server
echo "code-server is stopped."
;;
*)
echo "Usage: $0 {start|stop}"
exit 1
esac
exit 0
#######################################################

