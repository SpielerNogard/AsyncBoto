# Generate certificate
cd server
rm -f temp-ssh-key*
ssh-keygen -q -N '' -t rsa -f temp-ssh-key
cd ..

devcontainer up --workspace-folder .. --remove-existing-container --mount "type=bind,source=$(pwd)/server,target=/server"
# add pub key to SSH allow list
devcontainer exec --workspace-folder .. bash /server/init-ssh.sh


# Connect
#ssh -t -i server/temp-ssh-key -o NoHostAuthenticationForLocalhost=yes -o UserKnownHostsFile=/dev/null -o GlobalKnownHostsFile=/dev/null -p 2222 vscode@localhost exec bash
#open /Users/spielernogard/Applications/Gateway.app --ssh --host localhost --port 2222 --user vscode --private-key server/temp-ssh-key
open 'jetbrains-gateway://connect#idePath=/opt/pycharm&projectPath=/workspaces/AsyncBoto&host=localhost&port=2222&user=vscode&type=ssh&deploy=false&newUi=true'