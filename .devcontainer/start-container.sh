# Script to build and start the devcontainer. It also opens the selected editor.
# You need to have installed:
# - Docker https://docs.docker.com/engine/install/
# - devcontainer-cli https://github.com/devcontainers/cli/tree/main
# - vscli https://github.com/michidk/vscli (If you want to use Visual Studio Code)
# - Jetbrains Gateway https://plugins.jetbrains.com/plugin/14839-jetbrains-gateway (If you want to use PyCharm)
#
# Supported editors:
# - code: Visual Studio Code
# - pycharm: PyCharm
# - ssh: SSH
# - web: Web browser
#
# Usage:
# ./start-container.sh --editor <editor>
#

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory
cd "$SCRIPT_DIR" || exit

# Default editor
EDITOR="pycharm"

# Parse arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --editor) EDITOR="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Generate certificate
cd server
rm -f temp-ssh-key*
ssh-keygen -q -N '' -t rsa -f "$SCRIPT_DIR/server/temp-ssh-key"
cd ..

devcontainer up --workspace-folder .. --remove-existing-container --mount "type=bind,source=$(pwd)/server,target=/server"
# add pub key to SSH allow list
devcontainer exec --workspace-folder .. bash /server/init-ssh.sh

# Open the selected editor
if [ "$EDITOR" = "code" ]; then
    vscli open --command code .
elif [ "$EDITOR" = "pycharm" ]; then
    open 'jetbrains-gateway://connect#idePath=/opt/pycharm&projectPath=/workspaces/AsyncBoto&host=localhost&port=2222&user=vscode&type=ssh&deploy=false&newUi=true'
elif [ "$EDITOR" = "ssh" ]; then
  ssh -t -i "$SCRIPT_DIR/server/temp-ssh-key" -o NoHostAuthenticationForLocalhost=yes -o UserKnownHostsFile=/dev/null -o GlobalKnownHostsFile=/dev/null -p 2222 vscode@localhost exec bash
elif [ "$EDITOR" = "web" ]; then
    open 'http://localhost:8000'
else
    echo "Unsupported editor: $EDITOR"
    exit 1
fi