FROM golang:1.22.3-bullseye as builder

WORKDIR /app

COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . .

FROM builder as final

RUN --mount=type=cache,target="/root/.cache/go-build" go build -o bin .

CMD ["/app/bin"]