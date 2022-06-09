import subprocess
import getpass
import os
import requests
import time

class docker_execute():
    # Links für Windows-Version
    URLVSCODE = "https://az764295.vo.msecnd.net/stable/c3511e6c69bb39013c4a4b7b9566ec1ca73fc4d5/VSCodeUserSetup-x64-1.67.2.exe"
    URLDOCKER = "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"

    # Standards
    ProgramFiles = ["Docker.exe", "VSCode.exe"]
    Username = getpass.getuser()
    Destination = f'C:\\Users\\{Username}\\Downloads\\'
    #-------------------------------------------------Container Commands------------------------------------------------------#

    def complete_installation():
        try:
            filepathDocker = docker_execute.setDestination(0)
            filepathVSCode = docker_execute.setDestination(1)
            downloadDocker = requests.get(
                docker_execute.URLDOCKER, allow_redirects=True)
            downloadVSCode = requests.get(
                docker_execute.URLVSCODE, allow_redirects=True)
            with open(filepathDocker, "wb") as Docker, open(filepathVSCode, "wb") as VSCode:
                Docker.write(downloadDocker.content)
                VSCode.write(downloadVSCode.content)
            subprocess.call(filepathDocker + " batch.exe", shell=True)
            subprocess.call(filepathVSCode + " batch.exe", shell=True)
        except:
            pass

    def installation_docker():
        try:
            filepath = docker_execute.setDestination(0)
            download = requests.get(
                docker_execute.URLDOCKER, allow_redirects=True)
            with open(filepath, "wb") as file:
                file.write(download.content)
            subprocess.call(filepath + " batch.exe", shell=True)
        except:
            pass

    def installtion_vscode():
        try:
            filepath = docker_execute.setDestination(1)
            download = requests.get(
                docker_execute.URLVSCODE, allow_redirects=True)
            with open(filepath, "wb") as file:
                file.write(download.content)
            subprocess.call(filepath + " batch.exe", shell=True)
        except:
            pass

    def create_container(containername):
        os.system(f"docker {containername} create")

    def edit_container(containername):
        os.system(f"docker update {containername}")

    def delete_container(containername):
        os.system(f"docker rm /{containername}")

    def start_container(containername):
        os.system(f"docker start {containername}")

    def stop_container(containername):
        os.system(f"docker stop {containername}")

    def restart_container(containername):
        os.system(f"docker restart {containername}")

    def change_containername(containername, newcontainername):
        os.system(f" docker rename {containername} {newcontainername}")

    def list_of_containers():
        os.system("docker ps")
    #-------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------Image Commands----------------------------------------------------------#

    def create_image(username, imagename):
        os.system(f"docker build {username}/{imagename}")

    def delete_image(imagename):
        os.system(f"docker rmi {imagename}")

    def change_imagename(imagename,newimagename):
        os.system(f"docker tag {imagename} {newimagename}")

    def list_of_images():
        os.system("docker images")

    def touch_dockerfile():
        os.system("touch Dockerfile")
        dockerfile = open("Dockerfile", "w")
        dockerfile.write("""FROM node:16

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 8080
CMD [ "node", "server.js" ]
""")
        dockerfile.close()

    def setDestination(Input):
        filepath = docker_execute.Destination + \
            docker_execute.ProgramFiles[Input]
        return filepath
