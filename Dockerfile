FROM quay.io/jupyter/base-notebook:latest

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir ./pages
COPY /pages ./pages

WORKDIR /home/jovyan
USER jovyan

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["solara", "run", "./pages", "--host=0.0.0.0", "--port=8501"]