#/usr/bin/env sh

if [ "$1" = "manage" ]; then
    # Do not send the first argument to the management command
    shift

    # Run the Django management command
    DJANGO_SETTINGS_MODULE=coderdojo_portal.settings.production python /lib/coderdojo_portal/manage.py $@
else
    echo "[INFO] CoderDojo Portal is starting. Please wait..."

    # Run migrations
    echo "[INFO] Checking and running migrations..."
    DJANGO_SETTINGS_MODULE=coderdojo_portal.settings.production python /lib/coderdojo_portal/manage.py migrate || exit 1

    # Run Granian
    echo "[INFO] CoderDojo Portal is ready. Starting..."
    granian --interface wsgi --host 0.0.0.0 /lib/coderdojo_portal/coderdojo_portal/wsgi.py:application
fi
