### Overview:
 
This Web Application has been built using ***Python***(3.8.3) based ***Flask*** Web framework

##### Purpose: 
This Application is a basic Webserver which contains a Home page and info page about an application. Further enhancements can be done to this application by creating URL's as per the requirement and to achieve that "myapp.py" files which hosts the flask web application needs to be updated accordingly.

##### Version: 
Version of the APP has been set as v1.0 as initial and can be changed either in Docker file or while creating a Container and passing it as ENV variable in runtime.

##### Application Debug Level:
 Debug level is set as false by default and can be made true by passing as ENV variable while creating Docker Container

##### Logging: 
Logs of the applicaion can be found in "**myapp.log**" file which will be in the same path as your application,and can be found as you login to your APP container.This logs can be used for your troubleshooting and logging events for your application.Initial Log level has been set to INFO level and same information can be found on the webpage :

Myapp Info Page `http://localhost:5000/info`
#### Application Specifications:
##### OS: 
This application uses UBUNTU based base image and thus will support ubuntu commands which will update it to latest as a part of Docker image build.

##### Port Number:

5000 (set as default but changeable either in DOCKER file or mentioning at runtime during the container creation.)

***WEB URL***: 
`http://localhost:5000/`
`http://localhost:5000/info`

Where it will work with Host Ip as well and can be replaced with localhost in above link.

**Example** : `http://hostip:5000/`

##### Python File name:
 myapp.py and can be found in GIT URL.

##### Docker File: 
Docker file can be found in git hub mentioned below.

##### Git URL:
   [GITHUBLINK](https://github.com/srishkalra/mywebproject.git)


##### Steps to Build Docker image and deploying Container from it.

1) **Download the Docker file**:
   
   ##### Linux/Windows Terminal:
   
   Run the below command on git bash to clone the Repository to get the project files:
   
   Create a new directory "newproject" as below"
     
    `#mkdir newproject`
      
    `#cd newproject` 
      
    Use the below command to clone from GIT repository which contains Dockerfile, and application related files needed to build docker image:


    ```git clone https://github.com/srishkalra/mywebproject.git``` 

    After this you should be able to see the below files including Docker, in your working directory while listing the files.
     
    `myapp.py Dockerfile README.md`
  
 
   
      > Note: For Windows(Docker Desktop),  While cloning the Docker file in your project directory make sure it should be without any extension.
      
      **Below steps are common to any platform Windows/Unix(Just you need Docker installed)**:

 2) **Building a Docker Image using Dockerfile**:
     Downloaded "Dockerfile" from the Step1 can be used to build Docker image:

      Use below commands to Build a docker image:
      
     **Command**: 
       ```docker build -t <imagename>.```
    
     **Example**:
       ```docker build -t myappv1 .```


     > Note: myapp1 will be your image name in this example.

       Below are the sample logs which the above command will end up with for a succesfully built image.

     > Step 12/12 : CMD ["python", "myapp.py"] ---> Running in 517b5c0b8d62 Removing intermediate container 517b5c0b8d62 ---> 671d28fe949b Successfully built 671d28fe949b               Successfully tagged myappv1:latest```
 
 3) **Viewing the Built Docker Images**:
 
    **Command**:```docker images```
    
    > Output: REPOSITORY TAG IMAGE ID CREATED SIZE 
    > myappv1 latest 671d28fe949b 5 minutes ago 228MB

    > Note: Now to use this image to create a container, use image name as "myappv1:latest" as explained in next step.

 4) **Containerizing your Application from newly created Docker image**:

    **Command**: 
     ```docker run -d --name= -p <host_port>:<App(container)_port> <Image_name>```

    > -d option will run container in de-attach mode , and -p is used to mention port number.

    > Note: choose a port which is available in your host machine. In below example, 5000 has been given default in application as ENV variable in Docker file and can be               changed, explained in further instructions.As this application is built on Flask framework which uses 5000 by default.

    **Example**: 
     ```docker run -d --name=appv -p 5000:5000 myappv1:latest ```
  
     ```docker ps```
    > Output:  CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES 1144b339aeec myappv1:latest "python myapp.py" 7 seconds ago Up 5 seconds 0.0.0.0:5000->5000/tcp appv

    > Note: If you want to change the Port number other than 5000(Application port number) which is set as default, can be done using below command, by passing ENV Variable           using "-e" option as show below which creating a container same applies for version as well

    > **Syntax for passing ENV variables if required**
      ```docker run -d --name=<container name> -e PORT=<Container_port> -e VERSION=<app version> -p <Host_port:Container_port> <docker image name>```

       **Example for running container in a different specified port and version and enabling the DEBUG level to true**:
      ```docker run -d --name=appv -e PORT=6001 -e VERSION=v2.0 -e DEBUG=true -p 6000:6001 myappv1:latest```
       > Here 6001 is set to the Application Port Number at runtime, so Application will launch in 6001 Port number inside the container.

 5) **Check if Application is running successfully**: 
 
    **Command**: 
    ```docker logs <container name>```
   
    **Example**:
    ```docker logs appv```
    **Output** : It will show below logs:
      > Serving Flask app "myapp" (lazy loading)
        Environment: production
        WARNING: This is a development server. Do not use it in a production deployment.
        Use a production WSGI server instead.
        Debug mode: on

    <br>
 6) ***Login to your Containerized Application***
 
    **Command**:
    ```docker exec -it <container name> /bin/bash```
   
    **Example**:
    ```docker exec -it appv /bin/bash```

    **Output** : <br>You should be inside your container which runs your application.
    <br>

 7) **Application Launching**:
 
     Run the below commands inside the container :

    **Testing Homepage**: 

    ```curl ip:portnumber/```

     **Example**:
     > Note:curl localhost:5000 This should give the Home page of this Web Application which says "Welcome to Web APP!" as below and it is a success message(APP launched                successfull with homepage loaded)

     ```root@9bb260d373ab:/myfirstproject# curl localhost:5000     Welcome to Web APP!```

     Same you should be able to see on your browser.
     > Note: You should be using Host Port when you are launching the APP outside the container, and use Container port only when you are inside the container APP.


     **<br>Testing Info Page**
     ```curl ip:portnumber/info```
  
     **Example**: 
     ```curl localhost:5000/info```

     > This should show the information about the application which is in JSON format in this case as below:

     ```root@9bb260d373ab:/myfirstproject# curl localhost:5000/info [ { "service": [ { "git sha": "d7a9795c8e2346eb791540f797d6272916a3bce9", "service": "app", "version": "v1.0"        }, { "loglevel": "INFO", "port": "5000" } ] }, 200 ]```

     > Same you should be able to see on your browser.

     > Note: if you are using checking the above command on Host. Kindly use Host port Number in `http://localhost:<hostport no>/info` which is same in this case.

 8) **Checking the Application logging**:
  
     Application logs can be found inside the container , the momemt you login , the same path where you get the prompt. As it is ubuntu based image, **linux** based command          will work.<br>
    **Example**: 
    ```root@9bb260d373ab:/myfirstproject# ls```
    ```Dockerfile README.md myapp.py myapp.log```
     
    ***To see contents of myapp.log, use below command***:

    > root@9bb260d373ab:/mywebproject# cat myapp.log 
    2020-08-17 10:37:10,475 INFO werkzeug MainThread : * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit) 2020-08-17 10:37:10,476 INFO werkzeug MainThread : * Restarting       with stat 2020-08-17 10:37:10,710 WARNING werkzeug MainThread : * Debugger is active! 2020-08-17 10:37:10,711 INFO werkzeug MainThread : * Debugger PIN: 196-235-887 2020-08-     17 10:37:22,046 INFO app Thread-2 : Displaying the info logs 2020-08-17 10:37:22,047 INFO werkzeug Thread-2 : 172.17.0.1 - - [17/Aug/2020 10:37:22] "GET /info HTTP/1.1" 200     2020-08-17 10:38:00,674 INFO app Thread-3 : Displaying the info logs 2020-08-17 10:38:00,675 INFO werkzeug Thread-3 : 127.0.0.1 - - [17/Aug/2020 10:38:00] "GET /info             HTTP/1.1" 200

     #### Future Scope:
     For future enhancement, Docker file can be cloned to user repository and then after the the updation of the code, code can be version controlled via GIT using below               command.

     **Pre-requisites**: GIT client should be installed on your system, on the terminal run the below commands,
     Clone your GITHUB repository using this command to your client system

       `#git clone https://github.com/srishkalra/mywebproject.git` 

       Go to your clone repository/directory

      `#cd /mywebproject` 

       View files

       `#ls` 
       
       Switch to your test branch to make changes on your files/codes
       
       `#git checkout -b testbranch`
       
       Check which branch you are in currently(Should be testbranch)
       
       `#git branch`

       Modify your code changes to the existing file

       `#vi Dockerfile` 

       Use git add . in your bash to add all the files to the given directory - This command will add your modified files for staging

      `#git add .` 
      
       Use git status in your bash to view all the files which are going to be staged to the first commit

      `#git status` 
        
       You can create a commit message by git commit -m 'your message', which adds the change to your local repository

      `#git commit -m "New commit messsage" Dockerfile` 
     
       Now switch to master branch to merge your testbranch code
     
      `#git checkout master`
     
       Merge the changes(modified Dockerfile) you have done in the testbranch to the master branch
     
      `#git merge testbranch`

       Connect to your remote GITHUB repository and be ready to push your changes - Only use if you have not executed the git clone command in the first step

      `#git remote add origin https://github.com/srishkalra/mywebproject.git`

       Provide your GITHUB login details for pushing local changes/contents to your GitHub Repository
     
      `#git push origin master` 
     
       ##### Risk/Decisions: 
       GIT url need to be updated in Docker file to user git URL if path of "myapp.py"(Flask APP file).
 
