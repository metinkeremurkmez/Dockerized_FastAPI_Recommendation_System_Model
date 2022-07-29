# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./Pipfile /code/Pipfile

COPY ./model_iLab_case.pkl /code/model_iLab_case.pkl

#
RUN pip install pipenv 
RUN pipenv install

# 
COPY ./reco /code/reco

# 
CMD ["pipenv", "run", "uvicorn", "reco.api:app", "--host", "0.0.0.0", "--port", "80", "--reload"]