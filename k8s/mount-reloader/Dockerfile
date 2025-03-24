FROM golang:1.24.0 AS builder

WORKDIR /workspace
COPY app .
RUN go build -o watcher /workspace/main.go

FROM debian:stable-slim
WORKDIR /workspace
COPY --from=builder /workspace/watcher .

ENTRYPOINT ["/workspace/watcher"]
