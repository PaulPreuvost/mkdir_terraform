echo "START INSTALL NOMAD"

curl -L -o nomad.zip "https://releases.hashicorp.com/nomad/1.8.2/nomad_1.8.2_linux_amd64.zip"
sudo unzip nomad.zip -d /usr/local/bin
sudo chmod +x /usr/local/bin/nomad

nomad --version

echo "NOMAD INSTALLATION COMPLETED"