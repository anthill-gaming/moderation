#!/usr/bin/env bash

# Setup postgres database
createuser -d anthill_moderation -U postgres
createdb -U anthill_moderation anthill_moderation