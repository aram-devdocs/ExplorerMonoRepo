#!/bin/bash

if [[ "$1" == "migrate" && ("$2" != "--name" || -z "$3") ]]; then
    echo "Error: Migration name is required. Use: ./migrate.sh migrate --name \"Your description\""
    exit 1
fi

COMMAND=$1
MIGRATION_NAME=$3

echo "You are about to run \"$COMMAND\"."
if [[ "$COMMAND" == "migrate" ]]; then
    echo "Migration description: \"$MIGRATION_NAME\""
fi
read -p "Do you want to proceed? (y/n): " CONFIRM

if [[ "$CONFIRM" != "y" ]]; then
    echo "Operation cancelled."
    exit 0
fi

case $COMMAND in
"migrate")
    flask db migrate -m "$MIGRATION_NAME"
    ;;
"upgrade")
    flask db upgrade
    ;;
"downgrade")
    flask db downgrade
    ;;
*)
    echo "Usage: ./migrate.sh {migrate --name \"desc\"|upgrade|downgrade}"
    ;;
esac
