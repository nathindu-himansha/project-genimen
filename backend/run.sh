#!/bin/bash
export FLASK_APP="api:create_app('prod')"
export FLASK_ENV=development
flask run
