{%- if cookiecutter.include_dockerfile == 'yes' %}
# Build stage
FROM golang:1.25.5-trixie AS build

WORKDIR /build

COPY go.mod ./
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o {{ cookiecutter.project_name }} .

# Runtime stage
FROM chainguard/wolfi-base:latest

USER nonroot
WORKDIR /app

RUN chown -R nonroot:nonroot /app/
COPY --from=build --chown=nonroot:nonroot /build/{{ cookiecutter.project_name }} .

ENTRYPOINT ["./{{ cookiecutter.project_name }}"]
CMD [ "" ]

{%- endif %}
