"""Default configuration

Use env var to override
"""
import os

SERVER_NAME = os.getenv("SERVER_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")
# URL scheme to use outside of request context
PREFERRED_URL_SCHEME = os.getenv("PREFERRED_URL_SCHEME", "http")

BACKING_FHIR_URL = os.getenv("BACKING_FHIR_URL ", "http://hapi:8080/hapi-fhir-jpaserver/fhir")
