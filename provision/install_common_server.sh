echo "--------------------------------------------------------"
echo "START INSTALL COMMON SERVER SETTINGS"

sudo apt-get update -y
sudo apt-get install -y gpg zip curl

wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

echo "NORMALY FINISH INSTALL COMMON SERVER SETTINGS"
echo "--------------------------------------------------------"