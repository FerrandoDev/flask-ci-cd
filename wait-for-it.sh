#!/usr/bin/env bash
host="$1"
shift
cmd="$@"

until mysqladmin ping -h "$host" --silent; do
  echo "Attente de la base de données..."
  sleep 2
done

exec $cmd
