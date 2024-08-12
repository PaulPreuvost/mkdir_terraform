echo "START INSTALL TERRAFORM"

# Télécharger et ajouter la clé GPG HashiCorp
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

# Ajouter le dépôt HashiCorp à la liste des sources
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# Mettre à jour la liste des paquets et installer Terraform sans prompts
sudo apt-get update -y && sudo apt-get install -y terraform

echo "FINISHED INSTALL TERRAFORM"
