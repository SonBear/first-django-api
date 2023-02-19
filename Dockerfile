FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
EXPOSE 8000 
RUN python -m pip install Django
COPY . .
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]