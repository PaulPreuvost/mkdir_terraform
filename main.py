import os
import platform
from typing import List

def clearTerminal() -> None:
    system: str = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def verification(user_verification: str) -> bool:
    return user_verification.lower() == "y"

def userVerification(to_verify: str) -> str:
    print(f"Is '{to_verify}' correct? (y/n) ")
    return input()

def askUserPath() -> str:
    clearTerminal()
    print("Where do you want to create your folder? (Copy your path) ")
    origin_path: str = input()
    if not verification(userVerification(origin_path)):
        return askUserPath()
    return origin_path

def askUserProjectName() -> str:
    clearTerminal()
    print("What name do you want to give to your project?")
    project_name: str = input()
    if not verification(userVerification(project_name)):
        return askUserProjectName()
    return project_name

def createProjectStructure(user_path: str, project_name: str) -> None:
    user_folder_path: str = os.path.join(user_path, project_name)

    if not os.path.exists(user_folder_path):
        os.makedirs(user_folder_path)
        
        # Create the Vagrantfile
        vagrantfile_path: str = os.path.join(user_folder_path, "Vagrantfile")
        os.system(f"cd {user_folder_path} && vagrant init")
        
        # Create sub-folders
        sub_folders: List[str] = ['doc', 'env']
        for sub_folder in sub_folders:
            sub_folder_path: str = os.path.join(user_folder_path, sub_folder)
            os.makedirs(sub_folder_path)

            if sub_folder == 'env':
                sub_sub_folders: List[str] = ['cluster', 'provision']
                for sub_sub_folder in sub_sub_folders:
                    sub_sub_folder_path: str = os.path.join(sub_folder_path, sub_sub_folder)
                    os.makedirs(sub_sub_folder_path)

                    if sub_sub_folder == 'cluster':
                        # Create files in cluster folder
                        files_to_create = [
                            "cmd.md", "main.tf", "config.hcl", 
                            "outputs.tf", "provision.sh", "variables.tf"
                        ]
                        for file_name in files_to_create:
                            open(os.path.join(sub_sub_folder_path, file_name), 'w').close()
                        
                        # Create job folder with job.hcl file
                        job_folder_path = os.path.join(sub_sub_folder_path, 'job')
                        os.makedirs(job_folder_path)
                        open(os.path.join(job_folder_path, "job.hcl"), 'w').close()

                    elif sub_sub_folder == 'provision':
                        # Copy files from a 'provision' folder at the root level to this provision folder
                        root_provision_folder = os.path.join(os.getcwd(), 'provision')
                        if os.path.exists(root_provision_folder):
                            for file_name in os.listdir(root_provision_folder):
                                file_path = os.path.join(root_provision_folder, file_name)
                                if os.path.isfile(file_path):
                                    destination_file_path = os.path.join(sub_sub_folder_path, file_name)
                                    with open(file_path, 'rb') as src_file:
                                        with open(destination_file_path, 'wb') as dst_file:
                                            dst_file.write(src_file.read())

        print(f"The folder structure for the project '{project_name}' was created successfully.")
    else:
        print(f"The project folder '{project_name}' already exists.")

def main() -> None:
    user_path: str = askUserPath()
    project_name: str = askUserProjectName()
    createProjectStructure(user_path, project_name)

main()
