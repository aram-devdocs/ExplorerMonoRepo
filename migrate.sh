#!/bin/bash

if [[ "$1" == "migrate" && ("$2" != "--name" || -z "$3") ]]; then
    echo "Error: Migration name is required. Use: ./migrate.sh migrate --name \"Your description\""
    exit 1
fi

COMMAND=$1
MIGRATION_NAME=$3

# if -h or --help is provided, show usage
if [[ "$COMMAND" == "-h" || "$COMMAND" == "--help" ]]; then
    echo "Usage: ./migrate.sh {migrate --name \"desc\"|upgrade|downgrade}"
    exit 0
fi

# if command is 'migrate' and no name is provided, throw error
if [[ "$COMMAND" == "migrate" && -z "$MIGRATION_NAME" ]]; then
    echo "Error: Migration name is required. Use: ./migrate.sh migrate --name \"Your description\""
    exit 1
fi

# if command is not 'migrate', 'upgrade', or 'downgrade', throw error
if [[ "$COMMAND" != "migrate" && "$COMMAND" != "upgrade" && "$COMMAND" != "downgrade" ]]; then
    echo "Error: Invalid command. Use: ./migrate.sh {migrate --name \"desc\"|upgrade|downgrade}"
    exit 1
fi

# if no command is provided, throw error
if [[ -z "$COMMAND" ]]; then
    echo "Error: No command provided. Use: ./migrate.sh {migrate --name \"desc\"|upgrade|downgrade}"
    exit 1
fi

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
    flask --app apps/flask_api db migrate -m "$MIGRATION_NAME"
    ;;
"upgrade")
    flask --app apps/flask_api db upgrade
    ;;
"downgrade")
    flask --app apps/flask_api db downgrade
    ;;
*)
    echo "Usage: ./migrate.sh {migrate --name \"desc\"|upgrade|downgrade}"
    ;;
esac
