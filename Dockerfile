FROM postgres:alpine

RUN POSTGRES_PASSWORD=root -d -p 5432:5432 postgres:alpine