try:
    import django
    from django.db import models

    print("Django version:", django.get_version())
    print("Import successful")
except ImportError as e:
    print("Error importing Django:", e)
