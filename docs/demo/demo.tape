# Re-record the README demo from the repo root:
#
#   export KUBECONFIG="$PWD/demo-kubeconfig.yaml" CLUSTER=kube-tui-demo
#   bash scripts/dev-cluster.sh && bash scripts/dev-metrics.sh
#   kubectl apply -f docs/demo/workloads.yaml
#   kubectl config rename-context kind-kube-tui-demo staging-eu
#   cargo build --release --locked
#   sleep 180   # let settlement-worker rack up a few restarts
#   vhs docs/demo/demo.tape
#
# VHS cannot send function keys, so Focus studio is opened with :browse.

Output "docs/images/demo.gif"

Set Shell "bash"
Set Width 1440
Set Height 860
Set FontSize 15
Set Padding 16
Set TypingSpeed 55ms
Set Framerate 24
Env KUBECONFIG "demo-kubeconfig.yaml"
Env PS1 "$ "

Hide
Type "export PATH=$PWD/target/release:$PATH; clear" Enter
Show

Type "kubrick -A" Sleep 400ms Enter
Sleep 5s

Type "2" Sleep 2s
Type "t" Sleep 4s
Escape Sleep 1s
Type "0" Sleep 1s

Type "/" Sleep 300ms
Type "label:app=payments ready=true" Sleep 700ms Enter
Sleep 2s
Escape Sleep 500ms
Enter Sleep 2s
Type "4" Sleep 6s
Escape Sleep 1s

Type ":" Sleep 500ms
Type "browse" Sleep 600ms Enter
Sleep 3s
Sleep 1s

Ctrl+C Sleep 1s
