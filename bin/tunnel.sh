#!/bin/zsh
BASEDIR=$(dirname "$0")
. ~/.zshrc
. $BASEDIR/../.env
curl -i http://localhost:$METABASE_PORT > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Opening tunnel to metabasse at localhost:$METABASE_PORT"
  aws-role pro
  kubectl port-forward -n metabase svc/metabase $METABASE_PORT:80 &
fi