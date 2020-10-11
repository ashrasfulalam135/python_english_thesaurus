# python_english_thesaurus

#### Open gitbash and make directory
```sh
mkdir Desktop/python_projects/ 
export DEV_HOME=Desktop/python_projects
cd ${DEV_HOME}
```

#### Get the code from git
```sh
git clone https://github.com/ashrasfulalam135/python_english_thesaurus.git
```

#### Build image
```sh
export DEV_HOME=~/Desktop/python_projects/python_english_thesaurus/
cd ${DEV_HOME}/docker_env
docker-compose up -d
```

#### Run app
```sh
python3 app.py
```