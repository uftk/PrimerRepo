FROM python:3.8-slim

WORKDIR /app

# Instalación manual de .NET SDK
RUN apt-get update && \
    apt-get install -y wget ca-certificates apt-transport-https && \
    wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y dotnet-sdk-8.0 && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN dotnet restore

RUN dotnet publish -c Release -o out

EXPOSE 8080

CMD ["dotnet", "out/HelloWorld.dll"]