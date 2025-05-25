FROM python:3.12-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir ./pages
COPY /pages ./pages

# USER root
# RUN chown -R ${NB_UID} ${HOME}
# USER ${NB_USER}

EXPOSE 8765

HEALTHCHECK CMD curl --fail http://localhost:8765/_stcore/health

ENTRYPOINT ["solara", "run", "./pages", "--host=0.0.0.0"]